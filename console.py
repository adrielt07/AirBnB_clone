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
        print("", end="")

    def do_create(self, *arg):
        try:
            func = "models.{}".format(arg[0])
            model = eval(func)()
            model.save()
            print(model.id)
        except AttributeError:
            print("** class doesn't exist **")
        except SyntaxError:
            print("** class name missing **")

    def do_show(self, *arg):
        try:
        except AttributeError:
            print("** class doesn't exist **")
        except SyntaxError:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
