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


class Helmet:
    name = ""
    info = ""
    level = 0
    visibility = 0
    _type = ""
    heaviness = 0
    loudness = 0
    hit_points = 10000
    cut_damage_reduction = 0  # 1 - 10(%)
    stab_damage_reduction = 0  # 1 - 10(%)
    smash_damage_reduction = 0  # 1 - 10(%)
    special_abilities = []


class Armor:
    name = ""
    info = ""
    level = 0
    _type = ""
    heaviness = 0
    loudness = 0
    hit_points = 10000
    cut_damage_reduction = 0  # 1 - 10(%)
    stab_damage_reduction = 0  # 1 - 10(%)
    smash_damage_reduction = 0  # 1 - 10(%)
    special_abilities = []


class Player:
    char = ""
    info = ""
    x = 0
    y = 0
    health = 1
    max_health = 0
    stamina = 0
    max_stamina = 0
    difficulty = "hard"
    print_time = 0.015
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
    defence = []
    attack_power = []  # light, medium, heavy
    special_abilities = []
    helmet = Helmet()
    armor = Armor()


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
long_sword_mordhau.weapon_type = "heavy"
long_sword_mordhau.special_abilities = ["mordhau"]
long_sword_mordhau.weapon_class = "sword"

two_handed_axe = Weapon()
two_handed_axe.name = "obouruční sekera"
two_handed_axe.info = "ohromná dvoubřitvá zbraň, která nemá problém proseknout i tlusté brnění"
two_handed_axe.damage = 240
two_handed_axe.stamina = 6
two_handed_axe.max_stamina = 6
two_handed_axe.stamina_regain = 1
two_handed_axe.damage_type = ["cut"]
two_handed_axe.weapon_type = "heavy"
two_handed_axe.special_abilities = ["armor_piercing", "weak_dodge"]
two_handed_axe.weapon_class = "axe"

long_dagger = Weapon()
long_dagger.name = "dlouhá dýka"
long_dagger.info = "krátká, velice lehká, jednobřitvá zbraň"
long_dagger.damage = 120
long_dagger.stamina = 9
long_dagger.max_stamina = 9
long_dagger.stamina_regain = 2
long_dagger.damage_type = ["cut", "stab"]
long_dagger.weapon_type = "light"
long_dagger.special_abilities = ["extra dodge", "weak block", "poison"]
long_dagger.weapon_class = "dagger"

fists = Weapon()
fists.weapon_class = "unarmed"

# helmets
no_helmet = Helmet()

rusty_ork_helmet = Helmet()
rusty_ork_helmet.name = "rezavá orkská helma"
rusty_ork_helmet.info = "vyrobená skřety ve velmi primitivní podmínkách velmi primitivními nástroji, která se" \
                        " pak někde dlouho válela, nejspíš i s mrtvolou mrtvého orka, takže je dosti zrezlá a" \
                        " nositel si musí dát pozor aby se omylem nepořezal. Je velmi těžká ale hlavu docela ochrání"
rusty_ork_helmet.level = 1  # 1 - 3
rusty_ork_helmet.visibility = 1  # 0 - 3
rusty_ork_helmet.heaviness = 10  # 1 - 10
rusty_ork_helmet.loudness = 3
rusty_ork_helmet.hit_points = 500
rusty_ork_helmet.cut_damage_reduction = 8  # 1 - 10(%)
rusty_ork_helmet.stab_damage_reduction = 4  # 1 - 10(%)
rusty_ork_helmet.smash_damage_reduction = 6  # 1 - 10(%)
rusty_ork_helmet.special_abilities = ["rusty", "elf_debuff"]

helmet_1 = rusty_ork_helmet
helmet_1.hit_points += 500

helmet_2 = rusty_ork_helmet

# armors
no_armor = Armor()

chainmail_hauberk = Armor()
chainmail_hauberk.name = "kroužkový hauberk"
chainmail_hauberk.info = "lidmi vyrobená kroužková košile"
chainmail_hauberk.level = 2
chainmail_hauberk._type = "chaimail"
chainmail_hauberk.heaviness = 4
chainmail_hauberk.loudness = 7  # 1 - 9
chainmail_hauberk.hit_points = 5000
chainmail_hauberk.cut_damage_reduction = 3  # 1 - 10(%)
chainmail_hauberk.stab_damage_reduction = 3  # 1 - 10(%)
chainmail_hauberk.smash_damage_reduction = 4  # 1 - 10(%)
chainmail_hauberk.special_abilities = []

# player
player = Player()
player.char = "human"
player.weapon = long_sword
player.helmet = helmet_1
player.print_time = 0
player.health = 640
player.max_health = 640

# enemies
ork = Opponent()
ork.name = "ork"
ork.info = "ohromné zelené stvoření plné svalů schopné jen svýmy pařáty roztrhat nechráněného člověka na kusy"
ork.difficulty = 3
ork.lowest_health = 480
ork.highest_health = 560
ork.awareness = 3
ork.dodge_effectiveness = 0
ork.block_effectiveness = 7  # 7
ork.unarmed_weapon = fists
ork.weapons = [two_handed_axe, fists, fists, short_sword, long_dagger]
ork.defence = ["block"]
