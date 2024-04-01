# -*- coding: utf-8 -*-


import pytest

from .first_room_menu import FirstRoomMenu
from ..room_types import *


def test__should_return_space_station__when_space_station_option_chosen(monkeypatch):
    """Ensure that the correct option is returned on user input. Uses concrete example."""

    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr("builtins.input", lambda _: "1")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result == SPACE_STATION


def test__should_return_planet_base__when_planet_base_option_chosen(monkeypatch):
    """Ensure that the correct option is returned on user input. Uses concrete example."""

    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr("builtins.input", lambda _: "2")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result == PLANET_BASE


def test__should_return_space__when_space_option_chosen(monkeypatch):
    """Ensure that the correct option is returned on user input. Uses concrete example."""

    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr("builtins.input", lambda _: "3")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result == SPACE


def test__should_return_none__when_chosen_option_is_incorrect(monkeypatch):
    """Ensure that handle_option method returns None when incorrect option is chosen."""

    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr("builtins.input", lambda _: "999")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result is None


def test__should_return_none__when_input_is_incorrect(monkeypatch):
    """Ensure that handle_option method returns None on incorrect type of user input."""

    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr("builtins.input", lambda _: "sadafgsdgsf")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result is None


def test__should_return_none__when_input_is_number_lesser_than_one(monkeypatch):
    """Ensure that handle_option method returns None on incorrect number entered by user."""

    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr("builtins.input", lambda _: "0")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result is None
