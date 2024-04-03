# -*- coding: utf-8 -*-


from .base_menu import BaseMenu


class RoomMenu(BaseMenu):
    def handle_option(self, option_chosen):
        return ["space station", "planet base"]
