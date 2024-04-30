#!/usr/bin/python3
""" Create an Apiary"""
from base_model import BaseModel

class Beehive(BaseModel):
    """define an apiary"""
    count = 0

    def __init__(self, apiary):
        """initialize beehive"""
        super().__init__()
        self.id = Beehive.count
        Beehive.count += 1

        self.apiary_id = apiary.id
        self.type_of_hive = ""
        self.color = ""
        self.type_of_wood = ""
        self.num_of_frames = 0
        self.ready_for_harvest = False
        self.inspections = []
        self.harvests = []

    def add_inspection(self, inspection):
        """record inspections"""
        if not isinstance(inspection, Inspection):
            raise TypeError("Expected an object")
        else:
            self.inspection.append(inspection)

    def add_harvest(self, harvest):
        """record harvests"""
        if not isinstance(harvest, Harvest):
            raise TypeError("Expected an object")
        else:
            self.harvests.append(harvest)

    def update_harvest_status(self, status):
        """update whether the beehive is ready for harvest"""
        if status == True: 
            self.ready_for_harvest = True
        else:
            self.ready_for_harvest = False


if __name__ == "__main__":
    apiary = Apiary()
    beehive = Beehive(apiary)
    beehive1 = Beehive()
    beehive2 = Beehive()
    print(beehive.to_dict())
    print(beehive1.to_dict())
    print(beehive2.to_dict())
    print(beehive2.__class__)
    print(beehive2.__class__.__name__)
