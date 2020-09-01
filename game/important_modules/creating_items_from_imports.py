from game.important_modules.csv_importing import importing_dict_from_csv


def item_creation(cls, path=""):
    found_items = []
    for item_data in importing_dict_from_csv(path):
        item = cls(path, **item_data)
        if item.loaded:
            found_items.append(cls)
    return found_items
