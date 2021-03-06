#!/usr/bin/python3
"""
Entry for HBNBCommand class.
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command Interpreter.
    """
    prompt = "(hbnb) "
    allowed_modules = ["BaseModel", "User", "State", "City",
                       "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """
        Quit command.
        """
        return True

    def do_EOF(self, line):
        """
        Handling the End of File Char.
        """
        print()
        return True

    def emptyline(self):
        """
        FIX 4 Empty line + Enter which shouldn't do anything.
        """
        pass

    def do_create(self, line):
        """
        Creating a new instance of BaseModel, then
        saves it into a JSON File and print it's id.

        - 'Split' tokenizes he line to verify the existence
            of the module 'args[0]' and ignore other args if
            theres any
        """
        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
            else:
                if args[0] == self.allowed_modules[0]:
                    instance = BaseModel()
                elif args[0] == self.allowed_modules[1]:
                    instance = User()
                elif args[0] == self.allowed_modules[2]:
                    instance = State()
                elif args[0] == self.allowed_modules[3]:
                    instance = City()
                elif args[0] == self.allowed_modules[4]:
                    instance = Amenity()
                elif args[0] == self.allowed_modules[5]:
                    instance = Place()
                elif args[0] == self.allowed_modules[6]:
                    instance = Review()
                instance.save()
                print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints a string representation of an instance
        which is based on the class name and id.
        """
        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
        else:
            print("** class name missing **")
            return

        objs = FileStorage().all()
        if args[0]+"."+args[1] in objs:
            print(objs[args[0] + "." + args[1]])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes and instance which is based or not
        in the class name.
        """
        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
        else:
            print("** class name missing **")
            return

        objs = FileStorage().all()
        if args[0]+"."+args[1] in objs:
            del(objs[args[0] + "." + args[1]])
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances.
        """
        objs = FileStorage().all()

        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
                return

            fill_list1 = []
            for k, v in objs.items():
                if args[0] in k:
                    fill_list1.append(str(v))
            print(fill_list1)

        else:
            fill_list2 = []
            for v in objs.values():
                fill_list2.append(str(v))
            print(fill_list2)

    def do_update(self, line):
        """
        Updates an instance based on the class
        and id by adding or updating attributes.
        Then save the changes into the JSON File.
        """
        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return

            objs = FileStorage().all()
            instance = args[0] + "." + args[1]
            if instance in objs:

                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                if len(args) < 4:
                    print("** value missing **")
                    return

                if '"' in args[3]:
                    modification = args[3].replace('"', '')
                    the_object = objs[args[0] + "." + args[1]]
                    attribute = args[2]
                    value = modification

                    setattr(the_object, attribute, value)
                    objs[instance].save()
            else:
                print("** no instance found **")
        else:
            print('** class name missing **')
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
