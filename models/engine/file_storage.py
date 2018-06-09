#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    """
    serializes instances to a JSON & deserializes JSON to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """print the current __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """turn python objects into a specific dict format in __objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """take __objects and convert to JSON in a file"""
        new_dict = {}
        print("haah {}".format(self.__objects))
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
            print("newdict = {}".format(new_dict))
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """take json file and convert back to dictionary"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                current = json.load(f)
                for k, v in current.items():
                        __objects[k] = eval("BaseModel"(**v))
        except:
            print("IN the except")
            pass
