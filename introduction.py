from user_interface import *
from travel import *


player.last_direction = "South"
player.room = room1

class Intro:
    def __init__(self):
        self.window = Window()

    def intro(self):
        self.window.showMaximized()
        self.window.butt_reset()

        self.window.label.setText("Vítejte v reknamorcenovi")

        self.window.butt_1("Pokračovat", self.char_sel)

    def char_sel(self):
        self.window.butt_reset()

        self.window.label.setText("Vyberte si prosím rasu")

        self.window.butt_1("Trpaslík", self.dwarf_intro)
        self.window.butt_2("Člověk", self.human_intro)
        self.window.butt_3("Elf", self.elf_intro)
        self.window.butt_4("Informace o postavách", self.char_info)

    def char_info(self):
        self.window.label.setText("")

    def dwarf_intro(self):
        player = Dwarf()

    def human_intro(self):
        player = Human()

    def elf_intro(self):
        player = Elf()


class Moving:
    def __init__(self):
        self.room = Room()

