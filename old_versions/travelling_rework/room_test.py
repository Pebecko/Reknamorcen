from random import randint, choice, seed, sample
from os import system
from pathfinding import Pathfinder

# TODO - eventually remove coordinates from displaying
# TODO - add possibility of more players and AI movement

# TODO - put the map size into some settings accessible before the game start
x_size = 11
y_size = 11
levels = 2
# z_size = levels * 2 - 1
# number_of_rooms = x_size * y_size * z_size
show = False


class Item:
    def __init__(self, name):
        self.name = name

    def selected(self, kwargs):
        if kwargs["method"] == "drop":
            kwargs["room"].items.append(self)
            kwargs["player"].dropping_items(self)
        elif kwargs["method"] == "pickup":
            kwargs["room"].items.remove(self)
            kwargs["player"].picking_items(self, kwargs["room"])


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

    def __str__(self):
        return "x: {} y: {} z: {}".format(self.x, self.y, self.z)

    def make_copy(self):
        return Coordinates(self.x, self.y, self.z)


class Weapon(Item):
    def __init__(self, name="", mine=False, destroy_obstacles=False):
        super().__init__(name)
        self.mine = mine
        self.destroy_obstacles = destroy_obstacles


class Key(Item):
    def __init__(self, name):
        super().__init__(name)


class Character:
    def __init__(self, coordinates=Coordinates(), direction=None):
        self.map_symbol = "C"
        self.coordinates = coordinates
        self.direction = direction
        self.player_controlled = False
        self.visited_rooms = []
        self.goal = None

    def main(self):
        for room in rooms:
            if room.coordinates == self.coordinates:
                self.direction = room.pathfinder.parent_direction
                self.change_coordinates_in_direction()
                break

    def move(self, direction):
        self.direction = direction
        self.change_coordinates_in_direction()

    def change_coordinates_in_direction(self):
        # maybe use dictionary here
        if self.direction == "N":
            self.coordinates.y -= 1
        elif self.direction == "E":
            self.coordinates.x += 1
        elif self.direction == "S":
            self.coordinates.y += 1
        elif self.direction == "W":
            self.coordinates.x -= 1
        elif self.direction == "U":
            self.coordinates.z += 1
        elif self.direction == "D":
            self.coordinates.z -= 1

    def teleport(self, coordinates):
        self.direction = None
        self.coordinates = coordinates.make_copy()

    def finding_goal(self):
        # TODO - finish this
        self.goal = Coordinates(player.coordinates.x, player.coordinates.y, player.coordinates.z)


class Player(Character):
    def __init__(self, coordinates=Coordinates(), direction=None):
        super().__init__(coordinates, direction)

        self.player_controlled = True
        weapon = Weapon("pick", True, True)
        self.unarmed_weapon = Weapon("fists")
        self.weapon = self.unarmed_weapon
        self.items = []
        if self.weapon is not self.unarmed_weapon:
            self.items.append(weapon)

    def dropping_items(self, item):
        self.items.remove(item)

        if self.weapon is item:
            self.weapon = self.unarmed_weapon

    def picking_items(self, item, room):
        self.items.append(item)

        if isinstance(item, Weapon):
            if self.weapon is not self.unarmed_weapon:
                self.items.remove(self.weapon)
                room.items.append(self.weapon)
            self.weapon = item


class Group:
    def __init__(self, members=None):
        self.members = []
        if members is not None:
            self.members = members

    def move(self, direction):
        for member in self.members:
            member.move(direction)

    def teleport(self, coordinates):
        for member in self.members:
            member.teleport(coordinates)


