#!/usr/bin/python3
"""
Unit test for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class.
    """

    def test_init(self):
        """Test initialization of BaseModel instance."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.updated_at, datetime))

    def test_str(self):
        """Test the __str__ method."""
        instance = BaseModel()
        expected = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected)

    def test_save(self):
        """Test the save method."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
