from room_types import *

# rooms
class RoomOne(RoomTypeN):
    pass


class RoomTwo(RoomTypeSW):
    pass


class RoomThree(RoomTypeNEW):
    pass


class RoomFour(RoomTypeESW):
    pass


class RoomFive(RoomTypeE):
    pass


class RoomSix(RoomTypeNS):
    pass


class RoomSeven(RoomTypeNW):
    pass


class RoomEight(RoomTypeE):
    pass


class RoomNine(RoomTypeS):
    pass


room1 = RoomOne()
room2 = RoomTwo(y=1)
room3 = RoomThree(x=-1, y=1)
room4 = RoomFour(x=-2, y=1)
room5 = RoomFive(x=-3, y=1)
room6 = RoomSix(x=-2)
room7 = RoomSeven(x=-2, y=-1)
room8 = RoomEight(x=-3, y=-1)
room9 = RoomNine(x=-1, y=2)


class RoomSwitching:
    def room_choosing(self):
        while True:
            if player.x == room1.x and player.y == room1.y:
                room1.type()
            elif player.x == room2.x and player.y == room2.y:
                room2.type()
            elif player.x == room3.x and player.y == room3.y:
                room3.type()
            elif player.x == room4.x and player.y == room4.y:
                room4.type()
            elif player.x == room5.x and player.y == room5.y:
                room5.type()
            elif player.x == room6.x and player.y == room6.y:
                room6.type()
            elif player.x == room7.x and player.y == room7.y:
                room7.type()
            elif player.x == room8.x and player.y == room8.y:
                room8.type()
            elif player.x == room9.x and player.y == room9.y:
                room9.type()


start = RoomSwitching()
start.room_choosing()