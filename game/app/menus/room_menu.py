# -*- coding: utf-8 -*-


from .base_menu import BaseMenu


class RoomMenu(BaseMenu):
    def __init__(self, header=""):
        super().__init__(header, options=["Travel to destination", "Buy cargo", "Sell cargo"])

    def handle_option(self, option_chosen):
        option_returned = None
        try:
            option_chosen_int = int(option_chosen)
            if option_chosen_int < 1:
                option_returned = None
            else:
                option_returned = self.options[int(option_chosen) - 1]
        except IndexError or ValueError:
            option_returned = None
        finally:
            if option_returned == "Travel to destination":
                return ["space station", "planet base"]
