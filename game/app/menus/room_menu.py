# -*- coding: utf-8 -*-


from .base_menu import BaseMenu
from ..room_options import *


class RoomMenu(BaseMenu):
    """
    RoomMenu inherits BaseMenu and all of its basic behaviours, with exception for handle_input_taken method.
    Instances of this class are used thoroughly the game to allow player with basic interactions with systems.
    Every option chosen result in redirecting player to another menu – e.g. choosing OPTION_TRAVEL opens menu
    filled with travel destinations to choose from.

    Parameters
    ----------
    room : Room
        Room provides all data required by BaseMenu: room.room_type becomes header, room.doors are returned if
        OPTION_TRAVEL is chosen, and so on.

    Attributes
    ----------
    room : Room
        Instace of Room class.
    header : str
        Header of the menu. Will be printed on the top, in all-caps.
    options : Union[list | None]
        List of options that will be printed (and handled by the children of this class).
    """

    def __init__(self, room):
        self.room = room
        super().__init__(self.room.room_type, options=ALL_ROOM_OPTIONS)

    def handle_input_taken(self, input_taken):
        """
        Finds option from self.options according to the user input, then calls handle_option to take an action.
        """
        option_returned = None
        try:
            option_chosen_int = int(input_taken)
            if option_chosen_int < 1:
                option_returned = None
            else:
                option_returned = self.options[int(input_taken) - 1]
        except IndexError or ValueError:
            option_returned = None
        finally:
            return self.handle_option(option_returned)

    def handle_option(self, option):
        """Takes option found by handle_input_taken method then takes an action."""
        if option == "Travel to destination":
            return self.room.get_doors()
