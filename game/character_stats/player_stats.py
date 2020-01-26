from game.character_stats.character import Character
from game.equipment_stats.armor_stats.helmet_stats import GromrilHelmet
from game.equipment_stats.armor_stats.chest_armor_stats import ChainmailHauberk
from game.equipment_stats.weapon_stats import Fists, TwoHandedAxe, LongSword, LongDagger
from game.equipment_stats.potions import Potions
from game.important_modules.coordinates import Coordinates


class Player(Character):
    role = ""
    possessive_pronoun = "vaše"

    unarmed_weapon = Fists()

    defence = ["block", "dodge"]
    attack_power = ["small", "medium", "high"]

    # movement variables
    coordinates = Coordinates()
    last_direction = None
    last_fight = False

    def __str__(self):
        if self.weapon.weapon_class != "unarmed":
            weapon_info = "Vaše zbraň je {}, {}.\n".format(self.weapon.name, self.weapon.info)
        else:
            weapon_info = "Nemáte u sebe žádnou zbraň\n"

        if self.helmet.name != "":
            helmet_info = "Vaše helma je {}, {}.\n".format(self.helmet.name, self.helmet.info)
        else:
            helmet_info = "Nemáte žádnou helmu.\n"

        if self.armor.name != "":
            armor_info = "Vaše brnění je {}, {}.\n".format(self.armor.name, self.armor.info)
        else:
            armor_info = "Nemáte žádné brnění.\n"

        if self.potions.health_potions == 0:
            potion_info = "Nemáte žádné léčivé lektvary.\n"
        elif self.potions.health_potions == 1:
            potion_info = "Máte slední léčivý lektvar.\n"
        elif self.potions.health_potions in [2, 3, 4]:
            potion_info = "Máte " + str(self.potions.health_potions) + " léčivé lektvary.\n"
        else:
            potion_info = "Máte " + str(self.potions.health_potions) + " léčivých lektvarů.\n"

        return "Vaše postava je {}, {}.\n{}\n{}\n{}\n{}".format(self.name, self.info, weapon_info, helmet_info,
                                                                armor_info, potion_info)


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


# player
player = Guardsman(Potions(1))
