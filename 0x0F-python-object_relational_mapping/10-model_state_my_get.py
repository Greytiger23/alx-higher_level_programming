#!/usr/bin/python3
"""prints the State object with the name passed as argument
   from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_name(username, password, database, state_name):
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(username,
                           password, database))
    ses = sessionmaker(bind=engine)
    s = ses()
    a = s.query(State).filter(State.name == state_name).first()
    if a:
        print(a.id)
    else:
        print("Not found")
    s.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        print_name(username, password, database, state_name)
