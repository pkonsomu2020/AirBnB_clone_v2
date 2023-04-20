#!/usr/bin/python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))

        amenities = relationship('Amenity', secondary='place_amenity',
                                  back_populates='place_amenities', viewonly=False)
    else:
        @property
        def amenities(self):
            """
            Getter attribute amenities that returns the list of Amenity
            instances based on the attribute amenity_ids
            """
            from models import storage
            from models.amenity import Amenity

            amenity_objs = []
            for amenity_id in self.amenity_ids:
                amenity_obj = storage.get(Amenity, amenity_id)
                if amenity_obj is not None:
                    amenity_objs.append(amenity_obj)
            return amenity_objs

        @amenities.setter
        def amenities(self, obj):
            """
            Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_ids
            """
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
            else:
                pass

