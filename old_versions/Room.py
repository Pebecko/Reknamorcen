from  main_funcs import *
from character_stats import player


class Room:
    def __init__(self, fight=False, health_potions=0, north=None, east=None, south=None, west=None):
        self.fight = fight
        self.health_potions = health_potions
        self.north = north
        self.east = east
        self.south = south
        self.west = west


# room patterns
class RoomPatternOne(Room):
    def room_pattern_one(self, new_dir, next_room):
        while True:
            if player.last_direction is None:
                slow_print("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
            else:
                slow_print("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
            direction_choice = base_options()
            if direction_choice != "skip":
                break

        player.last_direction = "{}".format(new_dir)

        return next_room


class RoomPatternTwo(Room):
    pass


class RoomPatternThree(Room):
    pass


# room types
class RoomTypeN(RoomPatternOne):
    def moving(self):
        self.room_pattern_one("north", self.north)


class RoomTypeS(RoomPatternOne):
    def moving(self):
        self.room_pattern_one("south", self.south)


class RoomTypeNE(RoomPatternTwo):
    pass


class RoomTypeNS(RoomPatternTwo):
    pass


class RoomTypeNES(RoomPatternThree):
    pass


class RoomTypeNEW(RoomPatternThree):
    pass


class RoomOne(RoomTypeN):
    pass


class RoomTwo(RoomTypeS):

    pass


room_one = RoomOne()
room_two = RoomTwo()

room_one.north = room_two
room_two.south = room_one

next_room = room_one.moving()
next_room.moving()
