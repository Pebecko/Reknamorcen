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
    weapon = Weapon()
    unarmed_weapon = Weapon()
    weapons = []
    helmets = []
    armors = []
    defence = []
    attack_power = []  # light, medium, heavy
    special_abilities = []
    helmet = Helmet()
    armor = Armor()


# player
player = Player()
player.char = "dwarf"
player.weapon = two_handed_hammer
player.helmet = helmet_1
player.armor = chainmail_hauberk
player.print_time = 0
player.health = 800
player.max_health = 800
player.health_potions = 1

# enemies
ork = Opponent()
ork.name = "ork"
ork.info = "ohromné zelené stvoření plné svalů schopné jen svýmy pařáty roztrhat nechráněného člověka na kusy"
ork.difficulty = 3
ork.lowest_health = 480
ork.highest_health = 560
ork.awareness = 4
ork.dodge_effectiveness = 0
ork.block_effectiveness = 7  # 7
ork.unarmed_weapon = claws
ork.weapons = [two_handed_axe, two_handed_axe, short_sword, long_dagger, two_handed_axe]
ork.helmets = [helmet_2]
ork.armors = [no_armor]
ork.defence = ["block"]

skeleton = Opponent()
skeleton.name = "oživlá kostra"
skeleton.info = "zbytek mrtvého člověka z kterého červi už ožrali všechno maso animovaná nějakým čarodějem"
skeleton.difficulty = 2
skeleton.lowest_health = 300
skeleton.highest_health = 360
skeleton.awareness = 1
skeleton.dodge_effectiveness = 0
skeleton.block_effectiveness = 3
skeleton.unarmed_weapon = fists
skeleton.weapons = [short_sword, short_sword, short_sword, long_dagger, long_sword]
skeleton.helmets = [no_helmet]
skeleton.armors = [chainmail_hauberk]
skeleton.defence = ["block"]

small_spider = Opponent()
small_spider.name = "malý pavouk"
small_spider.info = "mládě ohromného pavouka, sice ještě nedorostlo plné velikosti ale i tak může být nebezpečné," \
                    " obzvlášť když jich je víc"
small_spider.difficulty = 1
small_spider.lowest_health = 120
small_spider.highest_health = 160
small_spider.awareness = 5
small_spider.dodge_effectiveness = 8
small_spider.block_effectiveness = 0
small_spider.unarmed_weapon = small_cheeks
small_spider.weapons = [small_cheeks]
small_spider.helmets = [no_helmet]
small_spider.armors = [no_armor]
small_spider.defence = ["dodge"]
