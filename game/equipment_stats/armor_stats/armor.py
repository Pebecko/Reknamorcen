from game.equipment_stats.item import Item


class Armor(Item):
    material = ""

    cut_damage_reduction = 0  # 1 - 10(%)
    stab_damage_reduction = 0  # 1 - 10(%)
    smash_damage_reduction = 0  # 1 - 10(%)

    def __init__(self, import_file="no_import_file_specified", **kwargs):
        super().__init__(import_file=import_file, **kwargs)
