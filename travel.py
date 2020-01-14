from room_types import RoomTypeE, RoomTypeES, RoomTypeESW, RoomTypeEW, RoomTypeN, RoomTypeNE, RoomTypeNES, \
    RoomTypeNESW, RoomTypeNES, RoomTypeNESW, RoomTypeNEW, RoomTypeNS, RoomTypeNSW, RoomTypeNW, RoomTypeS, RoomTypeSW, \
    RoomTypeW
from coordinates import Coordinates
from items import Items
from main_funcs import slow_print, shutdown
from random import randint


def room_choosing(player, world_map):
    while True:
        remaining_opponents = 0
        for room in world_map:
            if player.coordinates.x == room.coordinates.x and player.coordinates.y == room.coordinates.y and \
                    player.coordinates.z == room.coordinates.z:
                room.type()
            if room.fight is not None:
                remaining_opponents += 1
        if remaining_opponents == 0:
            slow_print("Všichni jsou mrtví. Přežili jste, abyste mohli zemřít další den.")
            shutdown()


# TODO Make the full map with all the levels
# rooms = [RoomTypeN(),
#          RoomTypeSW(Coordinates(0, 1, 1)),
#          RoomTypeNEW(Coordinates(-1, 1, 1), items=Items(1)),
#          RoomTypeESW(Coordinates(-2, 1, 1), 0),
#          RoomTypeE(Coordinates(-3, 1, 1), 2, Items(randint(1, 2))),
#          RoomTypeNS(Coordinates(-2, 0, 1)),
#          RoomTypeNW(Coordinates(-2, -1, 1), 3),
#          RoomTypeE(Coordinates(-3, -1, 1)),
#          RoomTypeS(Coordinates(-2, -1, 1), 1)]

rooms = [RoomTypeNW(),
         RoomTypeESW(Coordinates(-1), 0),
         RoomTypeN(Coordinates(-1, -1)),
         RoomTypeEW(Coordinates(-2), 3),
         RoomTypeES(Coordinates(-3)),
         RoomTypeNS(Coordinates(-3, -1)),
         RoomTypeN(Coordinates(-3, -2)),
         RoomTypeNS(Coordinates(0, 1), 0),
         RoomTypeESW(Coordinates(0, 2), 2, Items(randint(0, 2))),
         RoomTypeNE(Coordinates(-1, 2)),
         RoomTypeNS(Coordinates(-1, 3), items=Items(randint(1, 2))),
         RoomTypeES(Coordinates(-1, 4)),
         RoomTypeEW(Coordinates(0, 4)),
         RoomTypeSW(Coordinates(1, 4), 1),
         RoomTypeNS(Coordinates(1, 3), items=Items(randint(0, 2))),
         RoomTypeNEW(Coordinates(1, 2)),
         RoomTypeESW(Coordinates(2, 2), 3),
         RoomTypeNS(Coordinates(2, 1), 2),
         RoomTypeN(Coordinates(2)),
         RoomTypeNEW(Coordinates(3, 2), 3),
         RoomTypeW(Coordinates(4, 2), 2),
         RoomTypeS(Coordinates(3, 3), 0, Items(randint(1, 3)))]
