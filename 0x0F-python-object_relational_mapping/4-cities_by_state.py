#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host = 'localhost', user = sys.argv[1], password = sys.argv[2], db = sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM cities ORDER BY cities.id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()