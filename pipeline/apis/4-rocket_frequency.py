#!/usr/bin/env python3
"""Pipeline Api"""
import requests

if __name__ == '__main__':
    """pipeline api"""
    url = "https://api.spacexdata.com/v4/launches"
    r = requests.get(url)
    rocket_counts = {}

    for launch in r.json():
        rocket_id = launch["rocket"]
        if rocket_id in rocket_counts:
            rocket_counts[rocket_id] += 1
        else:
            rocket_counts[rocket_id] = 1

    rocket_list = []
    for rocket_id, count in rocket_counts.items():
        rurl = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
        response = requests.get(rurl)
        name = response.json()["name"]
        rocket_list.append((name, count))

    sorted_rockets = sorted(rocket_list, key=lambda x: (-x[1], x[0]))

    for name, count in sorted_rockets:
        print(f"{name}: {count}")
