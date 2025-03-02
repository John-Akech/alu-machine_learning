#!/usr/bin/env python3
"""Display upcoming SpaceX launch information"""

import requests
import sys

def main():
    # SpaceX API endpoint for upcoming launches
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    
    # Make a request to the SpaceX API
    res = requests.get(url)

    # Check if the request was successful
    if res.status_code != 200:
        print("Failed to retrieve data from SpaceX API, status code:", res.status_code)
        return

    # Parse the JSON response
    launches = res.json()

    # Initialize variables to track the soonest upcoming launch
    soonest_launch = None

    # Iterate through the upcoming launches to find the soonest one
    for launch in launches:
        if soonest_launch is None or launch["date_unix"] < soonest_launch["date_unix"]:
            soonest_launch = launch

    # If no upcoming launch is found, exit
    if soonest_launch is None:
        print("No upcoming launches found.")
        return

    # Extract the required information
    launch_name = soonest_launch["name"]
    date = soonest_launch["date_local"]
    rocket_id = soonest_launch["rocket"]
    launchpad_id = soonest_launch["launchpad"]

    # Fetch rocket name
    rocket_res = requests.get(f"https://api.spacexdata.com/v4/rockets/{rocket_id}")
    if rocket_res.status_code != 200:
        print("Failed to retrieve rocket data, status code:", rocket_res.status_code)
        return
    rocket_name = rocket_res.json()["name"]

    # Fetch launchpad details
    launchpad_res = requests.get(f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}")
    if launchpad_res.status_code != 200:
        print("Failed to retrieve launchpad data, status code:", launchpad_res.status_code)
        return
    launchpad = launchpad_res.json()
    launchpad_name = launchpad["name"]
    launchpad_locality = launchpad["locality"]

    # Format the output string
    output = f"{launch_name} ({date}) {rocket_name} - {launchpad_name} ({launchpad_locality})"
    print(output)

if __name__ == "__main__":
    main()
