#!/usr/bin/env python3
""" Return list of ships"""

import sys
import requests
import time

def get_github_user_location(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("location", "Location not available"))
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers.get("X-RateLimit-Reset", time.time()))
        minutes_remaining = max(0, (reset_time - time.time()) // 60)
        print(f"Reset in {int(minutes_remaining)} min")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub_API_URL>")
        sys.exit(1)
    
    api_url = sys.argv[1]
    get_github_user_location(api_url)
