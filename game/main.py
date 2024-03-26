# -*- coding: utf-8 -*-


from random import randint

from app.rooms_generation import RoomsGenerator


if __name__ == "__main__":
    rooms_generator = RoomsGenerator()
    print("\n*********\n")
    print("You boarded your brand-new Explorer-class starship.\nWhere will you go?\n")
    rooms = rooms_generator.generate_rooms(randint(1, 3))
    for i, room in enumerate(rooms):
        print(f"{i+1}) {room}")
