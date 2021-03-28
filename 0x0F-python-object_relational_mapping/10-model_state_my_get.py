#!/usr/bin/python3
"""
Random words bla
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    arg_state = session.query(State).filter(State.name == argv[4]).first()
    if arg_state is None:
        print("Not found")
    else:
        print("{}".format(arg_state.id))
    session.close()
