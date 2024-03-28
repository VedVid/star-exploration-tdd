# -*- coding: utf-8 -*-


import pytest

from .first_room_menu import FirstRoomMenu
from ..room_types import *


def test__should_return_space_station__when_space_station_option_chosen(monkeypatch):
    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr('builtins.input', lambda _: "1")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result == SPACE_STATION


def test__should_return_planet_base__when_planet_base_option_chosen(monkeypatch):
    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr('builtins.input', lambda _: "2")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result == PLANET_BASE


def test__should_return_space__when_space_option_chosen(monkeypatch):
    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr('builtins.input', lambda _: "3")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result == SPACE


def test__should_return_none__when_chosen_option_is_incorrect(monkeypatch):
    menu = FirstRoomMenu()

    menu.set_options([SPACE_STATION, PLANET_BASE, SPACE])
    monkeypatch.setattr('builtins.input', lambda _: "999")
    chosen = menu.take_input()
    result = menu.handle_option(chosen)

    assert result is None
