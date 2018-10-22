from Promts_stats.weapon_stats import *
from Promts_stats.helmet_stats import *
from Promts_stats.armor_stats import *


class Player:
    char = ""
    info = ""
    x = 3
    y = 3
    last_direction = None
    health = 1
    max_health = 0
    stamina = 0
    max_stamina = 0
    health_potions = 0
    difficulty = "hard"
    print_time = 0.015
    special_abilities = []
    test = True
    weapon = Weapon()
    helmet = Helmet()
    armor = Armor()
    last_fight = False


# player
player = Player()
player.char = "dwarf"
player.weapon = two_handed_hammer
player.helmet = helmet_2
player.armor = armor_1
player.print_time = 0
player.health = 800
player.max_health = 800
player.health_potions = 1


class Opponent:
    name = ""
    info = ""
    difficulty = 0
    health = 0
    max_health = 0
    lowest_health = 0
    highest_health = 0
    awareness = 0
    dodge_effectiveness = 0
    block_effectiveness = 0
    kind = ""
    weapon = Weapon()
    unarmed_weapon = Weapon()
    weapons = []
    helmets = [no_helmet]
    armors = [no_armor]
    defence = []
    attack_power = []  # light, medium, heavy
    special_abilities = []
    helmet = Helmet()
    armor = Armor()

# zelené kůže
class Greenskin(Opponent):
    kind = "greenskin"
    unarmed_weapon = claws
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
    weapons = [two_handed_axe, two_handed_axe, short_sword, long_dagger, two_handed_axe]
    helmets = [helmet_1, no_helmet]
    armors = [no_armor, no_armor, no_armor, armor_3]
    attack_power = ["medium", "heavy", "heavy"]


class Goblin(Greenskin):
    name = "skřet"
    attack_power = ["light"]


class BlackOrk(Greenskin):
    name = "černý ork"


# nemrtví
class Undead(Opponent):
    unarmed_weapon = fists
    defence = ["block"]
    kind = "undead"
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
    weapons = [short_sword, short_sword, short_sword, long_dagger, long_sword]
    armors = [armor_2, armor_4, no_armor, no_armor]
    attack_power = ["low", "low", "medium"]


class Zombie(Undead):
    name = "oživlá mrtvola"
    info = "ještě nerozložené tělo mrtvého člověka, animované nějakým čarodějem co ho donutil vstát z hrobu"
    difficulty = 2
    lowest_health = 340
    highest_health = 420
    awareness = 1
    dodge_effectiveness = 0
    block_effectiveness = 4
    weapons = [short_sword, short_sword, short_sword, long_dagger, long_sword]
    armors = [armor_2, armor_4, no_armor, no_armor]
    attack_power = ["low", "medium"]


# pavouci
class Spider(Opponent):
    kind = "spider"
    defence = ["dodge"]


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
    unarmed_weapon = small_cheeks
    weapons = [small_cheeks]


class GiantSpider(Spider):
    name = "velký pavouk"
    info = "dorostlý pavouk ohromné velikosti který si bez problému troufne na dospělého jedince"
    difficulty = 3
    lowest_health = 280
    highest_health = 430
    awareness = 4
    dodge_effectiveness = 6
    block_effectiveness = 0
    unarmed_weapon = cheeks
    weapons = [cheeks]


class MotherSpider(Spider):
    name = "pavoučí matka"
    defence = []


# oponenti
class Opponent1(OrkBoy):
    pass


opponent_1 = Opponent1()

class Opponent2(OrkBoy):
    pass


opponent_2 = Opponent2()


class Opponent3(Skeleton):
    pass


opponent_3 = Opponent3()


class Opponent4(Skeleton):
    pass


opponent_4 = Opponent4()


class Opponent5(Zombie):
    pass


opponent_5 = Opponent5()


class Opponent6(Zombie):
    pass


opponent_6 = Opponent6()


class Opponent7(SmallSpider):
    pass


opponent_7 = Opponent7()


class Opponent8(SmallSpider):
    pass


opponent_8 = Opponent8()