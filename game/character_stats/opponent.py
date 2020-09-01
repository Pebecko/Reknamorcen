from game.character_stats.character import Character
from game.important_modules.creating_items_from_imports import item_creation


opponents_import_path = "data/opponents.csv"


class Opponent(Character):
    possessive_pronoun = "jeho"

    def __init__(self, import_file="no import file given", **kwargs):
        super().__init__(import_file, **kwargs)

        self.difficulty = self.importing_integer("difficulty")


"""
class Greenskin(Opponent):
    race = "greenskin"
    unarmed_weapon = Claws()
    defence = ["block"]


class OrkBoy(Greenskin):
    name = "ork"
    info = "ohromné zelené stvoření plné svalů schopné jen svýmy pařáty roztrhat nechráněného člověka na kusy"
    difficulty = 3
    lowest_health = 520
    highest_health = 640
    awareness = 3
    dodge_effectiveness = 0
    block_effectiveness = 7
    possible_weapons = [TwoHandedAxe(), TwoHandedAxe(), ShortSword(), LongDagger(), TwoHandedAxe()]
    possible_helmets = [RustyOrkHelmet(), Helmet()]
    possible_armors = [ChestArmor(), ChestArmor(), ChestArmor(), LeatherTunic()]
    attack_power = ["medium", "high"]


class Goblin(Greenskin):
    name = "skřet"
    attack_power = ["light"]


class BlackOrk(Greenskin):
    name = "černý ork"


class Undead(Opponent):
    unarmed_weapon = Fists()
    defence = ["block"]
    race = "undead"
    character_traits = ["no_bleeding"]


class Skeleton(Undead):
    name = "oživlá kostra"
    info = "zbytek mrtvého člověka z kterého červi už ožrali všechno maso animovaná nějakým čarodějem"
    difficulty = 2
    lowest_health = 300
    highest_health = 360
    awareness = 1
    dodge_effectiveness = 0
    block_effectiveness = 3
    weapons = [ShortSword(), ShortSword(), ShortSword(), LongDagger(), LongSword()]
    armors = [ChainmailHauberk(), LeatherTunic(), ChestArmor(), ChestArmor()]
    attack_power = ["small", "medium"]


class Zombie(Undead):
    name = "oživlá mrtvola"
    info = "ještě nerozložené tělo mrtvého člověka, animované nějakým čarodějem co ho donutil vstát z hrobu"
    difficulty = 2
    lowest_health = 340
    highest_health = 420
    awareness = 1
    dodge_effectiveness = 0
    block_effectiveness = 4
    weapons = [ShortSword(), ShortSword(), ShortSword(), LongDagger(), LongSword(), Fists()]
    armors = [ChainmailHauberk(), LeatherTunic(), ChestArmor(), ChestArmor()]
    attack_power = ["small", "medium"]


class Spider(Opponent):
    race = "beast"
    defence = ["dodge"]
    character_traits = ["no_bones", "no_limbs"]


class SmallSpider(Spider):
    name = "malý pavouk"
    info = "mládě ohromného pavouka, sice ještě nedorostlo plné velikosti ale i tak může být nebezpečné," \
           " obzvlášť když jich je víc"
    difficulty = 1
    lowest_health = 120
    highest_health = 160
    awareness = 5
    dodge_effectiveness = 7
    block_effectiveness = 0
    unarmed_weapon = SmallCheeks()
    weapons = [SmallCheeks()]
    attack_power = ["small"]


class GiantSpider(Spider):
    name = "velký pavouk"
    info = "dorostlý pavouk ohromné velikosti který si bez problému troufne na dospělého jedince"
    difficulty = 3
    lowest_health = 280
    highest_health = 430
    awareness = 4
    dodge_effectiveness = 4
    block_effectiveness = 0
    unarmed_weapon = Cheeks()
    weapons = [Cheeks()]
    attack_power = ["medium"]


class MotherSpider(Spider):
    name = "pavoučí matka"
    defence = []
"""

all_opponent_types = item_creation(Opponent, opponents_import_path)
