#!/usr/bin/python3
"""
Module for the command line interface for the HBNB clone project.
"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Implements the command interpreter for the HBNB clone."""

    # Setting the command prompt
    prompt = '(hbnb) ' if sys.stdin.isatty() else ''

    # Dictionary of valid classes
    valid_classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    # List of commands that support dot notation
    supported_dot_commands = ['all', 'count', 'show', 'destroy', 'update']

    # Mapping of attribute names to their types for casting
    attribute_types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints the prompt if in non-interactive mode."""
        if not sys.stdin.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Parses the input line to support dot command syntax."""
        try:
            if '.' in line and '(' in line and ')' in line:
                cls_name, method_part = line.split('.', 1)
                method_name, arg_str = method_part.split('(', 1)
                arg_str = arg_str[:-1]  # Remove trailing ')'

                if method_name in self.supported_dot_commands:
                    line = method_name + ' ' + cls_name + ' ' + arg_str.replace('\"', '').replace(',', '')
        except Exception:
            pass
        return line

    def postcmd(self, stop, line):
        """Prints the prompt if in non-interactive mode."""
        if not sys.stdin.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, arg):
        """Exits the console."""
        exit()

    def help_quit(self):
        """Displays the help for the quit command."""
        print("Exit the HBNB console\n")

    def do_EOF(self, arg):
        """Exits the console on EOF."""
        print()
        exit()

    def help_EOF(self):
        """Displays the help for the EOF command."""
        print("Exit the HBNB console\n")

    def emptyline(self):
        """Overrides the default behavior to do nothing on an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_obj = self.valid_classes[arg]()
            new_obj.save()
            print(new_obj.id)
        except KeyError:
            print("** class doesn't exist **")

    def help_create(self):
        """Displays the help for the create command."""
        print("Create a new instance of a class.\nUsage: create <class name>\n")

    def do_show(self, arg):
        """Shows an instance of a class by id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        obj_key = f"{args[0]}.{args[1]}"
        if obj_key in obj_dict:
            print(obj_dict[obj_key])
        else:
            print("** no instance found **")

    def help_show(self):
        """Displays the help for the show command."""
        print("Show an instance of a class by id.\nUsage: show <class name> <id>\n")

    def do_destroy(self, arg):
        """Deletes an instance of a class by id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_key = f"{args[0]}.{args[1]}"
        if obj_key in storage.all():
            del storage.all()[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def help_destroy(self):
        """Displays the help for the destroy command."""
        print("Deletes an instance of a class by id.\nUsage: destroy <class name> <id>\n")

    def do_all(self, arg):
        """Displays all instances of a class."""
        if arg and arg not in self.valid_classes:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in storage.all().values():
            if not arg or obj.__class__.__name__ == arg:
                obj_list.append(str(obj))
        print(obj_list)

    def help_all(self):
        """Displays the help for the all command."""
        print("Displays all instances of a class.\nUsage: all <class name>\n")

    def do_count(self, arg):
        """Counts the number of instances of a class."""
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == arg:
                count += 1
        print(count)

    def help_count(self):
        """Displays the help for the count command."""
        print("Counts the number of instances of a class.\nUsage:
		count <class name>\n")

    def do_update(self, arg):
        """Updates an instance of a class by adding or updating attributes."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_key = f"{args[0]}.{args[1]}"
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = storage.all()[obj_key]
        setattr(obj, args[2], args[3].strip("\""))
        obj.save()

    def help_update(self):
        """Displays the help for the update command."""
        print("Updates an instance of a class.\nUsage:
		update <class name> <id> <attribute name> \"<attribute value>\"\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
