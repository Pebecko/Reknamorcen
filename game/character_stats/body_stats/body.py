from random import randrange
from game.character_stats.body_stats.chest import Chest
from game.character_stats.body_stats.hand import Hand
from game.character_stats.body_stats.head import Head
from game.character_stats.body_stats.leg import Leg
from game.character_stats.body_stats.blood import Blood


class Body:
    def __init__(self, hands_pairs=1, legs_pairs=1, heads=1, hand_mass=1000, leg_mass=1000, head_mass=1000,
                 chest_mass=1000):
        self.base_heads = heads
        self.heads = [Head(head_mass) for _ in range(heads)]

        self.chest = Chest(chest_mass)

        self.hands_pairs = hands_pairs
        self.hands = []
        for hand_pair in range(1, self.hands_pairs + 1):
            self.hands.append(Hand(hand_mass, "rigth", hand_pair))
            self.hands.append(Hand(hand_mass, "left", hand_pair))

        self.legs_pairs = legs_pairs
        self.legs = []
        for leg_pair in range(1, self.legs_pairs + 1):
            self.legs.append(Leg(leg_mass, "rigth", leg_pair))
            self.legs.append(Leg(leg_mass, "left", leg_pair))

        self.body_parts = [*self.heads, self.chest, *self.hands, *self.legs]

        self.body_mass = 0
        self.blood = Blood(self.body_mass)

        self.removed_body_parts = []

        self.alive = True

    def calculating_body_mass(self):
        total_mass = 0
        for body_part in self.body_parts:
            total_mass += body_part.mass

        self.body_mass = total_mass

    def bleed(self):
        for body_part in self.body_parts:
            self.blood.actual_blood_amount = body_part.bleed(self.blood.actual_blood_amount)

    def remove_limb(self, body_part_type="", side="", pair=1):
        for body_part in self.body_parts:
            if body_part.name == body_part_type:
                self.removed_body_parts.append(self.body_parts.pop(0))

    def check_for_death(self):
        if self.blood.actual_blood_amount < self.blood.minimal_blood_amount:
            self.alive = False
        for body_part in self.body_parts:
            if body_part.name == "head":
                break
        else:
            self.alive = False
