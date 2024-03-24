# -*- coding: utf-8 -*-


import pytest

from rooms_generation import RoomsGenerator


def test__should_generate_a_room__when_method_is_called():
    rooms_generator = RoomsGenerator()

    result = rooms_generator.generate()

    assert result is not None
