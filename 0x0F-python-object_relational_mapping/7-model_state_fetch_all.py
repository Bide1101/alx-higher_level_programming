#!/usr/bin/python3
'''
This list all states of a givien database
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    '''
    This gets the states from the database
    '''
    database_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    database_engine = create_engine(database_uri)
    Session = sessionmaker(bind=database_engine)

    session = Session()

    for r in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
