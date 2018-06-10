#!/usr/bin/python3
"""
Executes storage when module is called
"""
from models.engine import file_storage
from models.base_model import BaseModel

storage = file_storage.FileStorage()
storage.reload()

if __name__ != '__main__':
    def error_check(list_arg=[], n=0):
        """Check for common error messages for all methods"""
        try:
            class_name = "{}".format(list_arg[0])
            eval(class_name)()
        except IndexError:
            if len(list_arg) == 0:
                print("** class name missing **")
                return 0
        except NameError:
            print("** class doesn't exist **")
            return 0

        if n == 0:
            try:
                key = "{}.{}".format(list_arg[0], list_arg[1])
                return key
            except IndexError:
                if len(list_arg) == 1:
                    print("** instance id missing **")
                    return 0
