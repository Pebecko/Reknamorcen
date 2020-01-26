from random import randint


class Item:
    name = ""
    info = ""
    race = ""

    min_durability = 10_000
    max_durability = 10_000

    min_size = 1
    max_size = 1

    weight = 0
    loudness = 0
    item_traits = []

    def __init__(self, durability=None):
        self.active_traits = []
        if durability is None:
            self.durability = randint(self.min_durability, self.max_durability)
        else:
            self.durability = durability
