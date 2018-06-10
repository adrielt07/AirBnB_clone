#!/usr/bin/python3
from models.engine import file_storage
from models.base_model import BaseModel

storage = file_storage.FileStorage()
storage.reload()

if __name__ != '__main__':
    def error_check(list_arg=[]):
        try:
            class_name = "{}".format(list_arg[0])
            eval(class_name)()
        except IndexError:
            print("** class name missing **")
            return 0
        except NameError:
            print("** class doesn't exist **")
            return 0

        try:
            key = "{}.{}".format(list_arg[0], list_arg[1])
            return key
        except IndexError:
            print("** instance id missing **")
            return 0
