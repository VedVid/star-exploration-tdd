# -*- coding: utf-8 -*-


from .base_menu import BaseMenu


class TravelMenu(BaseMenu):
    """
    TravelMenu inherits BaseMenu and all of its basic behaviours, with exception for handle_input_taken method.
    Instances of this class are used thoroughly the game to allow player to travel from one room to another.

    Parameters
    ----------
    room : Room
        Room provides all data required by BaseMenu: room.room_type becomes header, room.doors are required to
        return door chosen from the player, and so on.

    Attributes
    ----------
    room : Room
        Instace of Room class.
    header : str
        Header of the menu. Will be printed on the top, in all-caps.
    options : Union[list | None]
        List of options (doors available from this room) that will be printed and handled.
    """

    def __init__(self, room):
        self.room = room
        super().__init__(self.room.room_type, options=self.room.doors)

    def handle_input_taken(self, input_taken):
        """
        Finds option from self.options according to the user input, then returns chosen option.
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
            return option_returned
