#!/usr/bin/python3

"""
Lists all states objects
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

arg = sys.argv[1:]

engine = create_engine(
    f"mysql+mysqldb://{arg[0]}:{arg[1]}@localhost:3306/{arg[2]}", 
    pool_pre_ping=True)


Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()

for state in states:
    print(f"{state.id}: {state.name}")
