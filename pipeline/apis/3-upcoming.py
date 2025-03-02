#!/usr/bin/env python3
"""Pipeline API"""

import requests


if __name__ == '__main__':
    """Pipeline API"""
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    r = requests.get(url)

    # Initialize variables to track the most recent launch
    recent = None
    launch_name = ""
    date = ""
    rocket_number = ""
    launch_number = ""

    # Iterate through the upcoming launches
    for dic in r.json():
        new = int(dic["date_unix"])
        if recent is None or new < recent:
            recent = new
            launch_name = dic["name"]
            date = dic["date_local"]  # Keep the date in the original format
            rocket_number = dic["rocket"]
            launch_number = dic["launchpad"]

    # Fetch rocket name
    rurl = "https://api.spacexdata.com/v4/rockets/{}".format(rocket_number)
    rocket_name = requests.get(rurl).json()["name"]

    # Fetch launchpad details
    lurl = "https://api.spacexdata.com/v4/launchpads/{}".format(launch_number)
    launchpad = requests.get(lurl).json()
    launchpad_name = launchpad["name"]
    launchpad_local = launchpad["locality"]

    # Format the output string
    string = "{} ({}) & {} - {} ({})".format(
        launch_name, rocket_name, date, launchpad_name, launchpad_local
    )

    print(string)
