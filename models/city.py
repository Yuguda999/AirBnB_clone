#!/usr/bin/python3
"""
Defines the City class for the HBNB project, extending BaseModel.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city with a relationship to a state.
    Attributes:
	state_id (str): The ID pf the state the city belongs to.
	name (str): The name of the city.
"""

state_id = ""
name = ""
