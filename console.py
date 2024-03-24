#!/usr/bin/python3
"""
This module defines command line intepreter
"""
from models.city import City
from models.user import User
import cmd
from models.base_model import BaseModel
from models import storage
from models.review import Review
from models.place import Place
from models.state import State
from models.amenity import Amenity
import shlex
import re
import ast


def split_curl(extra_args):
    """
    split curly braces for the update method
    """
    curl_brace = re.search(r"\{(.*?)\}", extra_args)
    if curl_brace:
        comma_parts = shlex.split(extra_args[:curl_brace.span()[0]])
        id_ = comma_parts[0].replace(",", "").strip()
        str_data = curl_brace.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("** invalid dictionary format **")
            return
        return id_, arg_dict
    else:
        try:
            args = extra_args.split(",")
            id_ = args[0].strip()
            attr_name = args[1].strip()
            attr_value = args[2].strip()
            return f"{id_}", f"{attr_name} {attr_value}"
        except Exception:
            print("** argument missing **")
class HBNBCommand(cmd.Cmd):
    """
    displays prompt
    """
    prompt = "(hbnb) "
    allowed_classes = ["BaseModel", "User", "Place", "State",
                       "City", "Amenity", "Review"]
    last_command = False

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

    def default(self, arg):
        """
        handle invalid syntax
        """
        arg_list = arg.split('.')
        input_class_name = arg_list[0]

        args = arg_list[1].split('(')
        input_method = args[0]
        extra_args = args[1].split(')')[0]

        dict_method = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }
        if input_method in dict_method.keys():
            if input_method != "update":
                return dict_method[input_method]("{} {}".format(
                                                 input_class_name, extra_args))
            else:
                obj_id, arg_dict = split_curl(extra_args)
                try:
                    if isinstance(arg_dict, str):
                        attr = arg_dict
                        return dict_method[input_method]("{} {} {}".format(
                                                         input_class_name,
                                                         obj_id, attr))
                    elif isinstance(arg_dict, dict):
                        return dict_method[input_method]("{} {} {}".format(
                                                         input_class_name, obj_id,
                                                         arg_dict))
                except Exception:
                    print("** argument missing **")
        print("** unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """
        To retrieve number of instances of a class
        """
        objects = storage.all()
        args = shlex.split(arg)
        input_class_name = args[0]

        num = 0

        if args:
            if input_class_name in self.allowed_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == input_class_name:
                        num += 1
                print(num)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

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
                curl_brace = re.search(r"\{(.*?)\}", arg)

                if curl_brace:
                    str_data = curl_brace.group(1)

                    arg_dict = ast.literal_eval("{" + str_data + "}")
                    attr_name = list(arg_dict.keys())
                    attr_value = list(arg_dict.values())
                    attr_name1 = attr_name[0]
                    attr_value1 = attr_value[0]
                    attr_name2 = attr_name[1]
                    attr_value2 = attr_value[1]
                    setattr(obj, attr_name1, attr_value1)
                    setattr(obj, attr_name2, attr_value2)
                else:
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
