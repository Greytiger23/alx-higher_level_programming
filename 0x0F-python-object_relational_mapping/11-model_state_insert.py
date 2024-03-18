#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_add(username, password, database):
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(username,
                           password, database))
    ses = sessionmaker(bind=engine)
    s = ses()
    new = State(name="Louisiana")
    s.add(new)
    s.commit()
    print(new.id)
    s.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        print_add(username, password, database)
