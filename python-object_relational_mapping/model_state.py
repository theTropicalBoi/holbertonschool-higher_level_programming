#!/usr/bin/python3
"""
Contains the class definition of a state and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Instance of Base
Base = declarative_base()


# Class State with base as inheritance
class State(Base):
    """
    State Class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
