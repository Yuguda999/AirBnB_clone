#!/usr/bin/python3
"""
Module defining the User class for the HBNB project, inheriting from BaseModel.
This class encapsulates user-related data, including authentication and personal information.
"""


from models.base_model import BaseModel


class User (BaseModel):
    """
    Represents a user in the application with attributes for identification and personal details.


    Attributes:
	email (str): Email address of the user.
	password (str): Password for authentication.
	first_name (str): User's first name.
	last_name (str): User's last name.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
