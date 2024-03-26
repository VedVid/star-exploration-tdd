# -*- coding: utf-8 -*-


import pytest

from .rooms_generation import RoomsGenerator


def test__should_generate_a_room__when_method_is_called():
    """Testing if choose_room_randomly always return at least one room."""

    rooms_generator = RoomsGenerator()

    rooms_generator.fill_rooms_available()
    result = rooms_generator.choose_room_randomly()

    assert result is not None


def test__should_generate_one_room__when_only_one_room_should_be_generated():
    """Testing if generator will return exactly one room if one room is desired."""

    rooms_generator = RoomsGenerator()

    result = rooms_generator.generate_rooms(1)

    assert len(result) == 1


def test__should_generate_two_rooms__when_two_rooms_should_be_generated():
    """Testing if generator will return exactly two rooms if two rooms are desired."""

    rooms_generator = RoomsGenerator()

    result = rooms_generator.generate_rooms(2)

    assert len(result) == 2


def test__should_generate_three_rooms__when_three_rooms_should_be_generated():
    """Testing if generator will return exactly three rooms if three rooms are desired."""

    rooms_generator = RoomsGenerator()

    result = rooms_generator.generate_rooms(3)

    assert len(result) == 3


def test__should_generate_three_different_rooms__when_three_rooms_should_be_generated():
    """Testing if generator will generate three unique rooms when tasked with it."""

    rooms_generator = RoomsGenerator()

    result = rooms_generator.generate_rooms(3)

    assert len(result) == len(set(result))


def test__should_rooms_available_be_empty__when_no_fill_rooms_available_called():
    """Testing if by default _rooms_available list is empty."""

    rooms_generator = RoomsGenerator()

    assert rooms_generator._rooms_available is None


def test__should_rooms_available_be_filled__when_fill_rooms_available_called():
    """Testing if _rooms_available contains the same rooms as _rooms list after being filled."""

    rooms_generator = RoomsGenerator()

    rooms_generator.fill_rooms_available()

    assert rooms_generator._rooms == rooms_generator._rooms_available


def test__should_raise_error__when_amount_of_rooms_to_be_generated_is_larger_than_length_of_rooms_list():
    """Testing if game raises IndexError if amount of rooms to be generated are too long."""

    rooms_generator = RoomsGenerator()

    with pytest.raises(IndexError):
        rooms_generator.generate_rooms(999)
