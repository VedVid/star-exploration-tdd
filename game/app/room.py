# -*- coding: utf-8 -*-


from random import choice

from .room_types import ALL_ROOM_TYPES


class Room:
    def __init__(self, room_type=None):
        self.room_type = room_type
        if self.room_type is None:
            self.set_room_type()

    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type="random"):
        if room_type in ALL_ROOM_TYPES:
            self.room_type = room_type
        else:
            # Assuming room_type == "random"
            self.room_type = choice(ALL_ROOM_TYPES)

    def get_doors(self):
        return [1]
