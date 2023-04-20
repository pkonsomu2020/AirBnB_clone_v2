#!/usr/bin/python3

from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True))


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity, backref="amenities")
