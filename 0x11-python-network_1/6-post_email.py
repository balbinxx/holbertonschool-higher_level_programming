#!/usr/bin/python3
"""
Random WRS
"""

import requests
from sys import argv


if __name__ == "__main__":
    val = {'email': argv[2]}
    rp = requests.post(argv[1], data=val)
    print(rp.text)
