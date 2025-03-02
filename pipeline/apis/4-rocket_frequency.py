#!/usr/bin/env python3

import requests
from collections import Counter

def get_launches():
    # SpaceX API endpoint for launches
    url = 'https://api.spacexdata.com/v4/launches'
    launches = []

    # Fetch data in pages (SpaceX API supports pagination)
    page = 1
    while True:
        response = requests.get(f'{url}?page={page}')
        data = response.json()
        
        if not data:
            break
        
        # Collect rocket names from each launch
        launches.extend(launch['rocket'] for launch in data)
        page += 1

    return launches

def main():
    # Get list of all rocket names from launches
    launches = get_launches()

    # Count the number of launches per rocket
    rocket_count = Counter(launches)

    # Sort first by the number of launches (descending), then alphabetically
    sorted_rockets = sorted(rocket_count.items(), key=lambda x: (-x[1], x[0]))

    # Print the results
    for rocket, count in sorted_rockets:
        print(f'{rocket}: {count}')

if __name__ == '__main__':
    main()
