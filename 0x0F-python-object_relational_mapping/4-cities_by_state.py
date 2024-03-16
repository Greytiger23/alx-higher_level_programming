#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    a = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3])
    b = a.cursor()
    b.execute("""SELECT * FROM cities""")
    c = b.fetchall()
    for row in c:
        print(row)
    b.close()
    a.close()
