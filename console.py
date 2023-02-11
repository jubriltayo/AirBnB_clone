#!/usr/bin/python3
"""Module for command interpretation"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""
    prompt = "(hbnb) "
    __classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """end of file signal to exit program
        """
        return True

    def emptyline(self):
        """empty line no longer execute last command"""
        pass

    def do_create(self, arg):
        """creates an instance of BaseModel, saves it
            to JSON file and prints the id
        """
        args = arg.split()
        
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(f"{args[0]}")()
            print(new_object.id)
        storage.save()

    def do_show(self, arg):
        """prints string representation of an instance based
            on class name and id
        """
        args = arg.split()

        object_id = f"{args[0]}.{args[1]}"
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2: 
            print("** instance id missing **")
        elif object_id not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[object_id])
            
    def do_destroy(self, arg):
        """Deletes an instance based on class name and id
            and saves the changes into JSON file
        """
        args = arg.split()

        object_id = f"{args[0]}.{args[1]}"
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2: 
            print("** instance id missing **")
        elif object_id not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[object_id]
        storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances
            based or not on the class name
        """
        args = arg.split()

        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if k.startswith(args[0])])
    
    def do_update(self, arg):
        """Updates an instance based on class name and id by adding
            or updating attribute
        """
        args = arg.split()

        object_id = f"{args[0]}.{args[1]}"
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2: 
            print("** instance id missing **")
        elif object_id not in storage.all():
            print("** no instance found **")
        elif len(args) < 3: 
            print("** attribute name missing **")
        elif len(args) < 4: 
            print("** value missing **")      

if __name__ == '__main__':
    HBNBCommand().cmdloop()
