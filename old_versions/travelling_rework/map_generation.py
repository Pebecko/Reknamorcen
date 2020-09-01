from random import randint
from os import system


class Coordinates:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


class Room:
    def __init__(self, coordinates=Coordinates()):
        self.coordinates = coordinates


x_size = 10
y_size = 6
z_size = 4
number_of_rooms = 80

rooms = []
while len(rooms) < number_of_rooms:
    rand_x = randint(0, x_size - 1)
    rand_y = randint(0, y_size - 1)
    rand_z = randint(0, z_size - 1)

    for room in rooms:
        if room.coordinates.x == rand_x and room.coordinates.y == rand_y and room.coordinates.z == rand_z:
            break
    else:
        rooms.append(Room(Coordinates(rand_x, rand_y, rand_z)))


def clearing_screen():
    system("cls")


def print_map(rooms, x, y, z):
    map_string = "    "
    for i in range(z):
        map_string += "level {}:".format(i + 1)
        map_string += " " * (3 * x)
    for y_cord in range(y):
        map_string += "\n"

        for z_cord in range(z):
            map_string += "        "
            for x_cord in range(x):
                for room in rooms:
                    if room.coordinates.x == x_cord and room.coordinates.y == y_cord and room.coordinates.z == z_cord:
                        map_string += "_X_"
                        break
                else:
                    map_string += "_-_"

    print(map_string)


print_map(rooms, x_size, y_size, z_size)
