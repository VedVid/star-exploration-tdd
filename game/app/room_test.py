# -*- coding: utf-8 -*-


import pytest
import random
from unittest import mock

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


def test__should_set_correct_room_type__when_set_room_type_called_with_correct_room_type():
    room_space_station = Room()
    room_space_station.set_room_type(SPACE_STATION)
    room_planet_base = Room()
    room_planet_base.set_room_type(PLANET_BASE)
    room_space = Room()
    room_space.set_room_type(SPACE)

    assert room_space_station.room_type == SPACE_STATION
    assert room_planet_base.room_type == PLANET_BASE
    assert room_space.room_type == SPACE


def test__should_set_random_room_type__when_room_is_instanced_without_room_type_argument():
    random_room = Room()

    assert random_room.room_type in ALL_ROOM_TYPES


def test__should_generate_one_door__when_randint_returns_1():
    with mock.patch("random.randint") as randint:
        randint.return_value = 1
        room = Room()

    assert len(room.get_doors()) == 1
