#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    row = c.fetchall()
    for states in row:
        print(states)
    c.close()
    db.close()
