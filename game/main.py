# -*- coding: utf-8 -*-


from random import randint

from app.menus.base_menu import BaseMenu
from app.rooms_generation import RoomsGenerator
from app.ship import Ship
from app.ship_variables import *


if __name__ == "__main__":
    rooms_generator = RoomsGenerator()
    player_ship = Ship(
        attack=randint(ATTACK_MIN, ATTACK_MAX),
        defense=randint(DEFENSE_MIN, DEFENSE_MAX),
        cargo_space=randint(CARGO_MIN, CARGO_MAX),
        max_hp=randint(HP_MIN, HP_MAX),
    )
    rooms = rooms_generator.generate_rooms(randint(1, 3))
    m = BaseMenu()
    m.set_header("You boarded your brand-new Explorer-class starship.\nWhere will you go?")
    m.set_options(rooms)
    m.print_separator()
    m.print_header()
    m.print_options()
