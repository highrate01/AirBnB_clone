#!/usr/bin/python3
"""
This module defines command line intepreter
"""
from models.user import User
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    displays prompt
    """
    prompt = "(hbnb)"
    allowed_classes = ["BaseModel", "User"]

    def do_create(self, arg):
        """
        creates a new instance of Basemodel, saves it and
        print the id
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{args[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        print the string representation of an instance
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(args[0], args[1])

            if key in objects:
                del (objects[key])
                storage.save()

            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        prints all string representation of instances
        """
        objects = storage.all()

        args = shlex.split(arg)

        if len(args) == 0:
            for key, value in objects.items():
                print(str(value))
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == args[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        update an instance  based on the class name and id
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")

            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = args[2]
                attr_value = args[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_quit(self, arg):
        """
        Defines quit command
        """
        return True

    def help_quit(self, arg):
        """
        define help command
        """
        print("Type Quit to exit")

    def do_EOF(self, arg):
        """
        Defines end of file command
        """
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
