# -*- coding: utf-8 -*-


from .base_menu import BaseMenu


class FirstRoomMenu(BaseMenu):

    def handle_option(self, option_chosen):
        match option_chosen:
            case "1":
                return self.options[0]