class Room:
    directions = ["N", "E", "S", "W"]
    direction_indexes = {None: 0, "N": 0, "D": 0, "U": 0, "E": 1, "S": 2, "W": 3}
    group = Group()
    player = Player()
    player_decides = False
    one_exit = False
    visited = False
    direction_index = 0

    def __init__(self, coordinates=Coordinates(), msg="", items=None):
        self.coordinates = coordinates
        self.pathfinder = Pathfinder()
        self.possible_exits = [False, False, False, False, False, False]
        self.obstacles = {"N": None, "E": None, "S": None, "W": None, "U": None, "D": None}
        self.items = []
        if items is not None:
            self.items = items
        # TODO - add room size, faction...

        # TODO - add creating room description here
        if msg == "":
            self.msg = msg
            # self.msg = "my coordinates: x {}, y {}, z {}".format(self.coordinates.x, self.coordinates.y,
            #                                                      self.coordinates.z)
        else:
            self.msg = msg

    def main(self, group):
        self.group = group
        self.player_decides = False

        for character in self.group.members:
            character.visited_rooms.append(self)
            if character.player_controlled:
                self.player_decides = True
                self.player = character

        self.room_actions()

    def room_actions(self):
        if self.player_decides:
            self.updating_direction_index()

            return self.picking_action(self.finding_possible_actions())
        else:
            return self.ai_movement()

    def updating_direction_index(self):
        self.direction_index = self.direction_indexes[self.player.direction]

    def finding_possible_actions(self):
        possible_actions = []

        possible_actions = self.finding_removable_obstacles(possible_actions)
        possible_actions = self.finding_item_actions(possible_actions)
        possible_actions = self.finding_possible_movement(possible_actions)

        return possible_actions

    def finding_removable_obstacles(self, possible_actions):
        directions = ["před vámi", "nalevo od vás", "za vámi", "napravo od vás", "nad vámi", "pod vámi"]

        for index, direction in enumerate(directions):
            if index < 4:
                obstacle = list(self.obstacles.values())[:4][self.direction_index - index]
            else:
                obstacle = list(self.obstacles.values())[index]

            try:
                if obstacle.is_removable(self.player):
                    if index < 4:
                        obstacle_direction = list(self.obstacles.keys())[:4][self.direction_index - index]
                    else:
                        obstacle_direction = list(self.obstacles.keys())[index]
                    for message in obstacle.creating_remove_message(self.player, direction):
                        possible_actions.append([obstacle,
                                                 {"room": self, "player": self.player,
                                                  "direction": obstacle_direction,
                                                  "method": message["method"]},
                                                 message["message"]])
            except AttributeError:
                pass

        return possible_actions

    def finding_item_actions(self, possible_actions):
        for item in self.items + self.player.items:
            possible_actions.append([item,
                                    {"room": self, "player": self.player,
                                     "method": "drop" if item in self.player.items else "pickup"},
                                    "zvednout {} ze země".format(item.name) if item in self.items else "položit {} na zem".format(item.name)])
        return possible_actions

    def finding_possible_movement(self, possible_actions):
        existing_directions = [{"offset": 0, "message": "jít [r]ovně", "key": "r"},
                               {"offset": 1, "message": "jít v[l]evo", "key": "l"},
                               {"offset": 2, "message": "jít [z]pět", "key": "z", "second_message": "jít v[z]ad"},
                               {"offset": 3, "message": "jít v[p]ravo", "key": "p"}]

        for direction in existing_directions:
            if self.possible_exits[:4][self.direction_index - direction["offset"]]:
                message = direction["message"]
                if direction.get("second_message") is not None and \
                        (self.player.direction is None or self.player.direction is "U" or self.player.direction is "D"):
                    message = direction["second_message"]
                try:
                    if not list(self.obstacles.values())[:4][self.direction_index - direction["offset"]].locked and \
                            list(self.obstacles.values())[:4][self.direction_index - direction["offset"]].unlockable:
                        raise AttributeError
                except AttributeError:
                    possible_actions.append([self, {"group": self.group,
                                                    "direction": self.directions[self.direction_index - direction["offset"]],
                                                    "own_key": direction["key"]}, message])

        if self.possible_exits[4]:
            try:
                if self.obstacles["U"].unlockable and not self.obstacles["U"].locked:
                    raise AttributeError
            except AttributeError:
                if self.player.direction == "D":
                    possible_actions.append([self, {"group": self.group, "direction": "U", "own_key": "n"},
                                             "jít zpět [n]ahoru"])
                else:
                    possible_actions.append([self, {"group": self.group, "direction": "U", "own_key": "n"},
                                             "jít [n]ahoru"])
        if self.possible_exits[5]:
            try:
                if self.obstacles["D"].unlockable and not self.obstacles["D"].locked:
                    raise AttributeError
            except AttributeError:
                if self.player.direction == "U":
                    possible_actions.append([self, {"group": self.group, "direction": "D", "own_key": "d"},
                                             "jít zpět [d]olů"])
                else:
                    possible_actions.append([self, {"group": self.group, "direction": "D", "own_key": "d"},
                                             "jít [d]olů"])


        return possible_actions

    def picking_action(self, possible_actions):
        map_printing()

        print(self.msg, self.creating_obstacle_message())  # , self.obstacles)

        while True:
            pl_message = "Můžete"

            for index, action in enumerate(possible_actions):
                if action[1].get("own_key") is not None:
                    pl_message += " "
                else:
                    pl_message += " [{}] ".format(index + 1)
                pl_message += action[2]

                if index == len(possible_actions) - 2:
                    pl_message += ", nebo"
                elif index == len(possible_actions) - 1:
                    pl_message += ".\n"
                else:
                    pl_message += ","
            if len(pl_message) < 10:
                pl_message = "Nemůžete nic dělat, máte smůlu.\n"

            player_option = input(pl_message)

            # TODO - put checking for these commands somewhere else
            # TODO - add possibility to show and hide unvisited rooms (cheat command)
            if player_option == "0":
                map_printing(0)
            elif player_option == "1":
                map_printing(1)
            elif player_option == "2":
                map_printing(2)
            elif player_option == "3":
                map_printing(3)
            elif player_option == "4":
                map_printing(4)
            if player_option == "show":
                global show
                show = not show
                clearing_screen()
                return self.picking_action(possible_actions)
            elif player_option == "tp":
                return teleport(self.player)

            for action in possible_actions:
                if action[1].get("own_key") == player_option:
                    return action[0].selected(action[1])
            try:
                if int(player_option) in range(1, len(possible_actions) + 1) and \
                        possible_actions[int(player_option) - 1][1].get("own_key") is None:
                    possible_actions[int(player_option) - 1][0].selected(possible_actions[int(player_option) - 1][1])
                    clearing_screen()
                    return self.room_actions()
                else:
                    raise ValueError
            except ValueError:
                print("wrong input")

    def creating_obstacle_message(self):
        message = "\n"

        for obstacle_key, obstacle_value in self.obstacles.items():
            try:
                if obstacle_value.locked is False and obstacle_value.unlockable:
                    raise AttributeError
            except AttributeError:
                pass
            else:
                if obstacle_key == list(self.obstacles.keys())[:4][self.direction_index]:
                    message += "Před vámi"
                elif obstacle_key == list(self.obstacles.keys())[:4][self.direction_index - 3]:
                    message += "Napravo od vás"
                elif obstacle_key == list(self.obstacles.keys())[:4][self.direction_index - 1]:
                    message += "Nalevo od vás"
                elif obstacle_key == list(self.obstacles.keys())[:4][self.direction_index - 2]:
                    message += "Za vámi"
                elif obstacle_key == "U":
                    message += "Nad vámi"
                elif obstacle_key == "D":
                    message += "Pod vámi"
                message += " {} {}. ".format(obstacle_value.verb, obstacle_value.translation)
        if message != "\n":
            message += "Nemůžete projít."

        return message

    def ai_movement(self):
        if self.group.members[0].goal is None or self.group.members[0].goal == self.coordinates:
            self.group.members[0].finding_goal()

        pathfinding(self.group.members[0].goal)

        self.selected({"group": self.group, "direction": self.pathfinder.parent_direction})

    def selected(self, kwargs):
        kwargs["group"].move(kwargs["direction"])


