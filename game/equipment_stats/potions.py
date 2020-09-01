from game.important_modules.outside_manipulable import OutsideManipulable


class Potions(OutsideManipulable):
    def __init__(self, import_file, **kwargs):
        super().__init__(import_file, **kwargs)

        self.health_potions = self.importing_integer("base_health_potions")
        self.strength_potions = self.importing_integer("base_strength_potions")
        self.speed_potions = self.importing_integer("base_speed_potions")
        self.max_potions = self.importing_integer("max_potions", 5)

    def __str__(self):
        message = ""
        if self.health_potions > 0:
            message += "Počet lektvarů léčení: {}\n".format(self.health_potions)
        if self.speed_potions > 0:
            message += "Počet lektvarů rychlosti: {}\n".format(self.speed_potions)
        if self.strength_potions > 0:
            message += "Počet lektvarů síly: {}\n".format(self.strength_potions)
        if message != "":
            message += "\n"

        return message
