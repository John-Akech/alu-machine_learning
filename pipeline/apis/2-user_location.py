#!/usr/bin/env python3

""" Return the location of a specific GitHub user """

import requests
import sys
import time

def get_user_location(api_url):
    res = requests.get(api_url)

    if res.status_code == 403:
        rate_limit_reset = int(res.headers.get('X-Ratelimit-Reset', 0))
        current_time = int(time.time())
        diff = (rate_limit_reset - current_time) // 60
        print("Reset in {} min".format(diff))
    elif res.status_code == 404:
        print("Not found")
    elif res.status_code == 200:
        user_data = res.json()
        print(user_data.get('location', 'Location not provided'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <API_URL>")
        sys.exit(1)

    api_url = sys.argv[1]
    get_user_location(api_url)
