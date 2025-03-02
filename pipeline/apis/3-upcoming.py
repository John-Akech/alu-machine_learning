#!/usr/bin/env python3
"""Pipeline API"""

import requests


if __name__ == '__main__':
    """Pipeline API"""
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    r = requests.get(url)

    # Check if the request was successful
    if r.status_code != 200:
        print("Failed to retrieve data from SpaceX API, status code:", r.status_code)
        exit(1)

    # Check if the response is empty
    data = r.json()
    if not data:
        print("No upcoming launches found.")
        exit(1)

    # Initialize variables to track the most recent launch
    recent = None
    launch_name = ""
    date = ""
    rocket_number = ""
    launch_number = ""

    # Iterate through the upcoming launches
    for dic in data:
        new = int(dic["date_unix"])
        if recent is None or new < recent:
            recent = new
            launch_name = dic["name"]
            date = dic["date_local"]  # Keep the date in the original format
            rocket_number = dic["rocket"]
            launch_number = dic["launchpad"]

    # Fetch rocket name
    rurl = "https://api.spacexdata.com/v4/rockets/{}".format(rocket_number)
    rocket_response = requests.get(rurl)
    if rocket_response.status_code != 200:
        print("Failed to retrieve rocket data, status code:", rocket_response.status_code)
        exit(1)
    rocket_name = rocket_response.json()["name"]

    # Fetch launchpad details
    lurl = "https://api.spacexdata.com/v4/launchpads/{}".format(launch_number)
    launchpad_response = requests.get(lurl)
    if launchpad_response.status_code != 200:
        print("Failed to retrieve launchpad data, status code:", launchpad_response.status_code)
        exit(1)
    launchpad = launchpad_response.json()
    launchpad_name = launchpad["name"]
    launchpad_local = launchpad["locality"]

    # Format the output string
    string = "{} ({}) {} - {} ({})".format(
        launch_name, date, rocket_name, launchpad_name, launchpad_local
    )

    print(string)
