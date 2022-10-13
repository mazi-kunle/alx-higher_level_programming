#!/usr/bin/python3
'''
This is a module.
'''

from sqlalchemy import Column, String, Integer, ForeignKeyConstraint
from relationship_state import Base


class City(Base):
    '''
    A city table
    '''
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(['state_id'], ['states.id']),
    )
