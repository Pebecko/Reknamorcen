from game.character_stats.character import Character
from game.important_modules.creating_items_from_imports import item_creation
from game.equipment_stats.armor_stats.helmet_stats import GromrilHelmet
from game.equipment_stats.armor_stats.chest_armor_stats import ChainmailHauberk
from game.important_modules.coordinates import Coordinates


players_import_path = "data/players.csv"


class Player(Character):
    possessive_pronoun = "vaše"
    player_controlled = True

    # movement variables
    coordinates = Coordinates()
    last_direction = None
    last_fight = False


"""
# races
class Dwarf(Player):
    race = "dwarf"
    health = 720
    max_health = 720
    character_traits = ["poison_resistance"]


class Human(Player):
    race = "human"
    health = 660
    max_health = 660


class Elf(Player):
    race = "elf"
    health = 580
    max_health = 580
    character_traits = ["sneaky"]


# characters
class Slayer(Dwarf):
    role = "slayer"
    name = "Gurni Gordrengi"
    info = "starý trpaslík co se před dlouhou dobou přidal k sektě trolobijců, co v poslední době bloudí daleko od" \
           " svého domova na jihu země lidí a hledá dalšího nepřítele s kterým by mohl hrdinně padnout v souboji"
    health = 500
    max_health = 820
    character_traits = ["poison_resistance", "no_armor"]
    weapon = TwoHandedAxe()


class Ironbreaker(Dwarf):
    role = "ironbreaker"
    health = 780
    max_health = 780
    weapon = LongDagger()
    helmet = GromrilHelmet()
    armor = ChainmailHauberk()


class Miner(Dwarf):
    pass


class Engineer(Dwarf):
    pass


class Guardsman(Human):
    role = "guardsman"
    name = "Erwin Grünbaum"
    armor = ChainmailHauberk()
    weapon = LongSword()


class Assasin(Elf):
    pass
"""

all_player_types = item_creation(Player, players_import_path)
for i in all_player_types:
    print(i)
