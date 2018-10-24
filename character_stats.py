from Promts_stats.opponent_stats import *


class Player:
    char = ""
    role = ""
    name = ""
    info = ""
    x = 0
    y = 0
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


class Dwarf(Player):
    char = "dwarf"
    health = 720
    max_health = 720
    special_abilities = ["poison_resistance"]


class Human(Player):
    char = "human"
    health = 660
    max_health = 660
    health_potions = 1


class Elf(Player):
    char = "elf"
    health = 580
    max_health = 580
    special_abilities = ["sneaky"]
    health_potions = 2


class Slayer(Dwarf):
    role = "slayer"
    name = "Gurni Gordrengi"
    info = "starý trpaslík co se před dlouhou dobou přidal k sektě trolobijců, co v poslední době bloudí daleko od" \
           " svého domova na jihu země lidí a hledá dalšího nepřítele s kterým by mohl hrdinně padnout v souboji"
    health = 820
    max_health = 820
    special_abilities = ["poison_resistance", "no_armor"]

# player
player = Slayer()
player.weapon = two_handed_axe
