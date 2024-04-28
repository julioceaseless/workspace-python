#!/usr/bin/python3
'''
This is a parent model
'''
import uuid
from datetime import datetime

class BaseModel:
    """This is the base model"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()


    def to_dict(self):
        """serialize an object to dictionary"""
        # retrieve dictionary representation of the object
        obj_to_dict = self.__dict__.copy()
        # add class attribute
        obj_to_dict['__class__'] = self.__class__.__name__
        # convert datetime object to ISO formart
        obj_to_dict['created_at'] = self.created_at.isoformat()
        obj_to_dict['updated_at'] = self.updated_at.isoformat()
        return obj_to_dict


    def __str__(self):
        """Return String representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    
    def save(self):
        """save and update 'updated_at' the time to current time"""
        self.updated_at = datetime.utcnow()
