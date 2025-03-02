#!/usr/bin/env python3

""" Return list of ships"""

import requests
import sys
import time

if __name__ == "__main__":
    res = requests.get(sys.argv[1])

    if res.status_code == 403:
        rate_limit = int(res.headers.get('X-Ratelimit-Reset'))
        current_time = int(time.time())
        diff = (rate_limit - current_time) // 60
        print("Reset in {} min".format(diff))
        # get remaining rate

    elif res.status_code == 404:
        print("Not found")
    elif res.status_code == 200:
        res = res.json()
        
        # Print all the data to check the structure
        print(res)

        # Assuming the structure contains detailed data, print location
        # Change this based on your actual response structure
        if 'location' in res:
            print(res['location'])
        else:
            # If 'location' key doesn't exist, look for other keys
            print("Location not found in the response")