class Obstacle:
    unlock_message = "odemknout"
    lock_message = "zamknout"
    mine_message = "vykopat"
    batter_message = "rozmlátit"

    def __init__(self, name="", verb="", translation="", map_symbol="O", unlockable=False, mineable=False,
                 batterable=False, keys=None):
        self.name = name
        self.verb = verb
        self.translation = translation
        self.map_symbol = map_symbol
        self.unlockable = unlockable
        self.locked = False
        self.keys = []
        if self.unlockable:
            self.locked = True
            if keys is not None:
                self.keys = keys
        self.mineable = mineable
        self.batterable = batterable

    def is_removable(self, _player):
        for item in _player.items:
            if (item in self.keys) and self.unlockable:
                return True
        if player.weapon.mine and self.mineable:
            return True
        elif _player.weapon.destroy_obstacles and self.batterable:
            return True

        return False

    def creating_remove_message(self, _player, direction):
        remove_message = []

        for item in _player.items:
            if (item in self.keys) and self.unlockable:
                if self.locked:
                    remove_message.append({"message": "{} {} {}".format(self.unlock_message, self.translation, direction),
                                           "method": "unlock"})
                    break
                else:
                    remove_message.append({"message": "{} {} {}".format(self.lock_message, self.translation, direction),
                                           "method": "lock"})
                    break
        if _player.weapon.mine and self.mineable:
            remove_message.append({"message": "{} {} {}".format(self.mine_message, self.translation, direction),
                                   "method": "remove"})
        if _player.weapon.destroy_obstacles and self.batterable:
            remove_message.append({"message": "{} {} {}".format(self.batter_message, self.translation, direction),
                                   "method": "remove"})

        return remove_message

    def selected(self, kwargs):
        if kwargs["method"] == "unlock":
            self.locked = False
            # kwargs["room"].obstacles[kwargs["direction"]].locked = False
            finding_coordinates(kwargs["room"].coordinates, rooms, kwargs["direction"])[0].obstacles[
                inverse_direction(kwargs["direction"])].locked = False
        elif kwargs["method"] == "lock":
            self.locked = True
            # kwargs["room"].obstacles[kwargs["direction"]].locked = True
            finding_coordinates(kwargs["room"].coordinates, rooms, kwargs["direction"])[0].obstacles[
                inverse_direction(kwargs["direction"])].locked = True
        elif kwargs["method"] == "remove":
            kwargs["room"].obstacles[kwargs["direction"]] = None
            finding_coordinates(kwargs["room"].coordinates, rooms, kwargs["direction"])[0].obstacles[
                inverse_direction(kwargs["direction"])] = None


