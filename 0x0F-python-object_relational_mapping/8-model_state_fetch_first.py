#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_states(username, password, database):
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(username,
                           password, database))
    ses = sessionmaker(bind=engine)
    s = ses()
    f = s.query(State).order_by(State.id).first()
    if f:
        print("{}: {}".format(f.id, f.name))
    else:
        print("Nothing")
    s.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        print_states(username, password, database)
