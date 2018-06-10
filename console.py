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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
