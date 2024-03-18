#!/usr/bin/python3
""" deletes all State objects with a name containing the
    letter a from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_del(username, password, database):
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(username,
                           password, database))
    ses = sessionmaker(bind=engine)
    s = ses()
    a = s.query(State).filter(State.name.like('%a%')).all()
    for state in a:
        s.delete(state)
    s.commit()
    s.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        print_del(username, password, database)
