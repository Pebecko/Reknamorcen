from random import randint
from game.important_modules.outside_manipulable import OutsideManipulable
from game.character_stats.body_stats.chest import Chest
from game.character_stats.body_stats.hand import Hand
from game.character_stats.body_stats.head import Head
from game.character_stats.body_stats.leg import Leg
from game.character_stats.body_stats.blood import Blood
from game.character_stats.body_stats.limb import Limb


class Body(OutsideManipulable):
    # hands_pairs=1, legs_pairs=1, heads=1, hand_mass=4_200, leg_mass=14_800, head_mass=6_000,
    #                  chest_mass=36_000, no_blood=False, no_brain=False,
    def __init__(self, import_file, **kwargs):
        super().__init__(import_file, **kwargs)

        # creating head(s)
        self.base_heads = self.importing_integer("heads", 1)
        head_mass = randint(self.importing_integer("min_head_mass", 6_000),
                            self.importing_integer("max_head_mass", 6_000))
        self.heads = [Head(head_mass) for _ in range(self.base_heads)]

        # creating chest
        chest_mass = randint(self.importing_integer("min_chest_mass", 36_000),
                             self.importing_integer("max_chest_mass", 36_000))
        self.chest = Chest(chest_mass)

        # creating hand(s)
        self.hands_pairs = self.importing_integer("hands_pairs", 1)
        self.hands = []
        hand_mass = randint(self.importing_integer("min_hand_mass", 4_200),
                            self.importing_integer("max_hand_mass", 4_200))
        for hand_pair in range(1, self.hands_pairs + 1):
            self.hands.append(Hand(hand_mass, "rigth", hand_pair))
            self.hands.append(Hand(hand_mass, "left", hand_pair))

        # creating leg(s)
        self.legs_pairs = self.importing_integer("legs_pairs", 1)
        self.legs = []
        leg_mass = randint(self.importing_integer("min_leg_mass", 14_800),
                           self.importing_integer("max_leg_mass", 14_800))
        for leg_pair in range(1, self.legs_pairs + 1):
            self.legs.append(Leg(leg_mass, "rigth", leg_pair))
            self.legs.append(Leg(leg_mass, "left", leg_pair))

        self.body_parts = [*self.heads, self.chest, *self.hands, *self.legs]
        self.removed_body_parts = []

        self.body_mass = 0
        self.calculating_body_mass()

        self.blood = Blood(self.body_mass)

        if self.importing_string("no_blood", False).casefold() == "y":
            self.no_blood = True
        else:
            self.no_blood = False
        if self.importing_string("no_brain", False).casefold() == "y":
            self.no_brain = True
        else:
            self.no_brain = False

    def calculating_body_mass(self):
        total_mass = 0
        for body_part in self.body_parts:
            total_mass += body_part.mass

        self.body_mass = total_mass

    def bleed(self):
        for body_part in self.body_parts + self.removed_body_parts:
            self.blood.actual_blood_amount = body_part.bleed(self.blood.actual_blood_amount)

    def remove_limb(self, body_part_type="", side="", pair=1):
        for body_part in self.body_parts:
            if body_part.name == body_part_type:
                if issubclass(body_part.__class__, Limb):
                    if body_part.side == side and body_part.pair == pair:
                        self.removed_body_parts.append(self.body_parts.pop(0))
                else:
                    self.removed_body_parts.append(self.body_parts.pop(0))

    def check_for_death(self):
        # bleedout
        if self.blood.actual_blood_amount < self.blood.minimal_blood_amount and not self.no_blood:
            self.alive = False

        # beheaded
        for body_part in self.body_parts:
            if body_part.name == "head":
                break
        else:
            if not self.no_brain:
                self.alive = False
