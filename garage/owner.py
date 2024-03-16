#!/usr/bin/env python3
""" class for garage customer details """
import uuid


class Car_Owner:

    def __init__(self, firstname, lastname):
        self.my_id = str(uuid.uuid4())
        self.first_name = firstname
        self.last_name = lastname


if __name__ == "__main__":
    owner = Car_Owner("Julius", "Machira")
    owner1 = Car_Owner("Levi", "Ireri")
    print(f"{owner.my_id}: {owner.first_name} {owner.last_name}")
    print(f"{owner1.my_id}: {owner1.first_name} {owner1.last_name}")
