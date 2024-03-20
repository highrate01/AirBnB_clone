#!/usr/bin/python3
"""
Defines class storage
"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    It serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        To add a new object to class attribute
        which stand as the storage for all the objecta
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """
        It retrieves all objects store in dictionary
        """

        return FileStorage.__objects

    def save(self):
        """
        It serializes the object dictionary into json format
        """

        all_objs = FileStorage.__objects
        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        To convert json file to object
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj.id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**values)

                        FileStorage.__obj[key] = instance
                except Exception:
                    pass
