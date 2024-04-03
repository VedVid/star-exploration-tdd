# -*- coding: utf-8 -*-


from .base_menu import BaseMenu
from ..room_options import *


class RoomMenu(BaseMenu):
    def __init__(self, room):
        self.room = room
        super().__init__(self.room.room_type, options=ALL_ROOM_OPTIONS)

    def handle_input_taken(self, input_taken):
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
        if option == "Travel to destination":
            return self.room.get_doors()
