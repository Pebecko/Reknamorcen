class Coordinates:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False


class Player:
    def __init__(self, coordinates=Coordinates(), direction="N"):
        self.coordinates = coordinates
        self.direction = direction


class Room:
    directions = ["N", "E", "S", "W"]
    direction_indexes = {None: 0, "N": 0, "D": 0, "U": 0, "E": 1, "S": 2, "W": 3}
    up = False
    down = False
    player = Player()
    one_exit = False

    def __init__(self, coordinates=Coordinates(), msg=""):
        self.coordinates = coordinates
        if msg == "":
            self.msg = "my coorinates: {}, {}, {}".format(self.coordinates.x, self.coordinates.y, self.coordinates.z)
        else:
            self.msg = msg
        self.possible_exits = [False, False, False, False]

    def moving(self, player):
        self.player = player

        print(self.msg)

        pl_index = self.direction_indexes[self.player.direction]

        pl_message = self.creating_player_message(pl_index)

        pl_option = input(pl_message)

        if (pl_option == "n" or self.one_exit) and self.up:
            self.move_up()
        elif (pl_option == "d" or self.one_exit) and self.down:
            self.move_down()
        elif (pl_option == "r" or self.one_exit) and self.possible_exits[pl_index]:
            self.player.direction = self.directions[pl_index]
            self.change_coordinates_in_direction()
        elif (pl_option == "p" or self.one_exit) and self.possible_exits[pl_index - 3]:
            self.player.direction = self.directions[pl_index - 3]
            self.change_coordinates_in_direction()
        elif (pl_option == "l" or self.one_exit) and self.possible_exits[pl_index - 1]:
            self.player.direction = self.directions[pl_index - 1]
            self.change_coordinates_in_direction()
        elif (pl_option == "z" or self.one_exit) and self.possible_exits[pl_index - 2]:
            self.player.direction = self.directions[pl_index - 2]
            self.change_coordinates_in_direction()

        return self.player

    def creating_player_message(self, pl_index):
        pl_message_parts = []

        if self.possible_exits[pl_index]:
            pl_message_parts.append("[r]ovně")
        if self.possible_exits[pl_index-3]:
            pl_message_parts.append("v[p]ravo")
        if self.possible_exits[pl_index-1]:
            pl_message_parts.append("v[l]evo")
        if self.possible_exits[pl_index-2]:
            if self.player.direction is None:
                pl_message_parts.append("v[z]ad")
            else:
                pl_message_parts.append("[z]pět")
        if self.up:
            if self.player.direction == "D":
                pl_message_parts.append("zpět [n]ahoru")
            else:
                pl_message_parts.append("[n]ahoru")
        if self.down:
            if self.player.direction == "U":
                pl_message_parts.append("zpět [d]olů")
            else:
                pl_message_parts.append("[d]olů")

        if len(pl_message_parts) > 1:
            pl_message = "Můžete jít"

            for index, direction in enumerate(pl_message_parts):
                pl_message += " " + direction

                if index == len(pl_message_parts) - 2:
                    pl_message += ", nebo"
                elif index == len(pl_message_parts) - 1:
                    pl_message += "."
                else:
                    pl_message += ","
        else:
            self.one_exit = True
            pl_message = "Můžete jít pouze {}, zmáčkněte enter až budete připraveni." \
                         "".format(pl_message_parts[0]).replace("[", "").replace("]", "")

        return pl_message

    def move_up(self):
        self.player.direction = "U"
        self.player.coordinates.z += 1

    def move_down(self):
        self.player.direction = "D"
        self.player.coordinates.z -= 1

    def change_coordinates_in_direction(self):
        if self.player.direction == "N":
            self.player.coordinates.x += 1
        elif self.player.direction == "E":
            self.player.coordinates.y += 1
        elif self.player.direction == "S":
            self.player.coordinates.x -= 1
        elif self.player.direction == "W":
            self.player.coordinates.y -= 1


player = Player()

coordinates = [Coordinates(),
               Coordinates(0, 0, 1),
               Coordinates(0, 0, -1),
               Coordinates(0, 1, 0),
               Coordinates(0, -1, 0),
               Coordinates(1, -1, 0),
               Coordinates(2, -1, 0),
               Coordinates(3, -1, 0),
               Coordinates(4, -1, 0),
               Coordinates(4, 0, 0)]

rooms = []
for coord in coordinates:
    room = Room(coord)

    for crd in coordinates:
        # N
        if crd.x == coord.x + 1 and crd.y == coord.y and crd.z == coord.z:
            room.possible_exits[0] = True

        # E
        if crd.x == coord.x and crd.y == coord.y + 1 and crd.z == coord.z:
            room.possible_exits[1] = True

        # S
        if crd.x == coord.x - 1 and crd.y == coord.y and crd.z == coord.z:
            room.possible_exits[2] = True

        # W
        if crd.x == coord.x and crd.y == coord.y - 1 and crd.z == coord.z:
            room.possible_exits[3] = True

        # U
        if crd.x == coord.x and crd.y == coord.y and crd.z == coord.z + 1:
            room.up = True

        # U
        if crd.x == coord.x and crd.y == coord.y and crd.z == coord.z - 1:
            room.down = True

    rooms.append(room)

_rooms = [Room(),
          Room(Coordinates(0, 0, 1)),
          Room(Coordinates(0, 0, -1)),
          Room(Coordinates(0, 1, 0)),
          Room(Coordinates(0, -1, 0))]

while True:
    for room in rooms:
        if player.coordinates == room.coordinates:
            player = room.moving(player)










#
# directions = ["N", "E", "S", "W"]
# possible_directions = [True, False, True, True]
# my_dir = "E"
#
# forward = False
# back = False
# left = False
# right = False
#
# frwd = 0
# lft = -1
# rght = -3
# bck = -2
#
# starting_index = directions.index(my_dir)
# if possible_directions[starting_index + frwd]:
#     print("f", True)
# if possible_directions[starting_index + lft]:
#     print("l", True)
# if possible_directions[starting_index + bck]:
#     print("b", True)
# if possible_directions[starting_index + rght]:
#     print("r", True)
