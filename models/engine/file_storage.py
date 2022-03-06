#!/usr/bin/python3
""""""
import json

class FileStorage():
    """"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """"""
        return self.__objects

    def new(self, obj):
        """"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize process
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({key: value.to_dict() for key, value in 
            self.__objects.items()}, f)
    def reload(self):
        """"""
