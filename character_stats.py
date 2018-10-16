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
two_handed_sword_mordhau.info = "dlouhá zbraň určená pro obouruční boj, jedno její seknutí bez broblému přesekne jakéhokoliv" \
                                " neobrněného nepřítele, tak ho i probodne"
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

# helmets
no_helmet = Helmet()

dwarven_miner_helmet = Helmet()
dwarven_miner_helmet.name = "trpasličí důlnická helma"
dwarven_miner_helmet.info = "používaná trpaslíky v dolech slouží spíše jako ochrana hlavy při chození tunelem než" \
                            " na boj, ale část úderu rozhodně zastaví"
dwarven_miner_helmet.level = 1
dwarven_miner_helmet.visibility = 1
dwarven_miner_helmet.loudness = 2
dwarven_miner_helmet.cut_damage_reduction = 5
dwarven_miner_helmet.stab_damage_reduction = 3
dwarven_miner_helmet.smash_damage_reduction = 5

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
rusty_ork_helmet.stab_damage_reduction = 2  # 1 - 10(%)
rusty_ork_helmet.smash_damage_reduction = 3  # 1 - 10(%)
rusty_ork_helmet.special_abilities = ["rusty", "elf_debuff"]

helmet_1 = dwarven_miner_helmet

helmet_2 = rusty_ork_helmet
helmet_2.hit_points += 500

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
