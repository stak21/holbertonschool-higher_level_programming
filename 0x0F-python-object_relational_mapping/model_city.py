#!/usr/bin/python3.4
""" Class: cities - Base Model of a City """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base


Base = declarative_base()


class City(Base):
    """ Class: A Class to map to a table """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('cities.id'), nullable=False)

    state = relationship("State", backref="cities")
