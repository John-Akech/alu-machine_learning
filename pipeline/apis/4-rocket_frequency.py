#!/usr/bin/env python3
"""Pipeline Api"""
import requests


if __name__ == '__main__':
    """pipeline api"""
    url = "https://api.spacexdata.com/v4/launches"
    r = requests.get(url)
    
    # Initialize an empty dictionary to count launches for each rocket
    rocket_dict = {}

    for launch in r.json():
        rocket_id = launch["rocket"]
        if rocket_id in rocket_dict:
            rocket_dict[rocket_id] += 1
        else:
            rocket_dict[rocket_id] = 1

    # Fetch rocket names and print the counts
    for key, value in sorted(rocket_dict.items(), key=lambda kv: kv[1], reverse=True):
        rurl = f"https://api.spacexdata.com/v4/rockets/{key}"
        req = requests.get(rurl)
        
        # Check if the request was successful
        if req.status_code == 200:
            rocket_name = req.json()["name"]
            print(f"{rocket_name}: {value}")
        else:
            print(f"Error fetching rocket name for ID {key}")
