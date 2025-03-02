#!/usr/bin/env python3

import requests
import sys

def fetch_launch_data():
    # SpaceX API URL for fetching launches data
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return {}
    
    return response.json()

def fetch_rocket_names():
    # SpaceX API URL for fetching rocket data
    url = "https://api.spacexdata.com/v4/rockets"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching rocket names: {response.status_code}")
        return {}
    
    rockets = response.json()
    rocket_names = {rocket["id"]: rocket["name"] for rocket in rockets}
    
    return rocket_names

def count_launches_by_rocket(launches):
    rocket_launch_count = {}
    
    for launch in launches:
        rocket_id = launch["rocket"]
        if rocket_id in rocket_launch_count:
            rocket_launch_count[rocket_id] += 1
        else:
            rocket_launch_count[rocket_id] = 1
            
    return rocket_launch_count

def display_rocket_launches(rocket_launch_count, rocket_names):
    # Sort by number of launches (descending), then by rocket name alphabetically
    sorted_rockets = sorted(rocket_launch_count.items(), key=lambda x: (-x[1], rocket_names[x[0]]))
    
    for rocket_id, count in sorted_rockets:
        rocket_name = rocket_names.get(rocket_id, "Unknown")
        print(f"{rocket_name}: {count}")

if __name__ == "__main__":
    # Fetch launches data
    launches = fetch_launch_data()

    if not launches:
        sys.exit(1)

    # Fetch rocket names
    rocket_names = fetch_rocket_names()

    if not rocket_names:
        sys.exit(1)

    # Count launches per rocket
    rocket_launch_count = count_launches_by_rocket(launches)

    # Display the results
    display_rocket_launches(rocket_launch_count, rocket_names)
