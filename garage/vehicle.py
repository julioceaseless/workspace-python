#!/usr/bin/env python3
"""
Declares the vehicle class
"""


class Vehicle:
    def __init__(self, make, model, yom, number_plate, owner_name):
        self.make = make
        self.model = model
        self.yom = yom
        self.num_plate = number_plate
        self.owner = owner_name

    def __repr__(self):
        return f"{self.make} {self.model}\n{self.yom}\n{self.num_plate}"


if __name__ == "__main__":

    vehicle = Vehicle("Subaru", "Impreza", 2006, "KBY-290B", "Julius Machira")
    print(vehicle)

