# -*- coding: utf-8 -*-


import pytest

from .player import Player


def test__should_player_location_be_set_as_none__when_game_starts():
    player = Player()

    result = player.room

    assert result is None
