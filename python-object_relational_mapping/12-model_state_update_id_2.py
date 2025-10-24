#!/usr/bin/python3

"""
Changes the name of a State object from the database hbtn_0e_6_usa
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

    state_2 = session.query(State).filter_by(id=2).first()

    if state_2:
        state_2.name = "New Mexico"
        session.commit()
