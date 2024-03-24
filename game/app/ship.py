# -*- coding: utf-8 -*-


from ship_variables import *


class Ship:
    def __init__(self, attack):
        self.attack = attack
        if self.attack < ATTACK_MIN:
            self.attack = ATTACK_MIN
        elif self.attack > ATTACK_MAX:
            self.attack = ATTACK_MAX
