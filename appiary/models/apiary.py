#!/usr/bin/python3
""" Create an Apiary"""
from base_model import BaseModel
from beehive import Beehive
from user import User


class Apiary(BaseModel):
    """define an apiary"""
    def __init__(self, name, location, user):
        super().__init__()
        self.name = name
        self.location = location
        self.user = user
        self.county = ""
        self.town = ""
        self.vegetation = []
        self.beehives = []

    def add_beehive(self, obj):
        """add beehive to apiary"""
        if not isinstance(obj, Beehive):
            raise TypeError("Expects a beehive object")
        else:
            self.beehives.append(obj.to_dict())



if __name__ == "__main__":
    beehive = Beehive()
    beehive1 = Beehive()
    beehive2 = Beehive()
    user1 = User("Julius", "Machira", 2000)
    apiary = Apiary("Kirwa C", (-73.935242, 40.730610), user1)
    apiary.add_beehive(beehive)
    apiary.add_beehive(beehive1)

    print(apiary.__dict__)
