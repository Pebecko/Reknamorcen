from game.character_stats.body_stats.limb import Limb


class Leg(Limb):
    def __init__(self, mass, side="", pair=1, leg_armor=None):
        super().__init__(mass, side, pair)
        self.name = "leg"
        self.armor = leg_armor
