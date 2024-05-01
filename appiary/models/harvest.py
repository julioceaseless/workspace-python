#!/usr/bin/python3
"""Harvests"""

from datetime import datetime
from models.base_model import BaseModel
from models.beehive import Beehive

class Harvest(BaseModel):
    """ record honey harvests"""
    count = 0
    def __init__(self, beehive):
        super().__init__()
        Harvest.count += 1
        self.beehive = beehive
        self.quantity = 0
        self.next_harvest = self.set_next_harvest().isoformat()

    def set_next_harvest(self):
        """record quantity harvested"""
        self.beehive.honey_ready = False
        current_month = datetime.now().month
        next_month = (current_month + 3) % 12
        next_year = datetime.now().year + (current_month + 3) / 12
        return datetime(int(next_year), int(next_month), int(self.created_at.day))

if __name__ == "__main__":
    beehive = Beehive("1234")
    harvest = Harvest(beehive)
    print(harvest.__dict__)
    print("---------------beehive--------------------")
    print(beehive.__dict__)
    
