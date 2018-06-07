#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()
        self.assertEqual(my_model.__class__, "BaseModel")
