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
