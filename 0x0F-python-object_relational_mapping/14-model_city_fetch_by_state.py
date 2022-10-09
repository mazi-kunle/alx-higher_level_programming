#!/usr/bin/python3
'''This is a module'''

from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            username, password, db))

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).join(State)
    for i in query:
        print(f'{i[1].name}: ({i[0].id}) {i[0].name}')

    session.close()
