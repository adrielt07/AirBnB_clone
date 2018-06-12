#!/usr/bin/python3
"""File Storage Test"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import pep8
import os
import json


class Test_FileStorage(unittest.TestCase):
    """
    Test Class FileStorage
    """
    def test_docstring(self):
        """check that docstring exist"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def setUp(self):
        """set up"""
        pass

    def tearDown(self):
        """tear down"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        """Method for all"""
        f0 = FileStorage()
        f_in_objects = f0.all()
        self.assertTrue(type(f_in_objects), dict)
#        self.assertTrue(, FileStorage.__objects)

    def test_new(self):
        """Test method for new"""
        f1 = FileStorage()

            
    def test_save_method(self):
        """Test save method"""
        f2 = FileStorage()
        b1 = BaseModel()

        f2.new(b1)
        b1.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", encoding="utf-8") as f:
            n = json.load(f)
            self.assertEqual(type(n), dict)
            for k, v in n.items():
                d = BaseModel(**v)
                for k, v in b1.__dict__.items():
                    self.assertTrue(k in d.__dict__)
#                    if k is 'created_at' or 'updated_at':
#                        self.assertNotEqual(d.__dict__['updated_at'], b1.__dict__['updated_at'])

    def test_reload(self):
        """Test reload method"""
        f3 = FileStorage()
#        try:
#            os.remove("file.json")
#        except:
#            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_json(self):
        """Raise errors related to JSON conversion"""
        with self.assertRaises(AttributeError):
            FileStorage.__objects
            FileStorage.__File_Path
