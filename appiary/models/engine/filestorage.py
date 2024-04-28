#!/usr/bin/python3
""" file storage"""
import json
from models.base_model import BaseModel
from models.beehive import Beehive
from models.apiary import Apiary
from models.inspection import Inspection
from models.user import User

classes = {
        'BaseModel': BaseModel, 'Apiary': Apiary, 'User': User, 
        'Inspection': Inspection, 'Beehive': Beehive
        }

class FileStorage:
    __file_path = "file.json"
    __objects = {}


    def all(self, cls=None):
        """Returns a dictionary of objects"""
        if cls is not None:
            filtered_objs = {}
            for key, value in FileStorage.__objects.items():
                if cls == value.__class__.__name__:
                    filtered_objs[key] = value
            return filtered_objs
        return FileStorage.__objects


    def new(self, obj):
        """create new object"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)
    
    def reload(self):
        """load objects from json file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                temp = json.load(f)
                for key, value in temp.items():
                    value = classes[value["__class__"]](**value)
                    FileStorage.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete object"""
        if obj is not None:
            # create key
            key = obj.__class__.__name__ + "." + obj.id
            del FileStorage.__objects[key]

