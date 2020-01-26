from random import randint, choice
from game.character_stats.character import Character
from game.equipment_stats.weapon_stats import Weapon, Claws, TwoHandedAxe, ShortSword, LongDagger, Fists, LongSword, \
    SmallCheeks, Cheeks
from game.equipment_stats.armor_stats.helmet_stats import Helmet, RustyOrkHelmet
from game.equipment_stats.armor_stats.chest_armor_stats import ChestArmor, LeatherTunic, ChainmailHauberk


class Opponent(Character):
    possessive_pronoun = "jeho"
    difficulty = 0

    lowest_health = 0
    highest_health = 0

    possible_weapons = [Weapon()]
    possible_helmets = [Helmet()]
    possible_armors = [ChestArmor()]

    # possible fight actions
    defence = []  # block, dodge
    attack_power = []  # small, medium, high

    def __init__(self):
        super().__init__()
        self.health = randint(self.lowest_health, self.highest_health)
        self.weapon = choice(self.possible_weapons)
        self.helmet = choice(self.possible_helmets)
        self.armor = choice(self.possible_armors)


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


all_opponents = [OrkBoy(), Skeleton(), Zombie(), SmallSpider(), GiantSpider()]
