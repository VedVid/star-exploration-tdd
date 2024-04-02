# -*- coding: utf-8 -*-


import pytest
import random
from unittest import mock

from .cargo_types import *
from .room import Room
from .room_types import *


def test__should_return_correct_room_type__when_get_room_type_called():
    """Ensure that room type getter works correctly."""

    room_space_station = Room(SPACE_STATION)
    room_planet_base = Room(PLANET_BASE)
    room_space = Room(SPACE)

    result_space_station = room_space_station.get_room_type()
    result_planet_base = room_planet_base.get_room_type()
    result_space = room_space.get_room_type()

    assert result_space_station == SPACE_STATION
    assert result_planet_base == PLANET_BASE
    assert result_space == SPACE


def test__should_set_correct_room_type__when_set_room_type_called_with_correct_room_type():
    """Ensure that room type setter works correctly."""

    room_space_station = Room()
    room_space_station.set_room_type(SPACE_STATION)
    room_planet_base = Room()
    room_planet_base.set_room_type(PLANET_BASE)
    room_space = Room()
    room_space.set_room_type(SPACE)

    assert room_space_station.room_type == SPACE_STATION
    assert room_planet_base.room_type == PLANET_BASE
    assert room_space.room_type == SPACE


def test__should_set_random_room_type__when_room_is_instanced_without_room_type_argument():
    """Ensure that when no arguments are provided, game correctly sets the room type at random."""

    random_room = Room()

    assert random_room.room_type in ALL_ROOM_TYPES


def test__should_set_random_room_type__when_argument_passed_to_setter_is_invalid():
    """Ensures that incorrect argument is handled correctly by set_room_type method."""

    room = Room()

    room.set_room_type(124252352354)
    result = room.get_room_type()

    assert result in ALL_ROOM_TYPES


def test__should_set_random_rooms__when_argument_passed_to_setter_is_list_with_incorrect_values():
    """Ensures list with incorrect elements is handled correctly by set_doors method."""

    room = Room()

    room.set_doors(["12434", 12141, [1]])
    result = room.get_doors()

    for door in result:
        assert door in ALL_ROOM_TYPES


def test__should_set_random_rooms__when_argument_passed_to_setter_is_not_list():
    """Ensures that argument that is not list is handled correctly by set_doors method."""

    room = Room()

    room.set_doors(124134)
    result = room.get_doors()

    for door in result:
        assert door in ALL_ROOM_TYPES


def test__should_generate_one_door__when_randint_returns_1():
    """Ensures the correct amount of generated doors."""

    with mock.patch("random.randint") as randint:
        randint.return_value = 1
        room = Room()

    assert len(room.get_doors()) == 1


def test__should_generate_two_doors__when_randint_returns_2():
    """Ensures the correct amount of generated doors."""

    with mock.patch("random.randint") as randint:
        randint.return_value = 2
        room = Room()

    assert len(room.get_doors()) == 2


def test__should_generate_three_doors__when_randint_returns_3():
    """Ensures the correct amount of generated doors."""

    with mock.patch("random.randint") as randint:
        randint.return_value = 3
        room = Room()

    assert len(room.get_doors()) == 3


def test__should_generate_any_cargo__when_class_is_instanced():
    """Ensure that the cargo_list is never empty."""

    room = Room()

    assert len(room.cargo_list) > 0


def test__should_generate_specific_set_of_cargos__when_class_is_instanced_with_random_seed_0():
    """Checks if cargo list is correctly created using seeded rng."""

    random.seed(0)
    room = Room()

    assert room.cargo_list == [
        {
            "name": "illegal goods",
            "price_min": 50,
            "price_max": 500,
            "price_current": 233,
        },
        {"name": "animals", "price_min": 10, "price_max": 200, "price_current": 139},
        {"name": "food", "price_min": 5, "price_max": 50, "price_current": 23},
        {
            "name": "industrial crate",
            "price_min": 50,
            "price_max": 250,
            "price_current": 85,
        },
    ]


def test__should_assign_right_cargo_list__when_list_of_cargo_is_passed_to_set_cargo_list_method():
    """Ensures that the cargo list setter works correctly."""

    room = Room()

    room.set_cargo_list(
        [
            {
                "name": "food",
                "price_min": 5,
                "price_max": 50,
                "price_current": 27,
            }
        ]
    )

    assert room.cargo_list == [
        {
            "name": "food",
            "price_min": 5,
            "price_max": 50,
            "price_current": 27,
        }
    ]


def test__should_return_correct_cargo_list__when_cargo_list_getter_is_called():
    """Ensures that the cargo list getter works correctly."""

    room = Room()

    room.set_cargo_list(
        [
            {
                "name": "food",
                "price_min": 5,
                "price_max": 50,
                "price_current": 27,
            },
            {
                "name": "illegal goods",
                "price_min": 50,
                "price_max": 500,
                "price_current": 373,
            },
        ]
    )
    result = room.get_cargo_list()

    assert result == [
        {
            "name": "food",
            "price_min": 5,
            "price_max": 50,
            "price_current": 27,
        },
        {
            "name": "illegal goods",
            "price_min": 50,
            "price_max": 500,
            "price_current": 373,
        },
    ]


def test__should_set_random_cargo_list__when_argument_passed_to_setter_is_list_with_incorrect_values():
    """Ensures list with incorrect elements is handled correctly by set_cargo_list method."""

    room = Room()

    room.set_cargo_list(["12434", 12141, [1]])
    result = room.get_cargo_list()

    for cargo in result:
        cargo["price_current"] = None
        assert cargo in ALL_CARGO_TYPES


def test__should_set_random_cargo_list__when_argument_passed_to_setter_is_list_with_incorrect_dict():
    """Ensures list with incorrect dicts within is handled correctly by set_cargo_list method."""

    room = Room()

    room.set_cargo_list(
        [
            {
                "name": "food",
                "prince_min": 5,
                "price_maaax": 50,
                "price_current": None,
            }
        ]
    )
    result = room.get_cargo_list()

    for cargo in result:
        cargo["price_current"] = None
        assert cargo in ALL_CARGO_TYPES


def test__should_set_random_cargo_list__when_argument_passed_to_setter_is_not_list():
    """Ensures that argument that is not list is handled correctly by set_cargo_list method."""

    room = Room()

    room.set_cargo_list(124134)
    result = room.get_cargo_list()

    for cargo in result:
        cargo["price_current"] = None
        assert cargo in ALL_CARGO_TYPES
