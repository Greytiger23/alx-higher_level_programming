#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    a = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3])
    b = a.cursor()
    b.execute("SELECT * FROM states")
    c = b.fetchall()
    for row in c:
        print(row)
    b.close()
    a.close()
