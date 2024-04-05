# -*- coding: utf-8 -*-


import pytest

from ..room import Room
from ..room_types import *
from .travel_menu import TravelMenu


def test__should_return_destination__when_a_door_is_chosen(monkeypatch):
    room = Room(doors=ALL_ROOM_TYPES)
    menu = TravelMenu(room)

    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = menu.handle_input_taken(menu.take_input())

    assert result == ALL_ROOM_TYPES[0]
