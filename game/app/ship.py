# -*- coding: utf-8 -*-


from ship_variables import *


class Ship:
    """
    Ship is base player unit. It can be also used for generating enemies to encounter in the space.

    Parameters
    ----------
    attack : int
        Base attack value of ship. Can't be lower than ATTACK_MIN and can't be higher than ATTACK_MAX
        that are specified in ship_variables.
    defense : int
        Base defense value of ship. Can't be lower than DEFENSE_MIN and can't be higher than DEFENSE_MAX
        that are specified in ship_variables.
    cargo_space : int
        Space for transporting cargo. Can't be lower than CARGO_MIN and can't be higher than CARGO_MAX
        that are specified in ship_variables.
    max_hp : int
        Max health points of ship. Can't be lower than HP_MIN and can't be higher than HP_MAX that are specified
        in ship_variables.

    Attributes
    ----------
    attack : int
        Base attack value of ship. Can't be lower than ATTACK_MIN and can't be higher than ATTACK_MAX
        that are specified in ship_variables.
    defense : int
        Base defense value of ship. Can't be lower than DEFENSE_MIN and can't be higher than DEFENSE_MAX
        that are specified in ship_variables.
    cargo_space : int
        Space for transporting cargo. Can't be lower than CARGO_MIN and can't be higher than CARGO_MAX
        that are specified in ship_variables.
    cargo : list of ??? (not specified yet)
        List of currently transported cargo. Should not be longer than value of cargo_space.
    max_hp : int
        Max health points of ship. Can't be lower than HP_MIN and can't be higher than HP_MAX that are specified
        in ship_variables.
    current_hp : int
        Current health points of ship. Can't be higher than its max_hp. If current_hp of player's ship is lower than 0,
        then the game ends.
    """

    def __init__(self, attack=ATTACK_MIN, defense=DEFENSE_MIN, cargo_space=CARGO_MIN, max_hp=HP_MIN):
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
        elif self.cargo_space > CARGO_MAX:
            self.cargo_space = CARGO_MAX
        self.cargo = []
        self.max_hp = max_hp
        if self.max_hp < HP_MIN:
            self.max_hp = HP_MIN
        elif self.max_hp > HP_MAX:
            self.max_hp = HP_MAX
        self.current_hp = self.max_hp
