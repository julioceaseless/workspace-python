#!/usr/bin/python3
"""Harvests"""

from datetime import datetime
from models.base_model import BaseModel
from models.beehive import Beehive
import models

class Harvest(BaseModel):
    """ record honey harvests"""
    count = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Harvest.count += 1
        self.hive_id = kwargs.get("hive_id")
        self.quantity = 0
        self.notes = kwargs.get("notes")
        self.next_harvest_date = self.next_harvest()

    
    def next_harvest(self):
        """schedule the next harvest date"""
        beehive = models.storage.get("Beehive", self.hive_id)
        if beehive and beehive.ready_for_harvest:
            beehive.ready_for_harvest = False
            current_month = datetime.now().month
            next_month = (current_month + 3) % 12
            next_year = datetime.now().year + (current_month + 3) / 12
            return datetime(int(next_year), int(next_month), int(self.created_at.day)).isoformat()
        else:
            return f"TBD"


if __name__ == "__main__":
    beehive = Beehive("1234")
    harvest = Harvest(beehive)
    print(harvest.__dict__)
    print("---------------beehive--------------------")
    print(beehive.__dict__)
    
