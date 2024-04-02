# -*- coding: utf-8 -*-


from random import randint

from .room import Room
from .room_types import *
from .ship import Ship
from .ship_variables import *


class Player:
    """
    Player class represents all data that is important from the player perspective. Currently it holds info about
    current room and player's ship.
    In the future, it will also hold info about cargo and money.

    Attributes
    ----------
<<<<<<< HEAD
=======
    ship : Ship
        Player's ship, with its cargo space, hp, attack and defense. Since player won't change the ship during
        the gameplay, there is no setter method for setting ship.
>>>>>>> origin/feature-bind-ship-to-player
    room : Union[Room | None]
        When Player is spawned at the beginning of game, then room is set to None. It gets set to Room intance
        only after player chooses the first destination of their travel.
    ship : Ship
        Player's ship, with its cargo space, hp, attack and defense. Since player won't change the ship during
        the gameplay, there is no setter method for setting ship.
    """

    def __init__(self, ship=None):
        self.room = None
        self.ship = ship
        if self.ship is None:
            self.create_ship()

    def get_room(self):
        """Gets None or instance of Room in which player currently is."""
        return self.room

    def set_room(self, room):
        """Sets room to room instance."""
        if isinstance(room, Room):
            if room.room_type in ALL_ROOM_TYPES:
                self.room = room
            else:
                raise ValueError("Incorrect room type set.")
        else:
            raise TypeError("Incorrect type of argument passed.")

    def create_ship(self):
        self.ship = Ship(
            attack=randint(ATTACK_MIN, ATTACK_MAX),
            defense=randint(DEFENSE_MIN, DEFENSE_MAX),
            cargo_space=randint(CARGO_MIN, CARGO_MAX),
            max_hp=randint(HP_MIN, HP_MAX),
        )
