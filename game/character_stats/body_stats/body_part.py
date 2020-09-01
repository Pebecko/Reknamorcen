from game.equipment_stats.weapon import Weapon


class BodyPart:
    name = ""
    armor = None

    def __init__(self, mass):
        self.mass = mass
        self.unarmed_weapon = self.defining_unarmed_weapon()
        self.bleeding_level = 0  # 0 <-> 3

    def defining_unarmed_weapon(self):
        return None

    def bleed(self, total_blood):
        return total_blood / 24 * self.bleeding_level
