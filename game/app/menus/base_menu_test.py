# -*- coding: utf-8 -*-


import pytest

from .base_menu import BaseMenu


def test__should_raise_exception__when_empty_options_accessed():
    """Game should raise ValueError exception if player can access empty list of options."""

    menu = BaseMenu()

    with pytest.raises(ValueError, match="Non-empty list of options expected."):
        menu.print_options()


def test__should_set_options__when_setter_for_options_called():
    """
    Method set_options should transform multiple arguments into single args tuple,
    transform it into list, then bind to the options attribute.
    """

    menu = BaseMenu()

    menu.set_options("aaaaa", "bbbbb", "ccccc")

    assert len(menu.options) == 3


def test__should_set_header__when_set_header_method_called():
    """Method set_header should set header attribute to the argument passed."""

    menu = BaseMenu()

    menu.set_header("HEADER")

    assert menu.header == "HEADER"


def test__should_raise_not_implemented__when_handle_option_method_called():
    """Game should raise NotImplementedError – player should not access BaseMenu directly."""
    menu = BaseMenu()

    with pytest.raises(
        NotImplementedError,
        match="This is BaseMenu, handle_option method is not implemented here.",
    ):
        menu.handle_option()
