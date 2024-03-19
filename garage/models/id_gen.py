#!/usr/bin/env python3
""" id generator """
from uuid import uuid4


class IdGen:
    """ creates a unique id for objects """

    def __init__(self):
        self.obj_id = str(uuid4())
