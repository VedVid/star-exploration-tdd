# -*- coding: utf-8 -*-


from random import choice

from .room_types import ALL_ROOM_TYPES


class Room:
    def __init__(self, room_type=None):
        self.room_type = room_type
        if self.room_type is None:
            self.room_type = choice(ALL_ROOM_TYPES)

    def get_room_type(self):
        return self.room_type
