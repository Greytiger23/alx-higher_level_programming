#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    """represents the class"""
    a = MySQLdb.connect(host="localhost", port=3306, user=username,
        passwd=password, db=database)
    b = a.cursor()
    b.execute("SELECT * FROM states ORDER BY id ASC")
    c = b.fetchall()
    for row in c:
        print(row)
    b.close()
    a.close()

if __name__ == "__main__":
    if len(sys.agv) != 4:
        print("Usage: python 0-select_states.sql <username>
        <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
