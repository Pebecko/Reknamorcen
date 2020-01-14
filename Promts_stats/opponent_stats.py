from Promts_stats.weapon_stats import Weapon, Claws, TwoHandedAxe, ShortSword, LongDagger, Fists, LongSword, \
    SmallCheeks, Cheeks
from Promts_stats.helmet_stats import Helmet, RustyOrkHelmet, GromrilHelmet, DwarvenMinerHelmet
from Promts_stats.armor_stats import Armor, LeatherTunic, ChainmailHauberk, GromrilBrestplate, SteelBrestplate


class Opponent:
    name = ""
    info = ""
    difficulty = 0
    health = 0
    max_health = 0
    lowest_health = 0
    highest_health = 0
    stamina = 0
    max_stamina = 0
    awareness = 0
    dodge_effectiveness = 0
    block_effectiveness = 0
    faction = ""
    weapon = Weapon()
    unarmed_weapon = Weapon()
    weapons = []
    helmets = [Helmet()]
    armors = [Armor()]
    defence = []
    attack_power = []  # light, medium, heavy
    special_abilities = []
    helmet = Helmet()
    armor = Armor()


# zelené kůže
class Greenskin(Opponent):
    faction = "greenskin"
    unarmed_weapon = Claws()
    defence = ["block"]


class OrkBoy(Greenskin):
    name = "ork"
    info = "ohromné zelené stvoření plné svalů schopné jen svýmy pařáty roztrhat nechráněného člověka na kusy"
    difficulty = 3
    lowest_health = 480
    highest_health = 560
    awareness = 4
    dodge_effectiveness = 0
    block_effectiveness = 7
    weapons = [TwoHandedAxe(), TwoHandedAxe(), ShortSword(), LongDagger(), TwoHandedAxe()]
    helmets = [RustyOrkHelmet(), Helmet()]
    armors = [Armor(), Armor(), Armor(), LeatherTunic()]
    attack_power = ["medium", "high"]


class Goblin(Greenskin):
    name = "skřet"
    attack_power = ["light"]


class BlackOrk(Greenskin):
    name = "černý ork"


# nemrtví
class Undead(Opponent):
    unarmed_weapon = Fists()
    defence = ["block"]
    faction = "undead"
    special_abilities = ["no_bleeding"]


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
    armors = [ChainmailHauberk(), LeatherTunic(), Armor(), Armor()]
    attack_power = ["low", "medium"]


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
    armors = [ChainmailHauberk(), LeatherTunic(), Armor(), Armor()]
    attack_power = ["low", "medium"]


# pavouci
class Spider(Opponent):
    faction = "beast"
    defence = ["dodge"]
    special_abilities = ["no_bones", "no_limbs"]


class SmallSpider(Spider):
    name = "malý pavouk"
    info = "mládě ohromného pavouka, sice ještě nedorostlo plné velikosti ale i tak může být nebezpečné," \
           " obzvlášť když jich je víc"
    difficulty = 1
    lowest_health = 120
    highest_health = 160
    awareness = 5
    dodge_effectiveness = 8
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
    dodge_effectiveness = 6
    block_effectiveness = 0
    unarmed_weapon = Cheeks()
    weapons = [Cheeks()]


class MotherSpider(Spider):
    name = "pavoučí matka"
    defence = []
