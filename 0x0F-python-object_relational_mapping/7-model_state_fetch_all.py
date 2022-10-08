#!/usr/bin/python3
'''
This is a module
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


username = argv[1]
password = argv[2]
database = argv[3]

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                       password, database))

Session = sessionmaker(bind=engine)
session = Session()


states = session.query(State).order_by(State.id).all()
for state in states:
    print(f'{state.id}: {state.name}')

session.close()
