# -*- coding: utf-8 -*-


import random

from .room_types import ALL_ROOM_TYPES


class Room:
    def __init__(self, room_type=None, doors=None):
        self.room_type = room_type
        if self.room_type is None:
            self.set_room_type()
        self.doors = doors
        if self.doors is None:
            self.set_doors()
        self.cargo_list = [1]

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
