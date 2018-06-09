#!/usr/bin/python3
"""
Entry point to command interpreter
"""
import cmd
class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the AirBnB shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Exits out of program"""
        return True

    def do_EOF(self, args):
        """Receives End Of File signal and exits out of program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
