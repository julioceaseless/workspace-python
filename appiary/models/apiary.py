#!/usr/bin/python3
""" Create an Apiary"""
from base_model import BaseModel


class Apiary(BaseModel):
    """define an apiary"""
    name = ""
    latitude = ""
    longitude = ""
    county = ""
    town = ""
    vegetation = []


if __name__ == "__main__":
    apiary = Apiary()
    print(apiary.__dict__)
