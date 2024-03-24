# -*- coding: utf-8 -*-


import pytest

from ship import Ship
from ship_variables import *


def test__should_set_ship_attack_to_min__when_attack_set_below_min_value():
    """Ship should not have base attack lower than minimum specified in ship_variables file."""

    ship = Ship(attack=ATTACK_MIN-1)

    assert ship.attack == ATTACK_MIN


def test__should_set_ship_attack_to_max__when_attack_set_over_max_value():
    """Ship should not have base attack higher than maximum specified in ship_variables file."""

    ship = Ship(attack=ATTACK_MAX+1)

    assert ship.attack == ATTACK_MAX


def test__should_not_interfere_to_attack_value__when_attack_is_in_range():
    """If base ship attack is within ranges specified in ship_variables file, then game should not interfere."""

    ship = Ship(attack=ATTACK_MIN+1)

    assert ship.attack == ATTACK_MIN + 1


def test__should_set_defense_to_min__when_defense_set_below_min_value():
    """Ship should not have base defense lower than minimum specified in ship_variables file."""

    ship = Ship(defense=DEFENSE_MIN-1)

    assert ship.defense == DEFENSE_MIN


def test__should_set_defense_to_max__when_defense_set_over_max_value():
    """Ship should not have base defense higher than maximum specified in ship_variables file."""

    ship = Ship(defense=DEFENSE_MAX+1)

    assert ship.defense == DEFENSE_MAX


def test__should_not_interfere_to_defense_value__when_defense_is_in_range():
    """If base ship defense is within ranges specified in ship_variables file, then game should not interfere."""

    ship = Ship(defense=DEFENSE_MIN)

    assert ship.defense == DEFENSE_MIN


def test__should_set_max_cargo_space_to_min__when_max_cargo_space_set_below_min_value():
    """Ship should not have max cargo space lower than minimum specified in ship_variables file."""

    ship = Ship(cargo_space=CARGO_MIN-1)

    assert ship.cargo_space == CARGO_MIN


def test__should_set_max_cargo_space_to_max__when_max_cargo_space_set_over_max_value():
    """Ship should not have max cargo space higher than maximum specified in ship_variables file."""

    ship = Ship(cargo_space=CARGO_MAX+1)

    assert ship.cargo_space == CARGO_MAX


def test__should_not_interfere_to_max_cargo_space__when_max_cargo_space_is_in_range():
    """If ship max cargo is within ranges specified in ship_variables file, then game should not interfere."""

    ship = Ship(cargo_space=CARGO_MIN)

    assert ship.cargo_space == CARGO_MIN


def test__should_cargo_space_be_empty__when_ship_is_newly_created():
    """In the moment of creation, ship should have empty cargo by defaul."""

    ship = Ship()

    assert len(ship.cargo) == 0


def test__should_set_max_hp_to_min__when_max_hp_is_set_below_min_value():
    """Ship should not have max hp lower than minimum specified in ship_variables file."""

    ship = Ship(max_hp=HP_MIN-1)

    assert ship.max_hp == HP_MIN


def test__should_set_max_hp_to_max__when_max_hp_is_set_over_max_value():
    """Ship should not have max hp higher than maximum specified in ship_variables file."""

    ship = Ship(max_hp=HP_MAX+1)

    assert ship.max_hp == HP_MAX


def test__should_not_interfere_to_max_hp__when_max_hp_is_in_range():
    """If ship max hp is within ranges specified in ship_variables file, then game should not interfere."""

    ship = Ship(max_hp=HP_MIN)

    assert ship.max_hp == HP_MIN


def test__should_current_hp_be_equal_to_max_hp__when_ship_is_newly_created():
    """In the moment of creation, ship current hp should be equal to its max hp by defaul."""

    ship = Ship()

    assert ship.current_hp == ship.max_hp
