#!/usr/bin/python3
"""
Random AGN
"""

import requests
from sys import argv


if __name__ == "__main__":
    rp = requests.get(argv[1])
    if rp.status_code >= 400:
        print("Error code: {}".format(rp.status_code))
    else:
        print(rp.text)
