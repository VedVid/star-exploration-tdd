# -*- coding: utf-8 -*-


import pytest

from .room_menu import RoomMenu
from ..room import Room
from ..room_types import *


def test__should_return_list_of_travel_destinations__when_player_choose_first_option(monkeypatch):
    room = Room(doors=[SPACE_STATION, PLANET_BASE])
    menu = RoomMenu(room=room)

    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = menu.handle_input_taken(menu.take_input())

    assert result == [SPACE_STATION, PLANET_BASE]
