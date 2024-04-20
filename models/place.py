#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    city_id = "00400"
    user_id = "40163748"
    name = "Nairobi"
    description = ""
    number_rooms = 1
    number_bathrooms = 1
    max_guest = 2
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
