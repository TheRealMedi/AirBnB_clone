#!/usr/bin/python3
"""

"""
import json


class FileStorage():
    """
    Initializing FileStorage Class.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary '__objects'.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the obj with key <obj class name>.id
        into '__objects'.
        """
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
        """
        Deserializes process.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                the_dict = json.loads(f.read())
                for value in the_dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
