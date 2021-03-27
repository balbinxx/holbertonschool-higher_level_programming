#!/usr/bin/python3
"""
Script that takes in the name of a state
as an argument and lists all cities of that state 
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name, FROM cities \
                INNER JOIN states ON \
                states.id=cities.states_id \
                WHERE states.name LIKE BINARY %s \
                ORDER BY cities.id", (argv[4], ))
    row = c.fetchall()
    print(", ".join(req[0] for req in row))
    c.close()
    db.close()
