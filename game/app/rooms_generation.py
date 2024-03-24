# -*- coding: utf-8 -*-


from random import choice

from room_types import *


class RoomsGenerator:

    _rooms = [SPACE_STATION, PLANET_BASE, SPACE]

    def choose_room_randomly(self):
        return choice(self._rooms)

    def generate_rooms(self, amount):
        new_rooms = []
        while amount > 0:
            new_room = self.choose_room_randomly()
            if new_room in new_rooms:
                continue
            new_rooms.append(self.choose_room_randomly())
            amount -= 1
        return new_rooms
