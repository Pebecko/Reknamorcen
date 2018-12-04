from character_stats import player


class Room:
    def __init__(self, north=None, east=None, south=None, west=None):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.exits = 0
        if self.north != None:
            self.exits += 1
        if self.east != None:
            self.exits += 1
        if self.south != None:
            self.exits += 1
        if self.west != None:
            self.exits += 1

    def north_setting(self):
        player.last_direction = "North"
        player.room = player.room.north

    def east_setting(self):
        player.last_direction = "East"
        player.room = player.room.east

    def south_setting(self):
        player.last_direction = "South"
        player.room = player.room.south

    def west_setting(self):
        player.last_direction = "West"
        player.room = player.room.west


room1 = Room()
room2 = Room(north=room1)

room1 = Room(south=room2)
