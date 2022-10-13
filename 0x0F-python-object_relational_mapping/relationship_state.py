#!/usr/bin/python3
'''
This is a module
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship, backref


Base = declarative_base()


class State(Base):
    '''
    A state table.
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')

    def __init__(self, name):
        self.name = name
