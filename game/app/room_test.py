# -*- coding: utf-8 -*-


import pytest

from .room import Room
from .room_types import *


def test__should_return_correct_room_type__when_get_room_type_called():
    room_space_station = Room(SPACE_STATION)
    room_planet_base = Room(PLANET_BASE)
    room_space = Room(SPACE)

    result_space_station = room_space_station.get_room_type()
    result_planet_base = room_planet_base.get_room_type()
    result_space = room_space.get_room_type()

    assert result_space_station == SPACE_STATION
    assert result_planet_base == PLANET_BASE
    assert result_space == SPACE
