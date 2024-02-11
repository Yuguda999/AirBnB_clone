#!/usr/bin/env python3
"""
This module defines a BaseModel class to serve as a foundation for all models in our hbnb clone.
"""

from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage_type

Base = declarative_base()

class BaseModel:
    """
    A base class for all hbnb models providing common attributes and methods.

    Attributes:
        id (String): Unique identifier for the model.
        created_at (DateTime): Timestamp of model creation.
        updated_at (DateTime): Timestamp of the last model update.
    """
    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, **kwargs):
        """Initializes a new model instance, optionally with properties from kwargs."""
        self.id = kwargs.get('id', str(uuid4()))
        self.created_at = self._parse_datetime(kwargs.get('created_at', datetime.utcnow()))
        self.updated_at = self._parse_datetime(kwargs.get('updated_at', datetime.utcnow()))
        for key, value in kwargs.items():
            if key not in ['id', 'created_at', 'updated_at', '__class__']:
                setattr(self, key, value)

    def __str__(self):
        """Returns the string representation of the model instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the model's last update timestamp and saves it to storage."""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Converts the model instance into a dictionary format."""
        model_dict = {**self.__dict__, "__class__": self.__class__.__name__}
        for key, value in model_dict.items():
            if isinstance(value, datetime):
                model_dict[key] = value.isoformat()
        model_dict.pop('_sa_instance_state', None)
        return model_dict

    def delete(self):
        """Deletes the current instance from storage."""
        from models import storage
        storage.delete(self)

    @staticmethod
    def _parse_datetime(value):
        """Parses a datetime object from a string or returns the current datetime if none."""
        if isinstance(value, datetime):
            return value
        try:
            return datetime.fromisoformat(value)
        except TypeError:
            return datetime.utcnow()
