# -*- coding: utf-8 -*-


import pytest

from ship import Ship
from ship_variables import *


def test__should_set_ship_attack_to_min__when_attack_set_below_min_value():
    ship = Ship(attack=ATTACK_MIN-1)

    assert ship.attack == ATTACK_MIN


def test__should_set_ship_attack_to_max__when_attack_set_over_max_value():
    ship = Ship(attack=ATTACK_MAX+1)

    assert ship.attack == ATTACK_MAX


def test__should_not_interfere_to_attack_value__when_attack_is_in_range():
    ship = Ship(attack=ATTACK_MIN+1)

    assert ship.attack == ATTACK_MIN + 1


def test__should_set_defense_to_min__when_defense_set_below_min_value():
    ship = Ship(defense=DEFENSE_MIN-1)

    assert ship.defense == DEFENSE_MIN


def test__should_set_defense_to_max__when_defense_set_over_max_value():
    ship = Ship(defense=DEFENSE_MAX+1)

    assert ship.defense == DEFENSE_MAX


def test__should_not_interfere_to_defense_value__when_defense_is_in_range():
    ship = Ship(defense=DEFENSE_MIN)

    assert ship.defense == DEFENSE_MIN


def test__should_set_max_cargo_space_to_min__when_max_cargo_space_set_below_min_value():
    ship = Ship(cargo_space=CARGO_MIN-1)

    assert ship.cargo_space == CARGO_MIN


def test__should_set_max_cargo_space_to_max__when_max_cargo_space_set_over_max_value():
    ship = Ship(cargo_space=CARGO_MAX+1)

    assert ship.cargo_space == CARGO_MAX


def test__should_not_interfere_to_max_cargo_space__when_max_cargo_space_is_in_range():
    ship = Ship(cargo_space=CARGO_MIN)

    assert ship.cargo_space == CARGO_MIN


def test__should_not_interfere_to_max_hp__when_max_hp_is_in_range():
    ship = Ship(max_hp=MIN_HP)

    assert ship.max_hp == MIN_HP
