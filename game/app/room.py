# -*- coding: utf-8 -*-


import random

from .cargo_types import ALL_CARGO_TYPES
from .room_types import ALL_ROOM_TYPES


class Room:
    def __init__(self, room_type=None, doors=None, cargo_list=None):
        self.room_type = room_type
        if self.room_type is None:
            self.set_room_type()
        self.doors = doors
        if self.doors is None:
            self.set_doors()
        self.cargo_list = cargo_list
        if self.cargo_list is None:
            self.set_cargo_list()

    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type="random"):
        if room_type in ALL_ROOM_TYPES:
            self.room_type = room_type
        else:
            # Assuming room_type == "random"
            self.room_type = random.choice(ALL_ROOM_TYPES)

    def set_doors(self, doors="random"):
        if doors == "random":
            no_of_doors = random.randint(1, len(ALL_ROOM_TYPES))
            self.doors = []
            while len(self.doors) < no_of_doors:
                self.doors.append(random.choice(ALL_ROOM_TYPES))

    def get_doors(self):
        return self.doors

    def set_cargo_list(self, cargo_list="random"):
        try:
            for cargo in cargo_list:
                self.cargo_list.append(cargo)
        except AttributeError:
            cargo_num = random.randint(1, len(ALL_CARGO_TYPES))
            tmp_cargo_types = ALL_CARGO_TYPES[:]
            self.cargo_list = []
            while len(self.cargo_list) < cargo_num:
                random.shuffle(tmp_cargo_types)
                new_cargo = tmp_cargo_types.pop()
                new_cargo["price_current"] = random.randint(
                    new_cargo["price_min"],
                    new_cargo["price_max"]
                )
                self.cargo_list.append(new_cargo)
