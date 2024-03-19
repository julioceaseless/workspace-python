#!/usr/bin/env python3
"""
Declares the vehicle class
"""
from sys import argv
from id_gen import IdGen
from engine.file_storage import FileStorage

class Vehicle(IdGen):
    """ vehicle class """
    def __init__(self, make, model, yom, number_plate, owner_name):
        super().__init__()
        self.make = make
        self.model = model
        self.yom = yom
        self.num_plate = number_plate
        self.owner = owner_name

    def __repr__(self):
        return f"Make:{self.make} Model:{self.model} YOM:{self.yom} Number_Plate:{self.num_plate}"

    def add(self):
        FileStorage.add_to_dict(self)

    def display(self):
        FileStorage.show_all()



if __name__ == "__main__":

    if (len(argv) != 6):
        print ("Usage: Model, Make, YOM, Number-Plate, FirstName-LastName")
        exit (-1)

    vehicle = Vehicle(argv[1], argv[2], argv[3], argv[4], argv[5])
    print(vehicle)
    print(vehicle.__dict__)
    vehicle.add_to_dict()
    print(vehicle.display())
