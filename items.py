class Items:
    def __init__(self, health_potions=0, weapons=None, armors=None, helmets=None):
        self.health_potions = health_potions
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
