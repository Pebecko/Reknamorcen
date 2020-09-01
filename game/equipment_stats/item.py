from random import randint
from game.important_modules.outside_manipulable import OutsideManipulable
from game.equipment_stats.material import Material


class Item(OutsideManipulable):
    weight = 0
    loudness = 0
    item_traits = []

    def __init__(self, import_file="no_import_file_specified", **kwargs):
        super().__init__(import_file=import_file, **kwargs)

        self.race = self.importing_string("race")
        self.name = self.importing_string("name")
        self.info = self.importing_string("info", False, "no info")

        self.active_traits = []

        self.material = Material(import_file=import_file, **kwargs)
        if not self.material.loaded:
            self.loaded = False

        self.mass = randint(self.importing_integer("min_size", 10_000),
                            self.importing_integer("max_size", 10_000))

        self.max_durability = self.mass * self.material.durability_multiplier
        self.weight = self.mass * self.material.density

    def __str__(self):
        return "{}, {}.\n{}".format(self.name, self.info, self.create_durability_message())

    def create_durability_message(self):
        if self.durability > self.max_durability * 0.95:
            message = "Vypadá úplně nově"
        elif self.durability >= self.max_durability * 0.8:
            message = "Vypadá v dobrém stavu"
        elif self.durability >= self.max_durability * 0.5:
            message = "Vypadá, že už má něco za sebou"
        elif self.durability >= self.max_durability * 0.25:
            message = "Vypadá dost poškozeně"
        elif self.durability >= self.max_durability * 0.10:
            message = "Vypadá velmi hodně poškozeně"
        else:
            message = "Vypadá, že téměř rozbitě"

        return message
