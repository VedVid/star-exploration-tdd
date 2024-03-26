# -*- coding: utf-8 -*-


import pytest

from base_menu import BaseMenu


def test__should_raise_exception__when_empty_options_accessed():
    menu = BaseMenu()

    with pytest.raises(ValueError, match="Non-empty list of options expected."):
        menu.print_options()
