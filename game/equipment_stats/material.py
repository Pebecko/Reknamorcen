from game.important_modules.outside_manipulable import OutsideManipulable


class Material(OutsideManipulable):
    def __init__(self, import_file="no_import_file_specified", **kwargs):
        super().__init__(import_file=import_file, **kwargs)

        self.name = self.importing_string("name")
        self.info = self.importing_string("info", False, "no info")

        self.weight = self.importing_integer("weight", 1)
        self.durability_multiplier = self.importing_float("durability_multiplier", 1)
        self.density = self.importing_integer("density", 1_000)
