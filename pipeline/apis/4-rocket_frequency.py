#!/usr/bin/env python3

import requests
from collections import defaultdict

def get_rocket_launches():
    # Fetch the launches data from the SpaceX API
    response = requests.get('https://api.spacexdata.com/v4/launches')
    response.raise_for_status()  # Raise an error for bad responses
    launches = response.json()
    
    # Dictionary to count launches per rocket
    rocket_count = defaultdict(int)

    # Count the number of launches for each rocket
    for launch in launches:
        rocket_id = launch['rocket']
        # Fetch rocket information using the rocket ID
        rocket_info_response = requests.get(f'https://api.spacexdata.com/v4/rockets/{rocket_id}')
        rocket_info_response.raise_for_status()  # Raise an error for bad responses
        rocket_info = rocket_info_response.json()
        rocket_name = rocket_info['name']
        rocket_count[rocket_name] += 1

    # Sort the rockets by number of launches (descending) and then by name (ascending)
    sorted_rockets = sorted(rocket_count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_rockets

if __name__ == '__main__':
    rocket_launches = get_rocket_launches()
    for rocket, count in rocket_launches:
        print(f"{rocket}: {count}")
