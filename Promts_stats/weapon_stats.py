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


# weapons
short_sword = Weapon()
short_sword.name = "krátký meč"
short_sword.info = "krátší ostrá zbraň schopná jak sekat, tak i bodat"
short_sword.damage = 160
short_sword.stamina = 8
short_sword.max_stamina = 8
short_sword.stamina_regain = 1.5
short_sword.damage_type = ["cut", "stab"]
short_sword.weapon_type = "light"
short_sword.special_abilities = ["mordhau"]
short_sword.weapon_class = "sword"

short_sword_mordhau = Weapon()
short_sword_mordhau.name = "krátký meč"
short_sword_mordhau.info = "ostrá zbraň schopná jak sekat, tak i bodat"
short_sword_mordhau.damage = 110
short_sword_mordhau.stamina = 8
short_sword_mordhau.max_stamina = 8
short_sword_mordhau.stamina_regain = 1.5
short_sword_mordhau.damage_type = ["smash"]
short_sword_mordhau.weapon_type = "light"
short_sword_mordhau.special_abilities = ["mordhau"]
short_sword_mordhau.weapon_class = "sword"

long_sword = Weapon()
long_sword.name = "dlouhý meč"
long_sword.info = "dlouhý meč určen pro obouruční držení, ale možný používat i v jedné ruce, který je" \
                  " schopný jak sekat, tak i bodat"
long_sword.damage = 210
long_sword.stamina = 8
long_sword.max_stamina = 8
long_sword.stamina_regain = 1.5
long_sword.damage_type = ["cut", "stab"]
long_sword.weapon_type = "medium"
long_sword.special_abilities = ["mordhau"]
long_sword.weapon_class = "sword"

long_sword_mordhau = Weapon()
long_sword_mordhau.name = "dlouhý meč"
long_sword_mordhau.info = "dlouhý meč určen pro obouruční držení, ale možný používat i v jedné ruce, který je" \
                          " schopný jak sekat, tak i bodat"
long_sword_mordhau.damage = 180
long_sword_mordhau.stamina = 8
long_sword_mordhau.max_stamina = 8
long_sword_mordhau.stamina_regain = 1.5
long_sword_mordhau.damage_type = ["smash"]
long_sword_mordhau.weapon_type = "medium"
long_sword_mordhau.special_abilities = ["mordhau"]
long_sword_mordhau.weapon_class = "sword"

two_handed_sword = Weapon()
two_handed_sword.name = "obouruční meč"
two_handed_sword.info = "dlouhá zbraň určená pro obouruční boj, jedno její seknutí bez broblému přesekne jakéhokoliv" \
                        " neobrněného nepřítele, tak ho i probodne"
two_handed_sword.damage = 240
two_handed_sword.stamina = 7
two_handed_sword.max_stamina = 7
two_handed_sword.stamina_regain = 1
two_handed_sword.damage_type = ["cut", "stab"]
two_handed_sword.weapon_type = "heavy"
two_handed_sword.special_abilities = ["mordhau"]
two_handed_sword.weapon_class = "sword"

two_handed_sword_mordhau = Weapon()
two_handed_sword_mordhau.name = "obouruční meč"
two_handed_sword_mordhau.info = "dlouhá zbraň určená pro obouruční boj, jedno její seknutí bez broblému přesekne" \
                                " jakéhokoliv neobrněného nepřítele, tak ho i probodne"
two_handed_sword_mordhau.damage = 210
two_handed_sword_mordhau.stamina = 7
two_handed_sword_mordhau.max_stamina = 7
two_handed_sword_mordhau.stamina_regain = 1
two_handed_sword_mordhau.damage_type = ["smash"]
two_handed_sword_mordhau.weapon_type = "heavy"
two_handed_sword_mordhau.special_abilities = ["mordhau"]
two_handed_sword_mordhau.weapon_class = "sword"

two_handed_axe = Weapon()
two_handed_axe.name = "obouruční sekera"
two_handed_axe.info = "ohromná dvoubřitvá zbraň, která nemá problém proseknout i tlusté brnění"
two_handed_axe.damage = 250
two_handed_axe.stamina = 6
two_handed_axe.max_stamina = 6
two_handed_axe.stamina_regain = 1
two_handed_axe.damage_type = ["cut"]
two_handed_axe.weapon_type = "heavy"
two_handed_axe.special_abilities = ["armor_piercing", "weak_dodge"]
two_handed_axe.weapon_class = "axe"

two_handed_hammer = Weapon()
two_handed_hammer.name = "obouruční kladivo"
two_handed_hammer.info = "ohromná trpaslíky vyrobená zbraň, určená aby tříštila kosti všech obrněnců, jedno co mají" \
                         " na sobě"
two_handed_hammer.damage = 230
two_handed_hammer.stamina = 5
two_handed_hammer.max_stamina = 5
two_handed_hammer.stamina_regain = 1
two_handed_hammer.damage_type = ["smash"]
two_handed_hammer.weapon_type = "heavy"
two_handed_hammer.special_abilities = ["weak_dodge", "dwarf_buff", "elf_debuff"]
two_handed_hammer.weapon_class = "hammer"

long_dagger = Weapon()
long_dagger.name = "dlouhá dýka"
long_dagger.info = "krátká, velice lehká, jednobřitvá zbraň"
long_dagger.damage = 120
long_dagger.stamina = 9
long_dagger.max_stamina = 9
long_dagger.stamina_regain = 2
long_dagger.damage_type = ["cut", "stab"]
long_dagger.weapon_type = "light"
long_dagger.special_abilities = ["extra_dodge", "weak_block", "elf_debuff"]
long_dagger.weapon_class = "dagger"

fists = Weapon()
fists.name = "pěsti"
fists.weapon_class = "unarmed"

claws = Weapon()
claws.name = "drápy"
claws.weapon_class = "unarmed"

small_cheeks = Weapon()
small_cheeks.name = "malá kusadla"
small_cheeks.damage = 40
small_cheeks.damage_type = ["stab"]
small_cheeks.weapon_type = "light"
small_cheeks.special_abilities = ["extra_dodge", "weak_block"]
small_cheeks.weapon_class = "unarmed"
