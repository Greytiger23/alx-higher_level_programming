#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def print_city(username, password, database):
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(username,
                           password, database))
    ses = sessionmaker(bind=engine)
    s = ses()
    a = s.query(City).order_by(City.id).all()
    for city in a:
        b = s.query(State).filter_by(id=city.state_id).first().name
        print("{}: ({}) {}".format(b, city.id, city.name))
    s.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        print_city(username, password, database)
