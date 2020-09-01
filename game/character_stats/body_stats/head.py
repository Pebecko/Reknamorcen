from game.character_stats.body_stats.body_part import BodyPart


class Head(BodyPart):
    def __init__(self, mass, helmet=None):
        super().__init__(mass)
        self.name = "head"
        self.stunned = False
        self.armor = helmet
