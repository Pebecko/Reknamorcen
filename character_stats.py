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
    print_time = 0.005
    special_abilities = []
    test = True
    weapon = fists
    helmet = no_helmet
    armor = no_armor
    last_fight = False


# races
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


# characters
class Slayer(Dwarf):
    role = "slayer"
    name = "Gurni Gordrengi"
    info = "starý trpaslík co se před dlouhou dobou přidal k sektě trolobijců, co v poslední době bloudí daleko od" \
           " svého domova na jihu země lidí a hledá dalšího nepřítele s kterým by mohl hrdinně padnout v souboji"
    health = 500
    max_health = 820
    special_abilities = ["poison_resistance", "no_armor"]
    weapon = two_handed_axe


class Ironbreaker(Dwarf):
    role = "ironbreaker"
    health = 780
    max_health = 780
    weapon = long_dagger
    helmet = gromril_helmet_1
    armor = armor_1


class Miner(Dwarf):
    pass


class Engineer(Dwarf):
    pass


class Guardsman(Human):
    role = "guardsman"
    name = "Erwin Grünbaum"
    armor = armor_1
    weapon = long_sword


class Assasin(Elf):
    pass


# player
player = Player()
player.print_time = 0
