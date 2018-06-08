from Recnamorcen.main_funcs import *


class Weapon:
    name = ""
    info = ""
    xp = 0
    damage = 0
    stamina = 0
    max_stamina = 0
    stamina_regain = 0
    hit_points = 10000
    damage_type = []
    weapon_type = ""
    special_abilities = []
    weapon_class = ""

    def get_info(self):
        slow_print(self.info)


class Player:
    char = ""
    info = ""
    health = 1
    max_health = 0
    stamina = 0
    max_stamina = 0
    difficulty = "easy"
    weapon = Weapon()
    gear = []


class Opponent:
    name = ""
    info = ""
    difficulty = 0
    health = 0
    max_health = 0
    lowest_health = 0
    highest_health = 0
    awareness = 0
    weapon = Weapon()
    weapons = []
    defence = []
    special_abilities = []

    def get_info(self):
        slow_print(self.info)


# weapons
short_sword = Weapon()
short_sword.name = "krátký meč"
short_sword.info = "ostrá zbraň schopná jak sekat, tak i bodat"
short_sword.damage = 5
short_sword.stamina = 8
short_sword.max_stamina = 8
short_sword.stamina_regain = 1.5
short_sword.damage_type = ["cut", "stab"]
short_sword.weapon_type = "light"
short_sword.special_abilities = ["mordhau"]
short_sword.weapon_class = "sword"

# mordhau style
short_sword_mordhau = Weapon()
short_sword_mordhau.name = "krátký meč"
short_sword_mordhau.info = "ostrá zbraň schopná jak sekat, tak i bodat"
short_sword_mordhau.damage = 3
short_sword_mordhau.stamina = 8
short_sword_mordhau.max_stamina = 8
short_sword_mordhau.stamina_regain = 1.5
short_sword_mordhau.damage_type = ["smash"]
short_sword_mordhau.weapon_type = "light"
short_sword_mordhau.special_abilities = ["mordhau"]
short_sword_mordhau.weapon_class = "sword"

two_handed_axe = Weapon()
two_handed_axe.name = "obouruční sekera"
two_handed_axe.info = "ohromná dvoubřitvá obouruční sekera, která nemá problém proseknout i tlusté brnění"
two_handed_axe.damage = 8
two_handed_axe.stamina = 6
two_handed_axe.max_stamina = 6
two_handed_axe.stamina_regain = 1
two_handed_axe.damage_type = ["cut"]
two_handed_axe.weapon_type = "heavy"
two_handed_axe.special_abilities = ["armor piercing", "weak dodge"]
two_handed_axe.weapon_class = "axe"

long_dagger = Weapon()
long_dagger.name = "dlouhá dýka"
long_dagger.info = "krátká, velice lehká, jednobřitvá zbraň"
long_dagger.damage = 4
long_dagger.stamina = 9
long_dagger.max_stamina = 9
long_dagger.stamina_regain = 2
long_dagger.damage_type = ["cut", "stab"]
long_dagger.weapon_type = "light"
long_dagger.special_abilities = ["extra dodge", "weak block"]
long_dagger.weapon_class = "dagger"

fists = Weapon()
fists.weapon_class = "unarmed"

# player
player = Player()
player.char = "human"
player.weapon = short_sword

# enemies
ork = Opponent()
ork.name = "ork"
ork.info = "ohromné zelené stvoření plné svalů schopné jen svýmy pařáty roztrhat nechráněného člověka na kusy"
ork.difficulty = 3
ork.lowest_health = 16
ork.highest_health = 26
ork.awareness = 3
ork.weapons = ["two_handed_axe"]
ork.defence = ["block"]
