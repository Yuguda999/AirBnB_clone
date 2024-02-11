#!/usr/bin/python3
"""
Module defining the State class for the HBNB project, extending BaseModel.
This class serves as the representation of a geographical state within the application.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    Defines the State class, representing a state in the application.
    
    Attributes:
        name (str): The name of the state.
    """
    name = ""
