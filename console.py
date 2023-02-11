#!/usr/bin/python3
"""Module for command interpretation"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """end of file command to exit program
        """
        return True

    def emptyline(self):
        """empty line no longer print last command"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