def clearing_screen():
    system("cls")


def rooms_on_level(z_level):
    count = 0

    for room in rooms:
        if room.coordinates.z == z_level:
            count += 1

    return count


def finding_coordinates(base_coordinates, to_search, *directions, give_items=True):
    results = []

    for direction in directions:
        searched_coordinate = base_coordinates.make_copy()
        # maybe use a dictionary with corresponding x and y movement according to current direction
        for letter in direction:
            if letter.casefold() == "n":
                searched_coordinate.y -= 1
            elif letter.casefold() == "e":
                searched_coordinate.x += 1
            elif letter.casefold() == "s":
                searched_coordinate.y += 1
            elif letter.casefold() == "w":
                searched_coordinate.x -= 1
            elif letter.casefold() == "u":
                searched_coordinate.z += 1
            elif letter.casefold() == "d":
                searched_coordinate.z -= 1

        for item in to_search:
            if isinstance(item, Room):
                if item.coordinates == searched_coordinate:
                    if give_items:
                        results.append(item)
                    else:
                        results.append(True)
                    break
            elif isinstance(item, Coordinates):
                if item == searched_coordinate:
                    if give_items:
                        results.append(item)
                    else:
                        results.append(True)
                    break
        else:
            if give_items:
                results.append(None)
            else:
                results.append(False)

    return results


