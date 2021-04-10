#!/usr/bin/python3
"""
fetches URL
"""

from urllib.error import HTTPError
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    r = Request(argv[1])
    try:
        with urlopen(r) as x:
            print(x.read().decode('utf-8'))
    except HTTPError as y:
        print('Error code: {}'.format(y.code))
