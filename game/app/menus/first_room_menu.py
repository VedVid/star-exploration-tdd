# -*- coding: utf-8 -*-


from .base_menu import BaseMenu


class FirstRoomMenu(BaseMenu):
    """
    FirstRoomMenu inherits BaseMenu and all of its basic behaviours, with exception for handle_option method.
    FirstRoomMenu is a special kind of menu that is present only in the first room, at the very beginning of game.
    It might be replaced by more generic menu class in the future.

    Parameters
    ----------
    header : str
        Header of the menu. Will be printed on the top, in all-caps.
    options : Union[list | None]
        List of options that will be printed (and handled by the children of this class).

    Attributes
    ----------
    header : str
        Header of the menu. Will be printed on the top, in all-caps.
    options : Union[list | None]
        List of options that will be printed (and handled by the children of this class).
    """

    def handle_option(self, option_chosen):
        """
        Returns option from self.options according to the user input.
        WARNING: most likely, this method is subject to change in the future. Right now, it just returns the value,
        but probably in the future it will call a function that will move player to the next room.
        """
        match option_chosen:
            case "1":
                return self.options[0]
            case "2":
                return self.options[1]
            case "3":
                return self.options[2]
        return None
