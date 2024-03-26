# -*- coding: utf-8 -*-


from random import shuffle

from .room_types import *


class RoomsGenerator:
    """
    RoomsGenerator is a class that is used for generating rooms. These rooms are available for the player
    to choose from to continue their journey.

    Attributes
    ----------
    _rooms : list of strings
        Contains every possible type of room to generate.
    _rooms_available : Union[list of strings, None]
        Copies _rooms content at the start of generate_rooms method. choose_room_randomly uses this list to pop
        random rooms.
    """

    _rooms = [SPACE_STATION, PLANET_BASE, SPACE]
    _rooms_available = None

    def fill_rooms_available(self):
        """
        Fills _rooms_available with values copied from _rooms. Necessary to allow shuffling and popping rooms
        by choose_room_randomly method.
        """
        self._rooms_available = self._rooms[:]

    def choose_room_randomly(self):
        """
        Returns random room from _rooms class list. It is used by generate_rooms method.

        Returns
        -------
        room : string
            Randomly chosen room from _rooms class attribute.
        """
        print(self._rooms_available)
        shuffle(self._rooms_available)
        return self._rooms_available.pop()

    def generate_rooms(self, amount):
        """
        Returns list of unique rooms.

        Parameters
        ----------
        amount : int
            Amount of rooms that should be generated.

        Returns
        -------
        new_rooms: list of strings
            List of generated rooms.
        """
        new_rooms = []
        # Small optimization: return copy of class _rooms if its length is equal to amount of rooms to be generated.
        if amount == len(self._rooms):
            return self._rooms[:]
        # Otherwise, we generate rooms by randomly choosing room to append the list.
        self.fill_rooms_available()
        while amount > 0:
            new_room = self.choose_room_randomly()
            new_rooms.append(new_room)
            amount -= 1
        return new_rooms
