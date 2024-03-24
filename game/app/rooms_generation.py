# -*- coding: utf-8 -*-


from random import choice

from room_types import *


class RoomsGenerator:

    _rooms = [SPACE_STATION, PLANET_BASE, SPACE]

    def generate(self):
        return choice(self._rooms)
