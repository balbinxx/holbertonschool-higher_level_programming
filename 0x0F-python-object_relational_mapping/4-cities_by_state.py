#!/usr/bin/python3
"""
Lists all cities from the database
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """)
    row = c.fetchall()
    for city in row:
        print(city)
    c.close()
    db.close()
