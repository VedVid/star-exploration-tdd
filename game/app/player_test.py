# -*- coding: utf-8 -*-


import pytest

from .player import Player
from .room import Room
from .room_types import *
from .ship import Ship


def test__should_game_create_random_ship__when_player_is_spawned_without_ship_passed_to_the_constructor():
    """Ensures that player always spawn with Ship, even if Ship is not passed to constructor."""

    player = Player()

    assert player.ship is not None


def test__should_set_ship_correctly__when_ship_is_passed_as_argument_to_constructor():
    """Player should have the custom ship if this ship is passed as argument to constructor during instancing."""

    ship = Ship()

    player = Player(ship)

    assert player.ship is ship


def test__should_get_correct_ship_info__when_ship_getter_is_called():
    """Check if ship getter works correctly."""

    ship = Ship()
    player = Player(ship)

    result = player.get_ship()

    assert result == ship


def test__should_player_location_be_set_as_none__when_game_starts():
    """Checks if player.room is always set to None at the moment of spawn."""

    player = Player()

    result = player.room

    assert result is None


def test__should_set_player_room__when_player_travels():
    """Ensures that the player.room is set correctly after player changes location."""

    player = Player()
    room = Room(room_type=PLANET_BASE)

    player.set_room(room)
    result = player.room

    assert result.room_type == PLANET_BASE


def test__should_raise_value_error__when_room_with_invalid_room_type_set_is_passed_as_argument_to_room_setter():
    """Checks if game correctly raises ValueError if Room with incorrect data is passed to the room setter."""

    player = Player()
    room = Room(room_type=PLANET_BASE)
    room.room_type = "Incorrect Room Type"

    with pytest.raises(ValueError, match="Incorrect room type set."):
        player.set_room(room)


def test__should_raise_type_error__when_invalid_type_of_argument_is_passed_to_room_setter():
    """Checks if game correctly raises TypeError if argument other than Room is passed to the room setter."""

    player = Player()

    with pytest.raises(TypeError, match="Incorrect type of argument passed."):
        player.set_room("dgsg")


def test__should_return_player_room__when_getter_is_called():
    """Tests player room getter."""

    player = Player()
    room = Room(room_type=PLANET_BASE)

    player.set_room(room)
    result = player.get_room()

    assert result.room_type == PLANET_BASE
