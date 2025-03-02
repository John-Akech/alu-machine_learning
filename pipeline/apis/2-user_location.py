#!/usr/bin/env python3

""" Return location of a user from GitHub API """

import requests
import sys
import time


def get_user_location(url):
    """Retrieve and print user location from GitHub API"""
    try:
        res = requests.get(url)

        # If rate limit is exceeded, handle 403 response
        if res.status_code == 403:
            rate_limit = int(res.headers.get('X-Ratelimit-Reset'))
            current_time = int(time.time())
            diff = (rate_limit - current_time) // 60  # calculate difference in minutes
            print(f"Reset in {diff} min")
            return
        
        # If user not found, handle 404 response
        if res.status_code == 404:
            print("Not found")
            return

        # If status code is 200, extract and print location
        if res.status_code == 200:
            data = res.json()
            location = data.get('location', 'Location not provided')
            print(location)
            return
        
        # Handle any unexpected status code
        print(f"Unexpected status code: {res.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
    else:
        get_user_location(sys.argv[1])
