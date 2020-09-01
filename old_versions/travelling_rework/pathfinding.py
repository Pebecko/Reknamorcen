class Pathfinder:
    def __init__(self):
        self.parent = None
        self.parent_direction = None
        self.distance = 99

    def resetting(self):
        self.parent = None
        self.parent_direction = None
        self.distance = 99
