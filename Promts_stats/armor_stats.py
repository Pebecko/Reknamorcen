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
