#!/usr/bin/python3

"""
Prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
import sys

if __name__ == "__main__":

    arg = sys.argv[1:]

    engine = create_engine(
        f"mysql+mysqldb://{arg[0]}:{arg[1]}@localhost:3306/{arg[2]}",
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(
        State).order_by(City.id.asc()).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
