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


def test__should_return_none__when_input_is_number_lesser_than_one(monkeypatch):
    """Ensure that handle_input_taken method returns None on incorrect number entered by user."""

    room = Room()
    menu = TravelMenu(room=room)

    monkeypatch.setattr("builtins.input", lambda _: "0")
    result = menu.handle_input_taken(menu.take_input())

    assert result is None


def test__should_return_none__when_chosen_option_is_incorrect(monkeypatch):
    """Ensure that handle_input_taken method returns None when incorrect option is chosen."""

    room = Room()
    menu = TravelMenu(room=room)

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr("builtins.input", lambda _: "999")
    result = menu.handle_input_taken(menu.take_input())

    assert result is None


def test__should_return_none__when_input_is_incorrect(monkeypatch):
    """Ensure that handle_input_taken method returns None on incorrect type of user input."""

    room = Room()
    menu = TravelMenu(room=room)

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr("builtins.input", lambda _: "sadafgsdgsf")
    result = menu.handle_input_taken(menu.take_input())

    assert result is None
    