#!/usr/bin/python3
"""
Unittest for base_model
"""
import unittest
import sys
from io import StringIO
from models.base_model import BaseModel
import pep8

class Test_BaseModel(unittest.TestCase):
    """
    Test class BaseModel
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_task0(self):
        my_model = BaseModel()
        new_model = BaseModel()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(type(my_model).__name__, "BaseModel")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "pep8")

    def setUp(self):
        """
        redirect stdout of the output for functions using print
        """
        sys.stdout = StringIO

    def tearDown(self):
        """
        re-establish the stdout back to normal after setUp
        """
        sys.stdout = sys.__stdout__
