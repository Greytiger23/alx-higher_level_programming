#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def list_cos(username, password, database, state_name):
    a = MySQLdb.connect(host="localhost", port=3306, user=username,
                        passwd=password, db=database)
    b = a.cursor()
    b.execute("""SELECT cities.name FROM cities
              INNER JOIN states ON states.id=cities.state_id
              WHERE states.name=%s""", (state_name,))
    c = b.fetchall()
    d = list(row[0] for row in c)
    print(*d, sep=", ")
    b.close()
    a.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        list_cos(username, password, database, state_name)
