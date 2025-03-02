#!/usr/bin/env python3

import requests
import sys
import time

def fetch_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 403:
        rate_limit = int(response.headers.get('X-Ratelimit-Reset'))
        current_time = int(time.time())
        diff = (rate_limit - current_time) // 60
        print(f"Reset in {diff} min")
    elif response.status_code == 404:
        print("User not found")
    elif response.status_code == 200:
        user_data = response.json()
        print(f"User Location: {user_data.get('location', 'No location provided')}")
    else:
        print(f"Failed to fetch user data: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 user_location.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    fetch_user_data(username)
