# -*- coding: utf-8 -*-


import pytest

from ship import Ship
from ship_variables import *


def test__should_set_ship_attack_to_min__when_attack_set_below_min_value():
    ship = Ship(attack=ATTACK_MIN-1)

    assert ship.attack == ATTACK_MIN
