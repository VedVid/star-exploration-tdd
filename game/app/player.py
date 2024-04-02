# -*- coding: utf-8 -*-


class Player:
    def __init__(self):
        self.room = None

    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room
