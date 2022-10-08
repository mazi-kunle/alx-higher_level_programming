#!/usr/bin/python3
'''
This is a module
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    '''
    A state table.
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
