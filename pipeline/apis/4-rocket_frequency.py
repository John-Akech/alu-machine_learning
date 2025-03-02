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
        data = response.json()
        launches.extend(data['docs'])  # 'docs' contains the launch data
        launches_url = data.get('next')  # 'next' is the URL for the next page
    return launches


if __name__ == "__main__":
    # Get all launches
    launches = get_all_launches()

    # Create a dictionary to use as a tally
    rocket_frequency = {}

    # Count launches per rocket
    for launch in launches:
        rocket_id = launch['rocket']

        if rocket_id in rocket_frequency:
            rocket_frequency[rocket_id]['frequency'] += 1
        else:
            rocket_frequency[rocket_id] = {}
            rocket_frequency[rocket_id]['frequency'] = 1

    # Get names for each rocket
    for id in rocket_frequency.keys():
        rocket_url = "https://api.spacexdata.com/v4/rockets/{}".format(id)
        response = requests.get(rocket_url)
        rocket = response.json()
        rocket_name = rocket['name']
        rocket_frequency[id]['name'] = rocket_name

    # Sort the rockets
    sorted_rockets = sorted(
        rocket_frequency.items(),
        key=lambda rocket: (-rocket[1]["frequency"], rocket[1]["name"])
    )

    for rocket, info in sorted_rockets:
        print("{}: {}".format(info['name'], info['frequency']))
