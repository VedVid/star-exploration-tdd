# -*- coding: utf-8 -*-


class BaseMenu:

    options = []

    def print_options(self):
        if not self.options:
            raise ValueError("Non-empty list of options expected.")
