#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def list_cos(username, password, database, state_name):
    a = MySQLdb.connect(host="localhost", port=3306, user=username,
                        passwd=password, db=database)
    b = a.cursor()
    query = """SELECT cities.name FROM cities
              JOIN states ON states.id = cities.states_id
              WHERE states.name = %s ORDER BY cities.id"""
    b.execute(query, (state_name,))
    c = b.fetchall()
    for row in c:
        print(row)
    b.close()
    a.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        list_cos(username, password, database, state_name)
