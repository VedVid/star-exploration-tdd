# -*- coding: utf-8 -*-


class BaseMenu:

    def __init__(self, header="", options=None):
        self.header = header
        self.options = options
        if self.options is None:
            self.options = []

    def set_header(self, header):
        self.header = header

    def set_options(self, *args):
        self.options = list(args)

    @staticmethod
    def print_separator():
        print("*********\n")

    def print_header(self):
        print(f"{self.header.capitalize()}\n")

    def print_options(self):
        if not self.options:
            raise ValueError("Non-empty list of options expected.")
        for index, option in enumerate(self.options, start=1):
            print(f"{index}) {option}\n")

    def handle_option(self):
        raise NotImplementedError("This is BaseMenu, handle_option method is not implemented here.")
