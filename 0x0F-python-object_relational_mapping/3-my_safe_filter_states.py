#!/usr/bin/python3
"""script that takes in arguments and displays all values in
   the states table of hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    a = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3])
    b = a.cursor()
    x = sys.argv[4]
    b.execute("SELECT * FROM states WHERE name LIKE %s", (x, ))
    c = b.fetchall()
    for row in c:
        print(row)
    b.close()
    a.close()
