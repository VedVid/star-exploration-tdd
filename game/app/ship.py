# -*- coding: utf-8 -*-


from ship_variables import *


class Ship:
    def __init__(self, attack=ATTACK_MIN, defense=DEFENSE_MIN, cargo_space=CARGO_MIN):
        self.attack = attack
        if self.attack < ATTACK_MIN:
            self.attack = ATTACK_MIN
        elif self.attack > ATTACK_MAX:
            self.attack = ATTACK_MAX
        self.defense = defense
        if self.defense < DEFENSE_MIN:
            self.defense = DEFENSE_MIN
        elif self.defense > DEFENSE_MAX:
            self.defense = DEFENSE_MAX
        self.cargo_space = cargo_space
        if self.cargo_space < CARGO_MIN:
            self.cargo_space = CARGO_MIN