# TODO - split this up into seperate functions
def map_printing(level=-1):
    if level == -1:
        level = player.coordinates.z
    map_string = "\nLevel {}:".format(level)
    map_string += "\n          "
    for x_coordinate in range(x_size):
        map_string += "x {}  ".format(x_coordinate)
        if x_coordinate < 10:
            map_string += " "
    for y_coordinate in range(y_size):
        top_line = "       "
        bottom_line = "   y {}".format(y_coordinate)
        if y_coordinate < 10:
            bottom_line += " "
        for x_coordinate in range(x_size):
            top_line += "   "
            for room in rooms:
                if room.coordinates == Coordinates(x_coordinate, y_coordinate, level):
                    if not room.possible_exits[5] and (room in player.visited_rooms or show):
                        room_left = "["
                    elif (room in player.visited_rooms or show) and room.obstacles["D"] is not None:
                        room_left = room.obstacles.get("D").map_symbol
                    elif room in player.visited_rooms or show:
                        room_left = "\\"
                    else:
                        room_left = " "

                    if not room.possible_exits[4] and (room in player.visited_rooms or show):
                        room_right = "]"
                    elif (room in player.visited_rooms or show) and room.obstacles["U"] is not None:
                        room_right = room.obstacles.get("U").map_symbol
                    elif room in player.visited_rooms or show:
                        room_right = "/"
                    else:
                        room_right = " "

                    north_visited = False
                    for rm in rooms:
                        if rm.coordinates.x == room.coordinates.x and rm.coordinates.y + 1 == room.coordinates.y and \
                                rm.coordinates.z == room.coordinates.z:
                            if rm in player.visited_rooms or show:
                                north_visited = True
                            break
                    if room.possible_exits[0] and (room in player.visited_rooms or show or north_visited):
                        if room.obstacles.get("N") is not None:
                            top_line += " {} ".format(room.obstacles.get("N").map_symbol)
                        else:
                            top_line += " | "
                    else:
                        top_line += "   "

                    west_visited = False
                    for rm in rooms:
                        if rm.coordinates.x + 1 == room.coordinates.x and rm.coordinates.y == room.coordinates.y and \
                                rm.coordinates.z == room.coordinates.z:
                            if rm in player.visited_rooms or show:
                                west_visited = True
                            break
                    if room.possible_exits[3] and (room in player.visited_rooms or show or west_visited):
                        if room.obstacles.get("W") is not None:
                            bottom_line += " {} ".format(room.obstacles.get("W").map_symbol)
                        else:
                            bottom_line += " - "
                    else:
                        bottom_line += "   "

                    for group in all_groups:
                        if player not in group.members:
                            if room.coordinates == player.coordinates and player.coordinates == group.members[0].coordinates:
                                room_middle = "X"
                                break
                            elif room.coordinates == group.members[0].coordinates:
                                room_middle = group.members[0].map_symbol
                                break
                    else:
                        if room.coordinates == player.coordinates:
                            if player.direction == "E":
                                room_middle = ">"
                            elif player.direction == "S":
                                room_middle = "v"
                            elif player.direction == "W":
                                room_middle = "<"
                            else:
                                room_middle = "^"
                        elif room.items and (room in player.visited_rooms or show):
                            room_middle = "i"
                        # pathfind debug
                        # elif room in player.visited_rooms or show:
                        #     if room.pathfinder.distance >= 99:
                        #         room_middle = "?"
                        #     elif room.pathfinder.distance < 10:
                        #         room_middle = str(room.pathfinder.distance)
                        #     else:
                        #         room_middle = " "
                        else:
                            room_middle = " "
                    bottom_line += "{}{}{}".format(room_left, room_middle, room_right)
                    break
            else:
                top_line += "   "
                bottom_line += "      "
        map_string += top_line + "\n" + bottom_line + "\n"

    print(map_string)


# older version of printing map useful for testing purposes
def old_print_map(_rooms, _player, x, y, z):
    map_string = "    "
    for i in range(z):
        map_string += "level {}:".format(i)
        map_string += " " * (3 * x)
    for y_cord in range(y):
        map_string += "\n"

        for z_cord in range(z):
            map_string += "        "
            for x_cord in range(x):
                for room in _rooms:
                    if Coordinates(x_cord, y_cord, z_cord) == _player.coordinates:
                        if player.direction == "E":
                            player_dir = ">"
                        elif player.direction == "S":
                            player_dir = "v"
                        elif player.direction == "W":
                            player_dir = "<"
                        else:
                            player_dir = "^"
                        map_string += "_{}_".format(player_dir)
                        break
                    if room.coordinates == Coordinates(x_cord, y_cord, z_cord):
                        map_string += "_X_"
                        break
                else:
                    map_string += "_._"
    print(map_string)


def getting_seed():
    while True:
        player_option = input("Přejete si [z]adat seed mapy, nebo ho [v]ygenerovat automaticky?\n")

        if player_option == "z":
            seed(input("Zadejte seed:\n"))
            return
        elif player_option == "v":
            game_seed = randint(100_000_000_000, 999_999_999_999)
            print("Váš seed je:", game_seed)
            seed(str(game_seed))
            return


def teleport(item, x=-1, y=-1, z=-1):
    coordinates = [x, y, z]
    limits = [x_size, y_size, levels]

    for index, coordinate in enumerate(coordinates):
        while coordinate == -1:
            player_option = input("input coordinate number {}: ".format(index + 1))
            try:
                if int(player_option) in range(limits[index]):
                    coordinates[index] = int(player_option)
                    break
                else:
                    print("not possible to teleport here")
            except ValueError:
                print("wrong input")
    try:
        item.teleport(Coordinates(*coordinates))
    except AttributeError:
        item.coordinates.x = coordinates[0]
        item.coordinates.y = coordinates[1]
        item.coordinates.z = coordinates[2]

    try:
        item.direction = None
    except AttributeError:
        pass

    return


