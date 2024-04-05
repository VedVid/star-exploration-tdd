# -*- coding: utf-8 -*-


from .base_menu import BaseMenu


class TravelMenu(BaseMenu):
    def __init__(self, room):
        self.room = room
        super().__init__(self.room.room_type, options=self.room.doors)

    def handle_input_taken(self, input_taken):
        return "space station"
