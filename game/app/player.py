# -*- coding: utf-8 -*-


from .room import Room
from .room_types import *


class Player:
    """
    Player class represents all data that is important from the player perspective. Currently it holds info about
    current room and player's ship.
    In the future, it will also hold info about cargo and money.

    Attributes
    ----------
    ship : Ship
        Player's ship, with its cargo space, hp, attack and defense.
    room : Union[Room | None]
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
        if isinstance(room, Room):
            if room.room_type in ALL_ROOM_TYPES:
                self.room = room
            else:
                raise ValueError("Incorrect room type set.")
        else:
            raise TypeError("Incorrect type of argument passed.")
