#!/usr/bin/python3
""" Create an Apiary"""
from base_model import BaseModel


class Beehive(BaseModel):
    """define an apiary"""
    def __init__(self):
        super().__init__()
        self.id = Beehive.count
        Beehive.count += 1

    apiary_id = ""
    type_of_hive = ""
    color = ""
    type_of_wood = ""
    num_of_frames = 0
    mounting_style = ""


if __name__ == "__main__":
    beehive = Beehive()
    beehive1 = Beehive()
    beehive2 = Beehive()
    print(beehive.to_dict())
    print(beehive1.to_dict())
    print(beehive2.to_dict())
    print(beehive2.__class__)
    print(beehive2.__class__.__name__)
