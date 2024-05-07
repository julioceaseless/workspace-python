#!/usr/bin/python3
"""Record harvests"""
from models.base_model import BaseModel
from datetime import datetime


class Inspection(BaseModel):
    """ harvests management"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.beehive_id = kwargs.get('beehive_id')
        self.notes = kwargs.get('notes')


    def update_notes(self, update_text):
        """update the notes"""
        if update_text:
            self.notes = update_text
            self.updated_at = datetime.now()

    def ready_for_harvest(self, status):
        """ update the status of the beehive"""
        beehive = storage.get_beehive_by_id(self.beehive_id)
        if beehive is None:
            return f"Beehive does not exist"
        beehive.update_harvest_status(status)
        

if __name__ == "__main__":
    inspection = Inspection("HIVE-002", "Good condition")
    print(inspection.to_dict())
    inspection.update_notes("Ants trying to enter the colony")
    print(inspection.to_dict())
