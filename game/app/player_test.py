# -*- coding: utf-8 -*-


import pytest

from .player import Player
from .room_types import *


def test__should_player_location_be_set_as_none__when_game_starts():
    player = Player()

    result = player.room

    assert result is None


def test__should_set_player_room__when_player_travels():
    player = Player()

    player.set_room(PLANET_BASE)
    result = player.room

    assert result == PLANET_BASE


def test__should_raise_exception__when_incorrect_type_of_argument_passed_to_room_setter():
    player = Player()

    with pytest.raises(ValueError, match="Incorrect room type set."):
        player.set_room([12325])


def test__should_return_player_room__when_getter_is_called():
    player = Player()

    player.set_room(PLANET_BASE)
    result = player.get_room()

    assert result == PLANET_BASE
