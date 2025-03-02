#!/usr/bin/env python3

"""Fetch and print the location of a given GitHub user using the GitHub API"""

import requests
import sys
import time

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        res = requests.get(url)

        if res.status_code == 403:
            rate_limit = res.headers.get('X-Ratelimit-Reset')
            if rate_limit:
                reset_time = int(rate_limit)
                current_time = int(time.time())
                diff = (reset_time - current_time) // 60
                print(f"Reset in {diff} min")
            else:
                print("Rate limit exceeded, but reset time unavailable.")
        
        elif res.status_code == 404:
            print("Not found")
        
        elif res.status_code == 200:
            res_json = res.json()
            print(res_json.get("location", "No location provided"))
        
        else:
            print(f"Unexpected error: {res.status_code}")

    except requests.RequestException as e:
        print(f"Error: {e}")
