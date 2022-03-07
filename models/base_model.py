#!/usr/bin/python3
"""
Definning the basemodel class.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    Basemodel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing base model.

        Argumments:
            -  *args  (tuple): Tuple which contains all args.
            - **kwargs (dict): Dictionary which contains all
                               argumments by key/value.
        Methods/Functions:
            - strptime(): creates a datetime object from the
                          given instance.
            - setattr():  Sets the value of an object attribute.
        """

        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    pass

                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.
                            strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))

                else:
                    setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Informal storagering object representation.
        """
        return "[{}] [{}] [{}]"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Save/updates the public instorageance attribute 'update_at'
        with the curent datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values of __dict__
        of the instorageance.
        """
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary.update({'created_at': self.created_at.isoformat()})
        dictionary.update({'updated_at': self.updated_at.isoformat()})
        return dictionary
