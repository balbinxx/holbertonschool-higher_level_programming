#!/usr/bin/python3
"""
Random misc
"""

import requests
from sys import argv

if __name__ == "__main__":
    rp = requests.get(argv[1])
    print(rp.headers.get('X-Request-Id'))
