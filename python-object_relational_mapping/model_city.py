#!/usr/bin/python3
"""
City class definition, linked to the `cities` table in the database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that inherits from Base
    Links to the MySQL table cities
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Establish a relationship with the State class
    state = relationship("State", backref="cities")
