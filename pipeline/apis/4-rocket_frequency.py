#!/usr/bin/env python3

"""
By using the (unofficial) SpaceX API, write a script
that displays the number of launches per rocket.

The script should:
- Retrieve all SpaceX launches
- Count the number of launches per rocket
- Fetch rocket names
- Sort results by number of launches (descending)
- Print results in the format: <rocket name>: <launch count>

Your code should not be executed when the file is imported
(you should use if __name__ == '__main__':)
"""

import requests as res
from collections import Counter


def launchCount():
    """
    Retrieves all SpaceX launches and counts the number per rocket.
    """
    link = "https://api.spacexdata.com/v4/launches"
    respond = res.get(link)

    if respond.status_code != 200:
        return "Error: Unable to fetch launch data"

    launches = respond.json()

    # Count launches per rocket ID
    rocket_counts = Counter(launch["rocket"] for launch in launches)

    # Fetch rocket names
    rocket_link = "https://api.spacexdata.com/v4/rockets"
    rocket_respond = res.get(rocket_link)

    if rocket_respond.status_code != 200:
        return "Error: Unable to fetch rocket data"

    rockets = rocket_respond.json()
    rocket_names = {rocket["id"]: rocket["name"] for rocket in rockets}

    # Format and sort output
    output = sorted(
        [(rocket_names.get(rid, "Unknown Rocket"), count)
         for rid, count in rocket_counts.items()],
        key=lambda x: (-x[1], x[0])
    )

    return output


if __name__ == "__main__":
    rocket_launch_counts = launchCount()

    if isinstance(rocket_launch_counts, str):
        print(rocket_launch_counts)
    else:
        for rocket_name, count in rocket_launch_counts:
            print("{}: {}".format(rocket_name, count))
