#!/usr/bin/python3
"""
Module for the Place class in the HBNB project.
Defines the Place class that inherits from BaseModel.
"""


from models.base_model import BaseModel

class Place(BaseModel):
    """
    Defines the Place class representing a lodging option in the HBNB project.


    Attributes:
	city_id (str): The ID of the city where the place is located.
	user_id (str): The ID of the User object who is the place.
