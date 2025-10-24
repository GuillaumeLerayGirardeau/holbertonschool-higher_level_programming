#!/usr/bin/python3

"""
python file that contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    Class that represents the table cities
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(
        "states.id", ondelete="CASCADE"), nullable=False)

    state = relationship("State", back_populates="cities")
