#!/usr/bin/python3
"""
Random s***
"""

import requests

if __name__ == "__main__":
    rp = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(rp.text), rp.text))
