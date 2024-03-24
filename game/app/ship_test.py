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
