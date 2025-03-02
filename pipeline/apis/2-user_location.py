#!/usr/bin/env python3
import requests
import sys
import time

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code == 403:
        rate_limit = int(res.headers.get('X-Ratelimit-Reset', 0))
        current_time = int(time.time())
        diff = (rate_limit - current_time) // 60
        print(f"Reset in {diff} min")
    
    elif res.status_code == 404:
        print("Not found")

    elif res.status_code == 200:
        data = res.json()
        print("Full API Response:", data)  # Debugging line
        print(data.get("location", "No location available"))  # Safer way to fetch location
