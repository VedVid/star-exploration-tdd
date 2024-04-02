# -*- coding: utf-8 -*-


from .room_types import *


class Player:
    """
    Player class represents all data that is important from the player perspective. Currently it holds only info about
    current room, in form of instance of Room the player is in.
    In the future, it will also hold info about cargo and money.

    Attributes
    ----------
    room Union[Room | None]
        When Player is spawned at the beginning of game, then room is set to None. It gets set to Room intance
        only after player chooses the first destination of their travel.
    """
    def __init__(self):
        self.room = None

    def get_room(self):
        """Gets None or instance of Room in which player currently is."""
        return self.room

    def set_room(self, room):
        """Sets room to room instance."""
            if room.room_type in ALL_ROOM_TYPES:
                self.room = room
            else:
                raise ValueError("Incorrect room type set.")
        else:
            raise ValueError("Incorrect room type set.")
