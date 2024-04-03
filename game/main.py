# -*- coding: utf-8 -*-


from random import randint

from app.menus.first_room_menu import FirstRoomMenu
from app.player import Player
from app.room import Room
from app.rooms_generation import RoomsGenerator
from app.ship import Ship
from app.ship_variables import *


if __name__ == "__main__":
    rooms_generator = RoomsGenerator()
    ship = Ship(
        attack=randint(ATTACK_MIN, ATTACK_MAX),
        defense=randint(DEFENSE_MIN, DEFENSE_MAX),
        cargo_space=randint(CARGO_MIN, CARGO_MAX),
        max_hp=randint(HP_MIN, HP_MAX),
    )
    player = Player(ship=ship)
    rooms = rooms_generator.generate_rooms(randint(1, 3))
    m = FirstRoomMenu()
    m.set_header(
        "You boarded your brand-new Explorer-class starship.\nWhere will you go?"
    )
    m.set_options(rooms)
    m.print_separator()
    m.print_header()
    m.print_options()
    new_location = m.handle_input_taken(m.take_input())

    new_room = Room(room_type=new_location)
    player.set_room(new_room)
    from pprint import pprint
    pprint(player.room)
    pprint(player.room.room_type)
    pprint(player.room.doors)
    pprint(player.room.cargo_list)
