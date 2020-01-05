from room_types import RoomTypeE, RoomTypeES, RoomTypeESW, RoomTypeEW, RoomTypeN, RoomTypeNE, RoomTypeNES, \
    RoomTypeNESW, RoomTypeNES, RoomTypeNESW, RoomTypeNEW, RoomTypeNS, RoomTypeNSW, RoomTypeNW, RoomTypeS, RoomTypeSW, \
    RoomTypeW, Coordinates, Items


def room_choosing(player, world_map):
    while True:
        for room in world_map:
            if player.x == room.coordinates.x and player.y == room.coordinates.y and player.z == room.coordinates.z:
                room.type()
                break


# TODO Make the full map with all the levels
rooms = [RoomTypeN(),
         RoomTypeSW(Coordinates(y=1)),
         RoomTypeNEW(Coordinates(-1, 1), items=Items(1)),
         RoomTypeESW(Coordinates(-2, 1)),
         RoomTypeE(Coordinates(-3, 1), 2, Items(2)),
         RoomTypeNS(Coordinates(-2)),
         RoomTypeNW(Coordinates(-2, -1), 3),
         RoomTypeE(Coordinates(-3, -1)),
         RoomTypeS(Coordinates(-2, -1), 1)]
