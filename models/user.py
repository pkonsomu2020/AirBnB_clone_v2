#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    places = relationship("Place", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
