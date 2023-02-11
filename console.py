#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, line):
        """quit command to exit"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Empty line and enter shouldnt execute the last program
        """
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
