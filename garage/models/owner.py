#!/usr/bin/env python3
""" class for garage customer details """


class CarOwner:
    _next_id = 1

    def __init__(self, firstname, lastname):
        self.owner_id = CarOwner._next_id
        CarOwner._next_id += 1
        self.first_name = firstname
        self.last_name = lastname


if __name__ == "__main__":
    owner = CarOwner("Julius", "Machira")
    owner1 = CarOwner("Levi", "Ireri")
    owner2 = CarOwner("Christie", "Wamuyu")
    owner3 = CarOwner("Florah", "Njoki")

    print(f"{owner.owner_id}: {owner.first_name} {owner.last_name}")
    print(f"{owner1.owner_id}: {owner1.first_name} {owner1.last_name}")
    print(f"{owner2.owner_id}: {owner2.first_name} {owner2.last_name}")
    print(f"{owner3.owner_id}: {owner3.first_name} {owner3.last_name}")

