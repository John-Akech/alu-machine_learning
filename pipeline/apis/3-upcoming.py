#!/usr/bin/env python3

import requests
from datetime import datetime

# Function to fetch the upcoming launch from the SpaceX API
def fetch_upcoming_launch():
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    
    if response.status_code == 200:
        launches = response.json()
        # Sort launches by date_unix and take the earliest one
        upcoming_launch = sorted(launches, key=lambda x: x['date_unix'])[0]

        # Extract relevant details
        launch_name = upcoming_launch['name']
        launch_date = datetime.utcfromtimestamp(upcoming_launch['date_unix'])
        local_date = launch_date.strftime('%Y-%m-%d %H:%M:%S')  # Format date in local time
        rocket_name = upcoming_launch['rocket']['name']
        launchpad_name = upcoming_launch['launchpad']['name']
        launchpad_locality = upcoming_launch['launchpad']['locality']

        # Return the formatted output
        return f"{launch_name} ({local_date}) {rocket_name} - {launchpad_name} ({launchpad_locality})"
    else:
        return "Error fetching upcoming launch data."

# Main execution block to prevent code from running when imported
if __name__ == '__main__':
    # Fetch and display the upcoming launch
    print(fetch_upcoming_launch())
