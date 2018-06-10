#!/usr/bin/python3
"""
Entry point to command interpreter
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the AirBnB shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Receives End Of File signal and exits out of program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, args):
        """Create a new instance of a class"""
        args = "".join(args).split()
        #check that there isn't more than one arg
        if len(args) == 1:
            error = models.error_check(args, 1)
            if error != 0:
                model = eval("models.{}".format(args[0]))()
                model.save()
                print(model.id)
        else:
            print("** class name missing **")

    def do_show(self, args):
        """Print the instance's class name and ID"""
        args = "".join(args).split()
        key = models.error_check(args)
        if key == 0:
            return
        try:
            obj_dict = models.storage.all()
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an existing instance"""
        args = "".join(args).split()
        key = models.error_check(args)
        if key == 0:
            return
        try:
            obj_dict = models.storage.all()
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Print instances: can print class-specific"""
        args = "".join(args).split()
        obj_dict = models.storage.all()
        #all w/o class name
        if len(args) == 0:
            for obj_id in obj_dict.keys():
                obj = obj_dict[obj_id]
                print(obj)
        #all w/class name
        else:
            try:
                eval("models.{}".format(args[0]))()
            except AttributeError:
                print("** class doesn't exist **")
                return
            else:
                for k, v in obj_dict.items():
                    if v.to_dict()['__class__'] == args[0]:
                        obj = obj_dict[k]
                        print(obj)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
