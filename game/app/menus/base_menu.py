# -*- coding: utf-8 -*-


class BaseMenu:
    """
    BaseMenu is class from which all other _Foo_Menu classes will inherit. It provides base functionalities.
    The main changes between BaseMenu and its children is handle_option method. Children will provide scene-specific
    implementation of this method, e.g. it could be JourneyMenu that maps options to desired destination.

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

    def __init__(self, header="", options=None):
        self.header = header
        self.options = options
        if self.options is None:
            self.options = []

    def set_header(self, header):
        """Sets menu's header."""
        self.header = header

    def set_options(self, options):
        """
        Sets menu's options.
        Takes list as argument and binds to self.options.
        """
        self.options = options

    @staticmethod
    def print_separator():
        """
        Prints separator at the top of the scene, to separate scenes from each other.
        No, we don't clear the screen in this game.
        """
        print("*********\n")

    def print_header(self):
        """Prints header in all caps."""
        print(f"{self.header.upper()}\n")

    def print_options(self):
        """Prints all options. Raises ValueError if list of options is empty."""
        if not self.options:
            raise ValueError("Non-empty list of options expected.")
        for index, option in enumerate(self.options, start=1):
            print(f"{index}) {option}")

    def take_input(self):
        v = input("> ")
        return v

    def handle_option(self, option_chosen):
        """
        Children of BaseMenu will use this method to handle options,
        by executing functions binded to the specific options.
        """
        raise NotImplementedError(
            "This is BaseMenu, handle_option method is not implemented here."
        )
