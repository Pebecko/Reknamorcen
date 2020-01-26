from game.character_stats.body_stats.limb import Limb


class Hand(Limb):
    def __init__(self, mass, side="", pair=1, carried_weapon=None, glove=None):
        super().__init__(mass, side, pair)
        self.name = "hand"
        self.carried_weapon = carried_weapon
        self.armor = glove
