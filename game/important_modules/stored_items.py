from game.equipment_stats.potions import Potions


class StoredItems:
    def __init__(self, potions=Potions(), weapons=None, armors=None, helmets=None):
        self.potions = potions

        if weapons is None:
            self.weapons = []
        else:
            self.weapons = weapons

        if armors is None:
            self.armors = []
        else:
            self.armors = armors

        if helmets is None:
            self.helmets = []
        else:
            self.helmets = helmets
