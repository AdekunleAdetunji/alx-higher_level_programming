#!/usr/bin/python3

"""
This module is a python file that contains class definition for city
defined in a manner similar to how the state class is defined in state.py
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


class City(Base):
    """
    This class defines the table structure for a city in mysql database
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
