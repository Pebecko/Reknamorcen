from game.character_stats.body_stats.body_part import BodyPart


class Limb(BodyPart):
    def __init__(self, mass, side="", pair=1):
        super().__init__(mass)
        self.broken = False
        self.side = side
        self.pair = pair
        self.unarmed_weapon = None
