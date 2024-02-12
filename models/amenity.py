#!/usr/bin/python3
"""
Defines the Amenity for the HBNB project, extending BaseModel.
This module provides the Amenity class used to represent the amenities offered by a Place.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity in the HBNB project.


    Attributes:
	name (str): The name of the amenity.
    """
    name = ""
