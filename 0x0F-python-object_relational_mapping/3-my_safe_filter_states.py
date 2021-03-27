#!/usr/bin/python3
"""
Displays the arg when matches, but safe from Sql injections 
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = %s", (argv[4]))
    row = c.fetchall()
    for states in row:
        print(states)
    c.close()
    db.close()
