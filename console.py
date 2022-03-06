#!/usr/bin/python3
""""""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = "(hbnb) "
    allowed_modules = ["BaseModel", "User", "State", "City",
                        "Amenity", "Place", "Review"]

    def do_quit(self, line):
        """"""
        return True

    def do_EOF(self, line):
        """"""
        print()
        return True

    def emptyline(self):
        """"""
        pass
    def do_create(self, line):
        """"""
        if line:
            args = line.split(' ')

            if args[0] not in self.allowed_modules:
                print("** class doesn't exixt **")
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
        """"""
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
        """"""
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
        """"""
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
        """"""
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
