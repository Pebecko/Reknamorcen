from game.equipment_stats.potions import Potions
from game.character_stats.body_stats.body import Body


class Character:
    race = ""
    name = ""
    info = ""
    possessive_pronoun = ""

    body = Body

    health = 1
    max_health = 1
    balance = 1
    max_balance = 1

    awareness = 0
    size = 1
    dodge_effectiveness = 0
    block_effectiveness = 0
    character_traits = []
    defence = []
    attack_power = []

    def __init__(self, potions=Potions(), helmets=None, chest_armor=None, gloves=None, hands_pairs=1, heads=1):
        self.active_traits = []
        self.potions = potions
        self.body = Body(hands_pairs, heads, helmets, chest_armor, gloves)

    def __str__(self):
        return "{}, {}.".format(self.name, self.info)
