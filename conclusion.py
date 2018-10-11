from character_stats import *
from main_funcs import *


class Conclusion:
    def returning_from_technique(self):
        if player.weapon is short_sword_mordhau:
            player.weapon = short_sword

        return self.end_call()

    def end_call(self):
        end_call = random.randint(0, 1)
        if end_call == 0:
            slow_print("Zabili jste ho.\n")
        elif end_call == 1:
            slow_print("Tohle už nepřežil.\n")

        return
