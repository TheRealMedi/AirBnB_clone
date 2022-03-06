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
        """
        Deserializes(convert a string to an object) the JSON file:
        '__file_path' to a dictionary: '__objects', in case the JSON
        file doesn't exist, it does nothing.
        - When data is RECEIVED it's deserialized.
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
