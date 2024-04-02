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


def test__should_raise_value_error__when_room_with_invalid_room_type_set_is_passed_as_argument_to_room_setter():
    player = Player()
    room = Room(room_type=PLANET_BASE)
    room.room_type = "Incorrect Room Type"

    with pytest.raises(ValueError, match="Incorrect room type set."):
        player.set_room(room)


def test__should_raise_type_error__when_invalid_type_of_argument_is_passed_to_room_setter():
    player = Player()

    with pytest.raises(TypeError, match="Incorrect type of argument passed."):
        player.set_room("dgsg")


def test__should_return_player_room__when_getter_is_called():
    player = Player()
    room = Room(room_type=PLANET_BASE)

    player.set_room(room)
    result = player.get_room()

    assert result.room_type == PLANET_BASE
