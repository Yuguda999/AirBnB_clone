#!/usr/bin/python3
"""
Module that defines the FileStorage class for the HBNB clone project.
This class handles the serialization and deserialization of the model instances to and from JSON format.
"""

import json

class FileStorage:
    """
    Manages the storage of all models in the HBNB clone project using JSON serialization.
    """
    __file_path = 'file.json'  # Path to the JSON file for storing instances
    __objects = {}  # Dictionary to store all objects by <class name>.id

    def all(self):
        """
        Returns the dictionary of all objects currently in storage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the storage dictionary to the JSON file (__file_path).
        """
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists; otherwise, does nothing).
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
                from models import classes  # Importing all class definitions
                for obj_id, obj_dict in objs.items():
                    self.__objects[obj_id] = classes[obj_dict['__class__']](**obj_dict)
        except FileNotFoundError:
            pass
