#!/usr/bin/python3
"""

Defines the Review class for the HBNB project, inheriting from BaseModel.This module provides the Review class used to represent guest reviews for places.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for a Place in the HBNB project.


    Attributes:
	place_id (str): The ID of the Place being reviewed.
	user_id (str): The ID of the User who wrote the review.
	text (str): The text content of the review.
   """
    place_id = ""
    user_id = ""
    text = ""
