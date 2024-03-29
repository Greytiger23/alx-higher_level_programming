#!/usr/bin/python3
"""module that class definition of a State and an instance
   Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

m = MetaData()
Base = declarative_base(metadata=m)


class State(Base):
    """represents the class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
