#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable
"""

from sys import argv
from urllib import request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as rp:
        print(rp.getheader("X-Request-Id"))
