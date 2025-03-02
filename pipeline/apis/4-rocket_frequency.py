#!/usr/bin/env python3
"""Pipeline Api"""
import requests


if __name__ == '__main__':
    """pipeline api"""
    # Fetching launches data
    url = "https://api.spacexdata.com/v4/launches"
    r = requests.get(url)
    
    # Check if the request was successful
    if r.status_code != 200:
        print("Error fetching launch data")
        exit()
    
    launches = r.json()  # Get all launches data
    print("Launches data fetched successfully")

    # Fetch rocket data separately to map rocket IDs to names
    rocket_url = "https://api.spacexdata.com/v4/rockets"
    rocket_response = requests.get(rocket_url)
    if rocket_response.status_code != 200:
        print("Error fetching rocket data")
        exit()

    rockets = rocket_response.json()  # Get all rocket data
    rocket_names = {rocket["id"]: rocket["name"] for rocket in rockets}
    print("Rocket names mapped successfully")

    # Initialize an empty dictionary to count launches for each rocket
    rocket_dict = {}

    # Process each launch and count the rockets
    for launch in launches:
        rocket_id = launch["rocket"]
        if rocket_id in rocket_dict:
            rocket_dict[rocket_id] += 1
        else:
            rocket_dict[rocket_id] = 1

    # Fetch rocket names and print the counts
    for rocket_id, count in sorted(rocket_dict.items(), key=lambda kv: kv[1], reverse=True):
        rocket_name = rocket_names.get(rocket_id, "Unknown")
        print(f"{rocket_name}: {count}")
