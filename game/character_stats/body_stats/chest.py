from game.character_stats.body_stats.body_part import BodyPart


class Chest(BodyPart):
    def __init__(self, mass, chest_armor=None):
        super().__init__(mass)
        self.name = "chest"
        self.armor = chest_armor
