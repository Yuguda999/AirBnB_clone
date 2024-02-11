#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os

class TestBaseModel(unittest.TestCase):
    """Defines the test suite for the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Class-level setup that runs once before all tests."""
        cls.name = 'BaseModel'
        cls.value = BaseModel

    def setUp(self):
        """Prepare resources for each test."""
        pass

    def tearDown(self):
        """Clean up resources after each test."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test BaseModel initialization."""
        instance = self.value()
        self.assertIsInstance(instance, BaseModel)

    def test_default_attributes(self):
        """Test default attributes are correctly set."""
        instance = self.value()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_kwargs_initialization(self):
        """Test initialization with keyword arguments."""
        instance = self.value(name="test", number=42)
        self.assertEqual(instance.name, "test")
        self.assertEqual(instance.number, 42)

    def test_save(self):
        """Test the save method and file storage."""
        instance = self.value()
        instance.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        instance = self.value()
        expected = '[BaseModel] ({}) {}'.format(instance.id, instance.__dict__)
        self.assertEqual(str(instance), expected)

    def test_to_dict(self):
        """Test conversion of instance attributes to dictionary for JSON."""
        instance = self.value()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_unique_id(self):
        """Test that each instance has a unique id."""
        instance_a = self.value()
        instance_b = self.value()
        self.assertNotEqual(instance_a.id, instance_b.id)

    def test_datetime_attributes(self):
        """Test the type of datetime attributes."""
        instance = self.value()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_updated_at_changes_on_save(self):
        """Test updated_at is modified upon calling save."""
        instance = self.value()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_attribute_addition(self):
        """Test that new attributes can be added to an instance."""
        instance = self.value()
        instance.custom_attribute = "custom_value"
        self.assertEqual(instance.custom_attribute, "custom_value")

    def test_kwargs_handling_invalid(self):
        """Test handling of invalid kwargs."""
        with self.assertRaises(TypeError):
            self.value(**{"__class__": "should_not_change"})

if __name__ == '__main__':
    unittest.main()
