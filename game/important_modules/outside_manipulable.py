class OutsideManipulable:
    def __init__(self, import_file, **kwargs):
        self.loaded = True
        self.import_file = import_file
        self.kwargs = kwargs

    def importing_string(self, imported_item, needed=True, base_value=""):
        item = ""

        try:
            item = self.kwargs[imported_item]
        except KeyError:
            self.loading_problem(imported_item)
        else:
            if self.kwargs[imported_item] == "":
                if needed:
                    self.loading_problem(imported_item, message="Parameter \"{}\" in {} needs to be specified")
                else:
                    item = base_value

        return item

    def importing_float(self, imported_item, base_value=0.0, min_value=0.0, max_value=float("inf")):
        item = 0.0

        try:
            self.kwargs[imported_item] = self.kwargs[imported_item].replace(" ", "").replace(",", ".")
            item = float(self.kwargs[imported_item])
        except KeyError:
            self.loading_problem(imported_item)
        except ValueError:
            if not self.kwargs[imported_item] == "":
                self.loading_problem(imported_item, message="Item \"{}\" in {} needs to be a decimal number.")
            else:
                item = base_value
        else:
            if min_value > item:
                self.loading_problem(imported_item, min_value, message="Value of \"{}\" needs to be at least {} in {}.")
            elif item > max_value:
                self.loading_problem(imported_item, max_value, message="Value of \"{}\" needs to be at most {} in {}.")

        return item

    def importing_integer(self, imported_item, base_value=0, min_value=0, max_value=float("inf")):
        item = 0

        try:
            item = int(self.kwargs[imported_item])
        except KeyError:
            self.loading_problem(imported_item)
        except ValueError:
            if not self.kwargs[imported_item] == "":
                self.loading_problem(imported_item, message="Item \"{}\" in {} needs to be an integer.")
            else:
                item = base_value
        else:
            if min_value > item:
                self.loading_problem(imported_item, min_value, message="Value of \"{}\" needs to be at least {} in {}.")
            elif item > max_value:
                self.loading_problem(imported_item, max_value, message="Value of \"{}\" needs to be at most {} in {}.")

        return item

    def importing_list(self, imported_item, base_value=None):
        item = []

        try:
            item = self.kwargs[imported_item].split(",")
        except KeyError:
            self.loading_problem(imported_item)
        else:
            if self.kwargs[imported_item] == "" and base_value is not None:
                item = base_value

        return item

    def loading_problem(self, *problematic_items, message="Could not find \"{}\" in {}."):
        self.loaded = False
        print("*import error* " + message.format(*problematic_items, self.import_file) + " Object can't be loaded.")
