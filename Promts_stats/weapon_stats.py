class Weapon:
    name = ""
    info = ""
    xp = 0
    damage = 0
    stamina_regain = 0
    damage_type = []
    weapon_type = ""
    special_abilities = []
    weapon_class = ""
    number = ""
    hands = []

    def __init__(self, hit_points=10_000):
        self.hit_points = hit_points


# weapons class patterns
class Sword(Weapon):
    damage_type = ["cut", "stab"]
    special_abilities = ["mordhau"]
    weapon_class = "sword"
    number = "sin"
    mordhau_variant = Weapon()


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


class ShortSword(Sword):
    name = "krátký meč"
    info = "krátší ostrá zbraň schopná jak sekat, tak i bodat"
    damage = 160
    stamina_regain = 1.5
    weapon_type = "light"
    special_abilities = ["mordhau", "extra_dodge"]
    hands = [1]
    mordhau_variant = None


class ShortSwordMordhau(ShortSword):
    damage = 110
    damage_type = ["smash"]


class LongSword(Sword):
    name = "dlouhý meč"
    info = "dlouhý meč určen pro obouruční držení, ale možný používat i v jedné ruce, který je" \
           " schopný jak sekat, tak i bodat"
    damage = 210
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
    stamina_regain = 1
    weapon_type = "heavy"
    special_abilities = ["armor_piercing", "weak_dodge"]
    hands = [2]


class BattleAxe(Axe):
    pass


class LumberAxe(Axe):
    pass


class TwoHandedHammer(Hammer):
    name = "obouruční kladivo"
    info = "ohromná trpaslíky vyrobená zbraň, určená aby tříštila kosti všech obrněnců, jedno co mají" \
           " na sobě, používaná ochrankou jejich vůdců"
    damage = 230
    stamina_regain = 1
    weapon_type = "heavy"
    special_abilities = ["weak_dodge", "dwarf_buff", "elf_debuff", "life_steal"]
    hands = [2]


class BattleHammer(Hammer):
    name = "jednoruční bojové kladivo"
    info = "trpaslíky vyrobená zbraň, na jednoručku je dost těžká, ale zato to s ní opravdu bolí"
    damage = 200
    stamina_regain = 1.5
    weapon_type = "medium"
    special_abilities = ["dwarf_buff", "elf_debuff"]
    hands = [1]


class BlacksmithHammer(Hammer):
    pass


class LongDagger(Dagger):
    name = "dlouhá dýka"
    info = "krátká, velice lehká, jednobřitvá zbraň"
    damage = 120
    stamina_regain = 2
    special_abilities = ["life_steal"]


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
