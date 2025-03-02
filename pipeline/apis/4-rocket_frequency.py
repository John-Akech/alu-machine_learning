#!/usr/bin/env python3
""" Calculates how many launches each rocket has been used
"""
import requests


def get_all_launches():
    """ Fetch all launches, handling pagination """
    launches_url = "https://api.spacexdata.com/v5/launches"
    launches = []
    while launches_url:
        response = requests.get(launches_url)
        if response.status_code == 200:
            data = response.json()
            launches.extend(data['docs'])  # 'docs' contains the launch data
            launches_url = data.get('next')  # 'next' is the URL for the next page
        else:
            print(f"Error fetching data: {response.status_code}")
            break
    return launches


if __name__ == "__main__":
    # Get all launches
    launches = get_all_launches()

    if not launches:
        print("No launch data found.")
    else:
        # Create a dictionary to use as a tally
        rocket_frequency = {}

        # Count launches per rocket
        for launch in launches:
            rocket_id = launch['rocket']
            rocket_frequency[rocket_id] = rocket_frequency.get(rocket_id, 0) + 1

        # Get names for each rocket
        rocket_names = {}
        for rocket_id in rocket_frequency.keys():
            rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
            response = requests.get(rocket_url)
            if response.status_code == 200:
                rocket = response.json()
                rocket_names[rocket_id] = rocket['name']
            else:
                print(f"Error fetching rocket name: {response.status_code}")

        # Print rocket usage
        sorted_rockets = sorted(
            rocket_frequency.items(),
            key=lambda rocket: (-rocket[1], rocket_names.get(rocket[0], 'Unknown'))
        )

        for rocket, frequency in sorted_rockets:
            rocket_name = rocket_names.get(rocket, 'Unknown')
            print(f"{rocket_name}: {frequency}")
