#!/usr/bin/python3
""""""
import uuid
from datetime import datetime
from models import storage

class BaseModel():
    """"""

    def __init__(self, *args, **kwargs):
        """"""

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
        """"""
        return "[{}] [{}] [{}]"\
            .format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary.update({'created_at': self.created_at.isoformat()})
        dictionary.update({'updated_at': self.updated_at.isoformat()})
        return dictionary

