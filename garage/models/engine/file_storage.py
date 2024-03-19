#!/usr/bin/env python3
""" This module saves objects to json """
import json
from os import path


class FileStorage:
    """
    stores objects to JSON file and retrieves them
    back fro JSON to objects
    """
    __file = "file.json"
    __objects = {}

    def show_all(self):
        """ display all objects """
        return FileStorage.__objects

    def add_new(self, obj):
        """add new object to the storage dictionary"""
        new_dict = {}

        # create a new dict without first entry
        for key, value in obj.__dict__.items():
            if key != "obj_id":
                new_dict[key] = value

        # create a key
        key = f"{obj.__class__.__name__}.{obj.obj_id}"
        
        # add new object to dictionary
        FileStorage.__objects[key] = new_dict
