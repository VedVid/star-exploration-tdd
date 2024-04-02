# -*- coding: utf-8 -*-


import pytest

from .player import Player
from .room import Room
from .room_types import *


def test__should_player_location_be_set_as_none__when_game_starts():
    player = Player()

    result = player.room

    assert result is None


def test__should_set_player_room__when_player_travels():
    player = Player()
    room = Room(room_type=PLANET_BASE)

    player.set_room(room)
    result = player.room

    assert result.room_type == PLANET_BASE


def test__should_return_player_room__when_getter_is_called():
    player = Player()

    player.set_room(PLANET_BASE)
    result = player.get_room()

    assert result.room_type == PLANET_BASE
