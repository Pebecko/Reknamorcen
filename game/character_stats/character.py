from game.equipment_stats.potions import Potions
from game.character_stats.body_stats.body import Body
from game.equipment_stats.weapon import all_weapon_types
from game.important_modules.outside_manipulable import OutsideManipulable


class Character(OutsideManipulable):
    possessive_pronoun = ""
    player_controlled = False

    def __init__(self, import_file, **kwargs):
        super().__init__(import_file, **kwargs)

        self.race = self.importing_string("race")
        self.faction = self.importing_string("faction", False, self.race)
        self.name = self.importing_string("name")
        self.info = self.importing_string("info", False, "no info")

        self.active_traits = []

        self.potions = Potions(self.import_file, **self.kwargs)
        if not self.potions.loaded:
            self.loaded = False
        self.body = Body(self.import_file, **self.kwargs)
        if not self.body.loaded:
            self.loaded = False

        self.awareness = self.importing_integer("awareness", 1)
        self.dodge_effectiveness = self.importing_integer("dodge_effectiveness")
        self.block_effectiveness = self.importing_integer("block_effectiveness")
        self.strength = self.importing_integer("strength", 1)

        self.character_traits = self.importing_list("character_traits")
        self.possible_defence = self.importing_list("possible_defence", ["block", "dodge"])
        self.possible_attack_power = self.importing_list("possible_attack_power", ["small", "medium", "high"])

        self.max_balance = 10_000
        self.balance = 10_000

        self.equipping_coefficient = self.importing_integer("equipping_coefficient")
        self.armoring_coefficient = self.importing_integer("armoring_coefficient")
        self.possible_weapons = self.importing_list("possible_weapons")
        self.possible_armors = self.importing_list("possible_armors")

        #self.assigning_equipment()

    def __str__(self):
        return "{}, {}.\n{}{}" \
            .format(self.name.capitalize(), self.info, self.create_equipment_message(), self.potions)

    @staticmethod
    def find_carried_equipment(to_search, attribute):
        found_equipment = []

        for item in to_search:
            if getattr(item, attribute) is not None and getattr(item, attribute) not in found_equipment:
                found_equipment.append(getattr(item, attribute))

        return found_equipment

    def create_equipment_message(self):
        carried_weapons = self.find_carried_equipment(self.body.hands, "carried_weapon")
        carried_armor = self.find_carried_equipment(self.body.body_parts, "armor")

        message = ""
        if len(carried_weapons) > 0:
            message += "{} zbra{} ".format(self.possessive_pronoun,
                                           "ň je" if len(carried_weapons) == 1 else "ně jsou").capitalize()

            for num, weapon in enumerate(carried_weapons):
                message += str(weapon)
                if num == len(carried_weapons) - 1:
                    message += ".\n"
                elif num == len(carried_weapons) - 2:
                    message += " a "
                else:
                    message += ", "

        if len(carried_armor) > 0:
            message += "{} brnění je".format(self.possessive_pronoun).capitalize()

            for num, armor in enumerate(carried_armor):
                message += str(armor)
                if num == len(carried_armor) - 1:
                    message += ".\n"
                elif num == len(carried_armor) - 2:
                    message += " a "
                else:
                    message += ", "

        return message

    def finding_assignable_equipment(self, equipment_list):
        possible_equipment = []
        for equipment in equipment_list:
            if equipment.race == self.race:
                possible_equipment.append(equipment)
        return possible_equipment

    def assigning_equipment(self):
        possible_weapons = self.finding_assignable_equipment(all_weapon_types)
        if possible_weapons is not None:
            pass
