#!/usr/bin/python3
"""Record harvests"""
from models.base_model import BaseModel


class Inspection(BaseModel):
    """ harvests management"""
    apiary_id = ""
    beehive_id = ""
    harvest_ready = ""
    observations = ""
