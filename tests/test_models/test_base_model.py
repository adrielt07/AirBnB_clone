#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    def test_docstring(self):
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_init(self):
        my_model = BaseModel()
        test_dict = my_model.to_dict()
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