def inverse_direction(direction):
    directions = ["N", "S", "E", "W", "U", "D"]

    try:
        if directions.index(direction) % 2 == 0:
            return directions[directions.index(direction) + 1]
        else:
            return directions[directions.index(direction) - 1]
    except ValueError:
        pass


def pathfinding(coordinates=Coordinates(), ignore_obstacles=False):
    active_parents = []
    directions = ["N", "S", "E", "W", "U", "D"]

    # resetting previous pathfind
    for room in rooms:
        room.pathfinder.resetting()

        if room.coordinates == coordinates:
            room.pathfinder.distance = 0
            active_parents.append(room)

    while True:
        new_parents = []
        for parent in active_parents:
            exit_directions = []
            for direction, possible_exit in zip(parent.directions, parent.possible_exits):
                if possible_exit and (ignore_obstacles or parent.obstacles[direction] is None):
                    exit_directions.append(direction)
            adjacent_rooms = finding_coordinates(parent.coordinates, rooms, *exit_directions)
            for index, adjacent_room in enumerate(adjacent_rooms):
                if adjacent_room is not parent.pathfinder.parent and adjacent_room is not None:
                    if adjacent_room.pathfinder.distance > parent.pathfinder.distance + 1:
                        new_parents.append(adjacent_room)
                        adjacent_room.pathfinder.distance = parent.pathfinder.distance + 1
                        adjacent_room.pathfinder.parent = parent
                        if index % 2 == 0:
                            adjacent_room.pathfinder.parent_direction = directions[index + 1]
                        else:
                            adjacent_room.pathfinder.parent_direction = directions[index - 1]
        if not new_parents:
            return
        else:
            active_parents = new_parents


# getting_seed()

