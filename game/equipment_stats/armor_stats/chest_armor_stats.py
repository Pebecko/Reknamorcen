from game.equipment_stats.armor_stats.armor import Armor


class ChestArmor(Armor):
    pass


# TODO Add new armor_stats
class ChainmailHauberk(ChestArmor):
    name = "kroužkový hauberk"
    info = "lidmi vyrobená kroužková košile"
    material = "chaimail"
    min_durability = 4_000
    max_durability = 8_000
    heaviness = 4
    loudness = 7  # 1 - 9
    cut_damage_reduction = 3  # 1 - 10(%)
    stab_damage_reduction = 3  # 1 - 10(%)
    smash_damage_reduction = 4  # 1 - 10(%)


class LeatherTunic(ChestArmor):
    name = "kožená tunika"
    info = "z kůže vyrobená vesta, je celkem tichá a dobře se v ní hýbe, ale tělo moc neochrání"
    material = "leather"
    min_durability = 2_000
    max_durability = 4_500
    heaviness = 1
    loudness = 2  # 1 - 9
    cut_damage_reduction = 1  # 1 - 10(%)
    stab_damage_reduction = 1  # 1 - 10(%)
    smash_damage_reduction = 3  # 1 - 10(%)


class SteelBrestplate(ChestArmor):
    pass


class GromrilBrestplate(ChestArmor):
    pass

