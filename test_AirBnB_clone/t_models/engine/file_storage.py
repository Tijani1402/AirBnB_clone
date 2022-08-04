""" class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file to instances """
import json
import uuid
import os
from datetime import datetime
from t_models.base_model import BaseModel

class FileStorage:
    """_summary_
    """
    __file_path = 'j_file.json'
    __objects = {}

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        
        key = (str(eval(f'obj.__class__.__name__' )) +
        '.'+
        str(eval(f'obj.id' )))
        self.__objects[key] = obj

    def save(self):
       
        json_file_dict ={}
        for key, value in self.__objects.items():
            json_file_dict[key] = value.to_dict()
            
        with open(self.__file_path, 'w') as f:
            json.dump(json_file_dict, f)
        
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                file_dict = json.load(f)
                file_obj = {}
                for key, value in file_dict.items():
                    clsname = key.split('.')[0]
                    clsobj = eval(value['__class__'](value))
                    file_obj[key] = clsobj
                return file_obj

