#!/usr/bin/env python3
"""Pipeline Api"""
import requests

if __name__ == '__main__':
    """pipeline api"""
    url = "https://api.spacexdata.com/v4/launches"
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print("Error fetching launches data: {}".format(e))
        exit(1)

    # Initialize an empty dictionary to count launches for each rocket
    rocket_dict = {}

    for launch in r.json():
        if "rocket" not in launch:
            continue  # Skip launches without a rocket field
        rocket_id = launch["rocket"]
        if rocket_id in rocket_dict:
            rocket_dict[rocket_id] += 1
        else:
            rocket_dict[rocket_id] = 1

    # Fetch rocket names and print the counts
    for key, value in sorted(rocket_dict.items(), key=lambda kv: kv[1], reverse=True):
        rurl = "https://api.spacexdata.com/v4/rockets/{}".format(key)
        try:
            req = requests.get(rurl)
            req.raise_for_status()  # Raise an exception for HTTP errors
            rocket_name = req.json()["name"]
            print("{}: {}".format(rocket_name, value))
        except requests.exceptions.RequestException as e:
            print("Error fetching rocket name for ID {}: {}".format(key, e))
