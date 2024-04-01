# -*- coding: utf-8 -*-


import pytest
import random
from unittest import mock

from .room import Room
from .room_types import *


def test__should_return_correct_room_type__when_get_room_type_called():
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
    random_room = Room()

    assert random_room.room_type in ALL_ROOM_TYPES


def test__should_generate_one_door__when_randint_returns_1():
    with mock.patch("random.randint") as randint:
        randint.return_value = 1
        room = Room()

    assert len(room.get_doors()) == 1


def test__should_generate_two_doors__when_randint_returns_2():
    with mock.patch("random.randint") as randint:
        randint.return_value = 2
        room = Room()

    assert len(room.get_doors()) == 2


def test__should_generate_three_doors__when_randint_returns_3():
    with mock.patch("random.randint") as randint:
        randint.return_value = 3
        room = Room()

    assert len(room.get_doors()) == 3


def test__should_generate_any_cargo__when_class_is_instanced():
    room = Room()

    assert len(room.cargo_list) > 0


def test__should_generate_specific_set_of_cargos__when_class_is_instanced_with_random_seed_0():
    random.seed(0)
    room = Room()

    assert room.cargo_list == [
        {'name': 'illegal goods', 'price_min': 50, 'price_max': 500, 'price_current': 233},
        {'name': 'animals', 'price_min': 10, 'price_max': 200, 'price_current': 139},
        {'name': 'food', 'price_min': 5, 'price_max': 50, 'price_current': 23},
        {'name': 'industrial crate', 'price_min': 50, 'price_max': 250, 'price_current': 85}
    ]


def test__should_assign_right_cargo_list__when_list_of_cargo_is_passed_to_set_cargo_list_method():
    room = Room()

    room.set_cargo_list([
        {
    "name": "food",
    "price_min": 5,
    "price_max": 50,
    "price_current": 27,
        }
    ])

    assert room.cargo_list == [
        {
            "name": "food",
            "price_min": 5,
            "price_max": 50,
            "price_current": 27,
        }
    ]


def test__should_return_correct_cargo_list__when_cargo_list_getter_is_called():
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
            }
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
            }
        ]
