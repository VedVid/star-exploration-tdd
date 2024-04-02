# -*- coding: utf-8 -*-


from .room_types import *


class Player:
    """
    Player class represents all data that is important from the player perspective. Currently it holds only info about
    current room. In the future, it will also hold info about cargo and money.
    """
    def __init__(self):
        self.room = None

    def get_room(self):
        return self.room

    def set_room(self, room):
        if room in ALL_ROOM_TYPES:
            self.room = room
        else:
            raise ValueError("Incorrect room type set.")
