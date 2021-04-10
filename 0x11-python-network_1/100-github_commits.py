#!/usr/bin/python3
"""
ADV
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(argv[2], argv[1])
    rp = requests.get(url)
    x = 0
    for c in rp.json():
        if x < 10:
            print("{}: {}".format(c.get("sha"),
                  c.get("commit").get("author").get("name")))
        x += 1
