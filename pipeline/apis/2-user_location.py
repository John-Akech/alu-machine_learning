#!/usr/bin/env python3
""" Return list of ships"""

import sys
import requests
import time

def get_user_location(api_url):
    response = requests.get(api_url)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers.get('X-Ratelimit-Reset', 0))
        current_time = int(time.time())
        minutes_to_reset = (reset_time - current_time) // 60
        print("Reset in {} min".format(minutes_to_reset))
    else:
        user_data = response.json()
        location = user_data.get('location')
        print(location if location else "Location not specified")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <API_URL>")
        sys.exit(1)

    api_url = sys.argv[1]
    get_user_location(api_url)
