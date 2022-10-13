#!/usr/bin/python3
'''This is a module'''

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           username, password, db))

    Session = sessionmaker(bind=engine)
    session = Session()
    all_state = session.query(State).join(City).order_by(State.id,
                                                         City.id).all()

    for state in all_state:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'\t{city.id}: {city.name}')

    session.close()
