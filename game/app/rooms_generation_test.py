# -*- coding: utf-8 -*-


import pytest

from rooms_generation import RoomsGenerator


def test__should_generate_a_room__when_method_is_called():
    rooms_generator = RoomsGenerator()

    result = rooms_generator.choose_room_randomly()

    assert result is not None


def test__should_generate_one_room__when_only_one_room_should_be_generated():
    rooms_generator = RoomsGenerator()

    result = rooms_generator.generate_rooms(1)

    assert len(result) == 1
