#!/usr/bin/python3
"""
Uses the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    rp = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(rp.json().get('id'))
