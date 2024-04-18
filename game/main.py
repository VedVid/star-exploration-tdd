# -*- coding: utf-8 -*-


from random import randint

from app.menus.first_room_menu import FirstRoomMenu
from app.menus.room_menu import RoomMenu
from app.menus.travel_menu import TravelMenu
from app.player import Player
from app.room import Room
from app.rooms_generation import RoomsGenerator
from app.room_types import *
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
    new_room = None

    while True:
        if isinstance(m, FirstRoomMenu):
            new_room = Room(room_type=new_location)
            player.set_room(new_room)
            m = RoomMenu(new_room)
        else:
            m.print_separator()
            m.print_header()
            m.print_options()
            option_chosen = m.handle_input_taken(m.take_input())
            if isinstance(m, RoomMenu):
                if option_chosen[0] in ALL_ROOM_TYPES:
                    m = TravelMenu(new_room)
            elif isinstance(m, TravelMenu):
                new_room = Room(room_type=option_chosen)
                m = RoomMenu(new_room)
                # elif player wants to buy
                # elif player wants to sell
            # elif isinstance(m, BuyMenu)
            # elif isinstance(m, SellMenu)
