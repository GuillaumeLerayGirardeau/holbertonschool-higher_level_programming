#!/usr/bin/python3

"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    existing_state = session.query(State).filter_by(name="Louisiana").first()

    if not existing_state:
        new_state = State(name = "Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)
