#!/usr/bin/python3

"""
This module contains a python class and an instance of the
declarative_base class
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """
    This class inherits from the Base class and serves as a helper for
    creation, insertion and deletion from the States table
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
