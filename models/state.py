#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from . import storage_type
from models.city import City


class State(BaseModel, Base):
    __tablename__ = 'states'
    if storage_type == 'db':
    	  name = Column(String(128), nullable=False)
    	  cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ''

    @property
    def cities(self):
            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
