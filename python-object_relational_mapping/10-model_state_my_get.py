#!/usr/bin/python3

"""
Prints the State object with the name passed as argument
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":

    arg = sys.argv[1:]

    engine = create_engine(
        f"mysql+mysqldb://{arg[0]}:{arg[1]}@localhost:3306/{arg[2]}",
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id).where(
        State.name == arg[3]).order_by(State.id.asc()).all()

    if state:
        print(state[0][0])
    else:
        print("Not found")
