import random
import time
import sys


x = 0
y = 0
last_direction = None

def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    print("")
    time.sleep(0.02)


class Walk:
    def __init__(self):
        pass
        self.x = x
        self.y = y
        self.last_direction = last_direction

    def room_picking(self, x, y, last_direction):
        while True:
            if x == 0 and y == 0:
                coordinates = self.room_one(x, y, last_direction)
            elif x == 0 and y == 1:
                coordinates = self.room_two(x, y, last_direction)

            x = coordinates[0]
            y = coordinates[1]
            last_direction = coordinates[2]

    def get_coordinates(self, x, y, last_direction):
        if last_direction == "North":
            y -= 1
        elif last_direction == "East":
            x += 1
        elif last_direction == "South":
            y += 1
        elif last_direction == "West":
            x -= 1
        return [x, y]

    def room_type_n(self, x, y, last_direction):
        if last_direction is None:
            slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
            input()
    
        elif last_direction == "South":
            slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
            input()
    
        last_direction = "North"
        coordinates = getCoordinates(x, y, last_direction)
        x = coordinates[0]
        y = coordinates[-1]
        return [x, y, last_direction]

    def room_type_s(self, x, y, last_direction):
        if last_direction is None:
            slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
            input()
    
        elif last_direction == "North":
            slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
            input()

        last_direction = "South"
        coordinates = getCoordinates(x, y, last_direction)
        x = coordinates[0]
        y = coordinates[-1]
        return [x, y, last_direction]

    def room_one(self, x, y, last_direction):
        coordinates = self.room_type_s(x, y, last_direction)

        return coordinates[0, 1, 2]

    def room_two(self, x, y, last_direction):
        coordinates = self.room_type_m(x, y, last_direction)

        return coordinates[0, 1, 2]


walk_1 = Walk()
print(walk_1.get_coordinates())

input("Press enter to exit.")
