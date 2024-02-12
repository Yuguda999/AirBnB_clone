#!/usr/bin/python3
"""
This script tests the functionality of the BaseModel class.
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID
import json
import os

class TestBaseModel(unittest.TestCase):
    """
    Defines test cases for the BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test case with BaseModel as the subject.
        """
        super().__init__(*args, **kwargs)
        self.model_name = 'BaseModel'
        self.model_class = BaseModel

    def setUp(self):
        """
        Setup actions before each test method.
        """
        pass

    def tearDown(self):
        """
        Cleanup actions after each test method.
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """
        Tests the creation of a BaseModel instance and its type.
        """
        instance = self.model_class()
        self.assertEqual(type(instance), self.model_class)

    def test_instance_from_dict(self):
        """
        Tests instantiation of BaseModel from a dictionary.
        """
        instance = self.model_class()
        instance_dict = instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertNotEqual(new_instance, instance)

    def test_unexpected_kwargs(self):
        """
        Tests instantiation with unexpected keyword arguments.
        """
        instance = self.model_class()
        instance_dict = instance.to_dict()
        instance_dict.update({'unexpected': 42})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**instance_dict)

    def test_save_method(self):
        """
        Tests the save method of BaseModel.
        """
        instance = self.model_class()
        instance.save()
        with open('file.json', 'r') as file:
            data = json.load(file)
            key = f"{self.model_name}.{instance.id}"
            self.assertIn(key, data)

    def test_string_representation(self):
        """
        Tests the string representation of a BaseModel instance.
        """
        instance = self.model_class()
        expected_format = f'[{self.model_name}] ({instance.id}) {instance.__dict__}'
        self.assertEqual(str(instance), expected_format)

    def test_to_dict_method(self):
        """
        Tests conversion of BaseModel instance to dictionary.
        """
        instance = self.model_class()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict, instance.to_dict())

    def test_instantiation_with_None(self):
        """
        Tests instantiation of BaseModel with None as a keyword argument.
        """
        with self.assertRaises(TypeError):
            new_instance = self.model_class(**{None: None})

    def test_id_attribute(self):
        """
        Tests the id attribute of BaseModel.
        """
        instance = self.model_class()
        self.assertIsInstance(instance.id, str)

    def test_created_at_attribute(self):
        """
        Tests the created_at attribute of BaseModel.
        """
        instance = self.model_class()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_attribute(self):
        """
        Tests the updated_at attribute of BaseModel.
        """
        instance = self.model_class()
        self.assertIsInstance(instance.updated_at, datetime)
        instance_dict = instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertNotEqual(new_instance.created_at, new_instance.updated_at)
