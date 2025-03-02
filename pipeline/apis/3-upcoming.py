#!/usr/bin/env python3

"""
By using the (unofficial) SpaceX API, write a
script that displays the upcoming launch with
these information:

Name of the launch
The date (in local time)
The rocket name
The name (with the locality) of the launchpad
Format:
<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)

The “upcoming launch” is the one which is the soonest
from now, in UTC (we encourage you to use the date_unix
for sorting it) - and if 2 launches have the same date, use
the first one in the API result.

Your code should not be executed when the file
is imported (you should use if __name__ == '__main__':)
"""

import requests as res

from datetime import datetime, timezone, timedelta


def upComing():
    """
    The “upcoming launch” is the one which is the soonest
    from now, in UTC (we encourage you to use the date_unix
    for sorting it) - and if 2 launches have the same date, us
    the first one in the API result.
    """
    link = "https://api.spacexdata.com/v4/launches/upcoming"
    respond = res.get(link)
    launches = respond.json()

    # grouping launch by date
    launches.sort(key=lambda x: x["date_unix"])
    upcoming_launch = launches[0]

    launch_name = upcoming_launch["name"]
    date_unix = upcoming_launch["date_unix"]
    rocket_id = upcoming_launch["rocket"]
    launchpad_id = upcoming_launch["launchpad"]

    # changing date to UTC-4
    launch_date_utc = datetime.fromtimestamp(date_unix, tz=timezone.utc)
    launch_date_local = launch_date_utc.astimezone(timezone(
        timedelta(hours=-4))
    )
    launch_date_str = launch_date_local.strftime('%Y-%m-%dT%H:%M:%S%z')
    launch_date_str = "{}:{}".format(
        launch_date_str[:-2], launch_date_str[-2:]
    )

    # rocket

    rocket_link = "https://api.spacexdata.com/v4/rockets/{}".format(rocket_id)
    rocket_respond = res.get(rocket_link)
    rocket_name = rocket_respond.json()["name"]

    # lauchpad

    launchp_link = "https://api.spacexdata.com/v4/launchpads/{}".format(
        launchpad_id
        )
    launchp_respond = res.get(launchp_link)
    launchp_data = launchp_respond.json()
    launchp_name = launchp_data["name"]
    launchp_locality = launchp_data["locality"]

    # output

    output = "{} ({}) {} - {} ({})".format(
            launch_name,
            launch_date_str,
            rocket_name,
            launchp_name,
            launchp_locality,
            )

    return output


if __name__ == "__main__":
    print(upComing())
