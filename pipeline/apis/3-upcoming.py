#!/usr/bin/env python3
"""Pipeline API"""

import requests
from datetime import datetime


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
            date = dic["date_local"]
            rocket_number = dic["rocket"]
            launch_number = dic["launchpad"]

    # Fetch rocket name
    rurl = f"https://api.spacexdata.com/v4/rockets/{rocket_number}"
    rocket_name = requests.get(rurl).json()["name"]

    # Fetch launchpad details
    lurl = f"https://api.spacexdata.com/v4/launchpads/{launch_number}"
    launchpad = requests.get(lurl).json()
    launchpad_name = launchpad["name"]
    launchpad_local = launchpad["locality"]

    # Format the output string
    string = "{} ({}) & {} - {} ({})".format(
        launch_name, date, rocket_name, launchpad_name, launchpad_local
    )

    print(string)
