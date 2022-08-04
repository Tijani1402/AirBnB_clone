#!/usr/bin/python3
import uuid
from datetime import datetime
from t_models import a_storage

class BaseModel:
    """_summary_
    """
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            a_storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at,
             "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at,
            "%Y-%m-%dT%H:%M:%S.%f")
    
    def __str__(self):
        return ("[" + self.__class__.__name__ + '] (' 
                 + str(self.id) + ') ' 
                 + str(self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        a_storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
