#!/usr/bin/env python3
"""Pipeline Api"""
import requests

def fetch_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from the SpaceX API")
        return []

def count_launches_per_rocket(launches):
    rocket_count = {}
    for launch in launches:
        rocket_name = launch['rocket']
        if rocket_name in rocket_count:
            rocket_count[rocket_name] += 1
        else:
            rocket_count[rocket_name] = 1
    return rocket_count

def get_rocket_name(rocket_id):
    url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['name']
    else:
        return f"Unknown Rocket ({rocket_id})"

def main():
    launches = fetch_launches()
    rocket_count = count_launches_per_rocket(launches)
    
    # Map rocket IDs to names
    rocket_name_count = {}
    for rocket_id, count in rocket_count.items():
        rocket_name = get_rocket_name(rocket_id)
        rocket_name_count[rocket_name] = count
    
    # Sort by count descending, then by name ascending
    sorted_rockets = sorted(rocket_name_count.items(), key=lambda x: (-x[1], x[0]))
    
    for rocket_name, count in sorted_rockets:
        print(f"{rocket_name}: {count}")

if __name__ == "__main__":
    main()