# new map generation
all_coordinates = []
for level_num in range(levels):
    level = []
    max_number_of_rooms = randint((x_size * y_size) // (3 / 1), (x_size * y_size) // (5 / 3))
    possible_additions = [Coordinates(randint(0, x_size - 1), randint(0, y_size - 1), level_num)]

    while (len(level) < max_number_of_rooms) or (not possible_additions):
        new_coordinates = choice(possible_additions)

        if False in finding_coordinates(new_coordinates, level, "n", "ne", "e", give_items=False) and \
                False in finding_coordinates(new_coordinates, level, "e", "se", "s", give_items=False) and \
                False in finding_coordinates(new_coordinates, level, "s", "sw", "w", give_items=False) and \
                False in finding_coordinates(new_coordinates, level, "w", "nw", "n", give_items=False):
            level.append(new_coordinates)

            possible_new_coordinates = [Coordinates(new_coordinates.x - 1, new_coordinates.y, level_num),
                                        Coordinates(new_coordinates.x, new_coordinates.y - 1, level_num),
                                        Coordinates(new_coordinates.x + 1, new_coordinates.y, level_num),
                                        Coordinates(new_coordinates.x, new_coordinates.y + 1, level_num)]

            for coordinates in level + possible_additions:
                for cord in possible_new_coordinates:
                    if cord.x < 0 or cord.x >= x_size or cord.y < 0 or cord.y >= y_size:
                        possible_new_coordinates.remove(cord)
                        break
                    if coordinates == cord:
                        possible_new_coordinates.remove(cord)
                        break
            possible_additions = possible_additions + possible_new_coordinates

        possible_additions.remove(new_coordinates)

    else:
        all_coordinates = all_coordinates + level

# shrinking map only to used size
x_min = x_size
x_max = 0
y_min = y_size
y_max = 0
for coordinates in all_coordinates:
    if coordinates.x < x_min:
        x_min = coordinates.x
    if coordinates.x > x_max:
        x_max = coordinates.x

    if coordinates.y < y_min:
        y_min = coordinates.y
    if coordinates.y > y_max:
        y_max = coordinates.y

# print(x_min, x_max, y_min, y_max)
for coordinates in all_coordinates:
    coordinates.x -= x_min
    coordinates.y -= y_min

x_size = x_max - x_min + 1
y_size = y_max - y_min + 1

# random map generation
# all_coordinates = []
# while len(all_coordinates) < number_of_rooms:
#     rand_x = randint(0, x_size - 1)
#     rand_y = randint(0, y_size - 1)
#     rand_z = randint(0, z_size - 1)
#
#     for coordinate in all_coordinates:
#         if coordinate.x == rand_x and coordinate.y == rand_y and coordinate.z == rand_z:
#             break
#     else:
#         all_coordinates.append(Coordinates(rand_x, rand_y, rand_z))

# handmade map for testing purposes
# all_coordinates = [Coordinates(1, 1, 1),
#                    Coordinates(1, 1, 2),
#                    Coordinates(1, 1, 0),
#                    Coordinates(1, 2, 1),
#                    Coordinates(0, 1, 2),
#                    Coordinates(2, 1, 2),
#                    Coordinates(1, 0, 1)]

# removing redundant coordinates
# num = 0
# while num < len(all_coordinates):
#     coordination = all_coordinates[num]
#
#     if False not in finding_coordinates(coordination, all_coordinates, "n", "nw", "w", give_items=False):
#         all_coordinates.remove(choice(finding_coordinates(coordination, all_coordinates, "", "n", "nw", "w")))
#     else:
#         num += 1

# creating passages on odd levels
# transit_levels_passages = []
# for i in range(z_size):
#     if i % 2 == 1:
#         transit_levels_passages.append([i, randint(2, 4), 0])
# num = 0
# while num < len(all_coordinates):
#     coordination = all_coordinates[num]
#
#     for level in transit_levels_passages:
#         if coordination.z == level[0]:
#             if level[1] <= level[2]:
#                 all_coordinates.remove(coordination)
#             else:
#                 # TODO - remove this mess
#                 if (False not in finding_coordinates(coordination, all_coordinates, "u", "d", give_items=False)) \
#                         and (level[1] > level[2]) and \
#                         ((False in finding_coordinates(coordination, all_coordinates, "n", "nu", "nd", give_items=False)) and
#                          (False in finding_coordinates(coordination, all_coordinates, "e", "eu", "ed", give_items=False)) and
#                          (False in finding_coordinates(coordination, all_coordinates, "s", "su", "sd", give_items=False)) and
#                          (False in finding_coordinates(coordination, all_coordinates, "w", "wu", "wd", give_items=False))):
#                     level[2] += 1
#                     num += 1
#                 else:
#                     all_coordinates.remove(coordination)
#             break
#     else:
#         num += 1

rooms = []

# connecting rooms
for coord in all_coordinates:
    rooms.append(Room(coord))

    for crd in all_coordinates:
        # N
        if crd.x == coord.x and crd.y == coord.y - 1 and crd.z == coord.z:
            rooms[-1].possible_exits[0] = True

        # E
        elif crd.x == coord.x + 1 and crd.y == coord.y and crd.z == coord.z:
            rooms[-1].possible_exits[1] = True

        # S
        elif crd.x == coord.x and crd.y == coord.y + 1 and crd.z == coord.z:
            rooms[-1].possible_exits[2] = True

        # W
        elif crd.x == coord.x - 1 and crd.y == coord.y and crd.z == coord.z:
            rooms[-1].possible_exits[3] = True

        # # U
        # elif crd.x == coord.x and crd.y == coord.y and crd.z == coord.z + 1:
        #     rooms[-1].up = True
        #
        # # D
        # elif crd.x == coord.x and crd.y == coord.y and crd.z == coord.z - 1:
        #     rooms[-1].down = True

# new game generation
# spawning player
for room in sample(rooms, len(rooms)):
    if (room.coordinates.x < 3 or room.coordinates.y < 3) and room.coordinates.z == levels - 1:
        player = Player(coordinates=room.coordinates.make_copy())
        break
else:
    print("unable to spawn player")

pathfinding(player.coordinates)
key = Key("klíč 1")

# choice(rooms).items.append(key)
# generating stairs
for room in sample(rooms, len(rooms)):
    # if room.coordinates.x >= 7 and room.coordinates.y >= 7 and room.coordinates.z == levels - 1 and \
    #         None not in finding_coordinates(room.coordinates, rooms, "d"):
    if room.pathfinder.distance > (x_size + y_size) // 3 and room.coordinates.z == levels - 1 and \
            None not in finding_coordinates(room.coordinates, rooms, "d"):
        obstacle = Obstacle("metal_door", "jsou", "okované dveře", "Đ", True, False, False)
        obstacle.keys = [key]
        room.obstacles["D"] = obstacle
        room.possible_exits[5] = True
        finding_coordinates(room.coordinates, rooms, "d")[0].obstacles["U"] = obstacle
        finding_coordinates(room.coordinates, rooms, "d")[0].possible_exits[4] = True
        break
else:
    print("unable to create downward passage")

pathfinding(player.coordinates)
key_room = None
# spawning key
for room in sample(rooms, len(rooms)):
    # if (7 > room.coordinates.x > 3 and 7 > room.coordinates.y > 3) and room.coordinates.z == levels - 1:
    if 99 > room.pathfinder.distance > (x_size + y_size) // 4:
        room.items.append(key)
        key_room = room
        break
else:
    print("unable to spawn key")

player_group = Group([player])
all_groups = [player_group]  # , group_1, group_2]

# spawning wooden doors
while True:
    pathfinding(player.coordinates)
    if key_room.pathfinder.distance >= 99:
        break
    pathfinding(key_room.coordinates)
    for room in sample(rooms, len(rooms)):
        if 5 > room.pathfinder.distance > 2:
            for direction, possible_exit in zip(room.directions, room.possible_exits):
                if possible_exit and randint(0, 1) == 1 and room.obstacles[direction] is None:
                    obstacle = Obstacle("wooden_door", "jsou", "dřevěné dveře", "D", True, False, True)
                    obstacle.keys.append(key)
                    room.obstacles[direction] = obstacle
                    finding_coordinates(room.coordinates, rooms, direction
                                        )[0].obstacles[inverse_direction(direction)] = obstacle
                    break
            break

# spawning axe
for room in sample(rooms, len(rooms)):
    if 99 > room.pathfinder.distance > 2:
        room.items.append(Weapon("sekyra", False, True))
        break
else:
    print("unable to spawn axe")

# # generating keys
# all_keys = []
# for num in range(randint(3, 5)):
#     all_keys.append(Key("klíč " + str(num + 1)))

# generating obstacles
# obstacle_directions = ["N", "E", "S", "W", "U", "D"]
# obstacle_types = [("rubble", "jsou", "sutiny v cestě", "%", False, True, False),
#                   ("wooden_door", "jsou", "dřevěné dveře", "D", True, False, True),
#                   ("metal_door", "jsou", "okované dveře", "Đ", True, False, False)]
# for room in rooms:
#     if randint(0, 5) == 0:
#         direction = choice(obstacle_directions)
#         obstacle = Obstacle(*choice(obstacle_types))
#         obstacle.keys = sample(all_keys, randint(1, len(all_keys)))
#         if room.obstacles[direction] is None and \
#             (room.possible_exits[Room.direction_indexes[direction]] and (direction not in ["U", "D"]) or
#                 direction == "U" and room.up or direction == "D" and room.down):
#             room.obstacles.update({direction: obstacle})
#             finding_coordinates(room.coordinates, rooms, direction)[0].obstacles.update({inverse_direction(direction): obstacle})
# r_num = randint(0, len(rooms) - 1)
# character = Character(coordinates=Coordinates(rooms[r_num].coordinates.x, rooms[r_num].coordinates.y, rooms[r_num].coordinates.z))
# r_num = randint(0, len(rooms) - 1)
# char = Character(coordinates=Coordinates(rooms[r_num].coordinates.x, rooms[r_num].coordinates.y, rooms[r_num].coordinates.z))
# char.map_symbol = "G"
# player = Player(coordinates=Coordinates(rooms[0].coordinates.x, rooms[0].coordinates.y, rooms[0].coordinates.z))
# group_1 = Group([character])
# group_2 = Group([char])
# rooms[0].visited = True
# for key in all_keys:
#     choice(rooms).items.append(key)
# choice(rooms).items.append(Weapon("sekyra", False, True))
# choice(rooms).items.append(Weapon("krumpáč", True))
# player.items = sample(all_keys, randint(1, len(all_keys) - 1))

while True:
    # old_print_map(rooms, player, x_size, y_size, z_size)
    # pathfinding(player.coordinates)
    # character.main()
    for group in all_groups:
        for room in rooms:
            if group.members[0].coordinates == room.coordinates:
                room.main(group)
                clearing_screen()
                break
