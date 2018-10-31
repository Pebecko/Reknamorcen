class Armor:
    name = ""
    info = ""
    level = 0
    material = ""
    heaviness = 0
    loudness = 0
    hit_points = 10000
    cut_damage_reduction = 0  # 1 - 10(%)
    stab_damage_reduction = 0  # 1 - 10(%)
    smash_damage_reduction = 0  # 1 - 10(%)
    special_abilities = []
    occupied = False


no_armor = Armor()


# armor patterns
class ChainmailHauberk(Armor):
    name = "kroužkový hauberk"
    info = "lidmi vyrobená kroužková košile"
    level = 2
    material = "chaimail"
    heaviness = 4
    loudness = 7  # 1 - 9
    hit_points = 5000
    cut_damage_reduction = 3  # 1 - 10(%)
    stab_damage_reduction = 3  # 1 - 10(%)
    smash_damage_reduction = 4  # 1 - 10(%)
    special_abilities = []


class LeatherTunic(Armor):
    name = "kožená tunika"
    info = "z kůže vyrobená vesta, je celkem tichá a dobře se v ní hýbe, ale tělo moc neochrání"
    level = 1
    material = "leather"
    heaviness = 1
    loudness = 2  # 1 - 9
    hit_points = 3000
    cut_damage_reduction = 1  # 1 - 10(%)
    stab_damage_reduction = 1  # 1 - 10(%)
    smash_damage_reduction = 3  # 1 - 10(%)
    special_abilities = []


class SteelBrestplate(Armor):
    pass


class GromrilBrestplate(Armor):
    pass


# armors
class Armor1(ChainmailHauberk):
    pass


class Armor2(ChainmailHauberk):
    pass


class Armor3(LeatherTunic):
    pass


class Armor4(LeatherTunic):
    pass


# armors
armor_1 = Armor1()
armor_2 = Armor2()
armor_3 = Armor3()
armor_4 = Armor4()
