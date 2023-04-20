#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    places = relationship("Place", cascade="all, delete-orphan", back_populates="cities")

    def __repr__(self):
        return f"City(id={self.id}, name='{self.name}')"
