# -*- coding: utf-8 -*-


import random

from .cargo_types import ALL_CARGO_TYPES
from .room_types import ALL_ROOM_TYPES


class Room:
    """
    Room is a class that keeps all data related to the room in which player currently is, like room type, list of
    rooms that are available from there, and cargo available to buy here. Data from Room is used by various
    kind of menus. Room class does not define any behaviour with exception for setters and getters that are not quite
    necessary, but helpful for testing.

    Parameters
    ----------
    room_type : Union[str | None]
        Type of the current room. It should match one of the values definied in room_types.py file. If set to None
        as it is by default, room type is chosen randomly.
    doors : Union[list | None]
        List of all rooms available from this room. These rooms are not generated yet, only their types are specified.
        Every room must match one of the values definied in room_types.py file.
        If set to None as it is by default, game chooses amount of doors and their types randomly.
    cargo_list : Union[list | None]
        List of cargo available there. Every cargo should match one of the values definied in cargo_types.py file.
        If set to None as it is by default, game chooses amount of cargo and their type randomly.

    Attributes
    ----------
    header : str
        Header of the menu. Will be printed on the top, in all-caps.
    options : Union[list | None]
        List of options that will be printed (and handled by the children of this class).
    """

    def __init__(self, room_type=None, doors=None, cargo_list=None):
        self.room_type = room_type
        if self.room_type is None:
            self.set_room_type()
        self.doors = doors
        if self.doors is None:
            self.set_doors()
        self.cargo_list = cargo_list
        if self.cargo_list is None:
            self.set_cargo_list()

    def get_room_type(self):
        """Returns type of the current room."""
        return self.room_type

    def set_room_type(self, room_type="random"):
        """
        Sets type of the current room. If "random" or invalid value is passed to this method, the room type
        is chosen randomly.
        """
        if room_type in ALL_ROOM_TYPES:
            self.room_type = room_type
        else:
            # Assuming room_type == "random"
            self.room_type = random.choice(ALL_ROOM_TYPES)

    def get_doors(self):
        """Returns rooms that are avaible to get there from the current room."""
        return self.doors

    def set_doors(self, doors="random"):
        """
        Sets passageways to another rooms. If "random" or invalid value is passed to this method, the doors
        are being set randomly.
        """
        invalid = False
        if isinstance(doors, list):
            for door in doors:
                if door not in ALL_ROOM_TYPES:
                    invalid = True
                    break
        else:
            invalid = True
        if doors == "random" or invalid:
            no_of_doors = random.randint(1, len(ALL_ROOM_TYPES))
            self.doors = []
            while len(self.doors) < no_of_doors:
                self.doors.append(random.choice(ALL_ROOM_TYPES))

    def get_cargo_list(self):
        """Returns list of cargo that is available for player to purchase."""
        return self.cargo_list

    def set_cargo_list(self, cargo_list="random"):
        """
        Sets list of cargo available for player to purchase.. If "random" or invalid value is passed to this method,
        the cargo list is created randomly.
        """
        invalid = False
        if isinstance(cargo_list, list):
            self.cargo_list = []
            for cargo in cargo_list:
                try:
                    try:
                        if (
                            cargo["name"]
                            and cargo["price_min"]
                            and cargo["price_max"]
                            and cargo["price_current"]
                        ):
                            self.cargo_list.append(cargo)
                    except KeyError:
                        invalid = True
                except TypeError:
                    invalid = True
        elif invalid or not isinstance(cargo_list, list):
            cargo_num = random.randint(1, len(ALL_CARGO_TYPES))
            tmp_cargo_types = ALL_CARGO_TYPES[:]
            self.cargo_list = []
            while len(self.cargo_list) < cargo_num:
                random.shuffle(tmp_cargo_types)
                new_cargo = tmp_cargo_types.pop()
                new_cargo["price_current"] = random.randint(
                    new_cargo["price_min"], new_cargo["price_max"]
                )
                self.cargo_list.append(new_cargo)
