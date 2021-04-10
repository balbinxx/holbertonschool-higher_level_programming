#!/usr/bin/python3
"""
Random BLS
"""
import requests
from sys import argv


if __name__ == "__main__":
    val = {'q': ""}
    if len(argv) == 2:
        val['q'] = argv[1]

    rp = requests.post('http://0.0.0.0:5000/search_user', data=val)
    try:
        if not rp.json():
            print("No result")
        else:
            print("[{}] {}".format(rp.json().get('id'), rp.json().get('name')))
    except ValueError:
        print('Not a valid JSON')
