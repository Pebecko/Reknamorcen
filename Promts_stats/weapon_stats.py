class Weapon:
    name = ""
    info = ""
    xp = 0
    damage = 0
    stamina_regain = 0
    hit_points = 10000
    damage_type = []
    weapon_type = ""
    special_abilities = []
    weapon_class = ""
    number = ""
    hands = []


# weapons class patterns
class Sword(Weapon):
    damage_type = ["cut", "stab"]
    special_abilities = ["mordhau"]
    weapon_class = "sword"
    number = "sin"


class Axe(Weapon):
    damage_type = ["cut"]
    weapon_class = "axe"
    number = "sin"


class Hammer(Weapon):
    damage_type = ["smash"]
    weapon_class = "hammer"
    number = "sin"


class Dagger(Weapon):
    damage_type = ["cut", "stab"]
    weapon_type = "light"
    special_abilities = ["extra_dodge", "weak_block"]
    weapon_class = "dagger"
    number = "sin"
    hands = [1]

class Spear(Weapon):
    hands = [1, 2]


class Halberd(Weapon):
    hands = [2]


class Mace(Weapon):
    hands = [1]


class Chopper(Weapon):
    hands = [1]


class Flail(Weapon):
    hands = [1]


class Staff(Weapon):
    pass


class Pickaxe(Weapon):
    hands = [2]


class Unarmed(Weapon):
    weapon_type = "light"
    special_abilities = ["extra_dodge", "weak_block"]
    weapon_class = "unarmed"
    number = "plu"
    hands = [1, 2]

# weapons patterns
class ShortSword(Sword):
    name = "krátký meč"
    info = "krátší ostrá zbraň schopná jak sekat, tak i bodat"
    damage = 160
    stamina = 8
    max_stamina = 8
    stamina_regain = 1.5
    weapon_type = "light"
    special_abilities = ["mordhau", "extra_dodge"]
    hands = [1]


class ShortSwordMordhau(ShortSword):
    damage = 110
    damage_type = ["smash"]


class LongSword(Sword):
    name = "dlouhý meč"
    info = "dlouhý meč určen pro obouruční držení, ale možný používat i v jedné ruce, který je" \
           " schopný jak sekat, tak i bodat"
    damage = 210
    stamina = 8
    max_stamina = 8
    stamina_regain = 1.5
    weapon_type = "medium"
    hands = [1, 2]


class LongSwordMordhau(LongSword):
    damage = 180
    damage_type = ["smash"]


class TwoHandedSword(Sword):
    name = "obouruční meč"
    info = "dlouhá zbraň určená pro obouruční boj, jedno její seknutí bez broblému přesekne jakéhokoliv" \
           " neobrněného nepřítele, tak ho i probodne"
    damage = 240
    stamina = 7
    max_stamina = 7
    stamina_regain = 1
    weapon_type = "heavy"
    special_abilities = ["mordhau", "human_buff", "weak_dodge"]
    hands = [2]


class TwoHandedSwordMordhau(TwoHandedSword):
    damage = 210
    damage_type = "smash"


class TwoHandedAxe(Axe):
    name = "obouruční sekera"
    info = "ohromná dvoubřitvá zbraň, která nemá problém proseknout i tlusté brnění"
    damage = 250
    stamina = 6
    max_stamina = 6
    stamina_regain = 1
    weapon_type = "heavy"
    special_abilities = ["armor_piercing", "weak_dodge"]
    hands = [2]


class TwoHandedHammer(Hammer):
    name = "obouruční kladivo"
    info = "ohromná trpaslíky vyrobená zbraň, určená aby tříštila kosti všech obrněnců, jedno co mají" \
           " na sobě"
    damage = 230
    stamina = 5
    max_stamina = 5
    stamina_regain = 1
    weapon_type = "heavy"
    special_abilities = ["weak_dodge", "dwarf_buff", "elf_debuff"]
    hands = [2]


class LongDagger(Dagger):
    name = "dlouhá dýka"
    info = "krátká, velice lehká, jednobřitvá zbraň"
    damage = 120
    stamina = 9
    max_stamina = 9
    stamina_regain = 2


class Fists(Unarmed):
    name = "pěsti"


class Claws(Unarmed):
    name = "drápy"


class SmallCheeks(Unarmed):
    name = "malá kusadla"
    damage = 40
    damage_type = ["stab"]
    weapon_type = "light"


class Cheeks(Unarmed):
    name = "kusadla"
    damage = 120
    damage_type = ["stab"]
    weapon_type = "medium"
    special_abilities = ["poison"]

# weapons
short_sword = ShortSword()

short_sword_mordhau = ShortSwordMordhau()

long_sword = LongSword()

long_sword_mordhau = LongSwordMordhau()

two_handed_sword = TwoHandedSword()

two_handed_sword_mordhau = TwoHandedSwordMordhau()

two_handed_axe = TwoHandedAxe()

two_handed_hammer = TwoHandedHammer()

long_dagger = LongDagger()

fists = Fists()

claws = Claws()

small_cheeks = SmallCheeks()

cheeks = Cheeks()