from csv import DictReader
from pathlib import Path


def importing_dict_from_csv(file_location):
    with open(Path(__file__).parent.parent.parent / file_location, "r") as csv_file:
        return tuple(DictReader(csv_file, delimiter=";"))
