# -*- coding: utf-8 -*-


class BaseMenu:

    def __init__(self, options=None):
        self.options = options
        if self.options is None:
            self.options = []

    def print_options(self):
        if not self.options:
            raise ValueError("Non-empty list of options expected.")
