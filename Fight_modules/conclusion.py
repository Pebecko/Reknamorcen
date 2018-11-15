from character_stats import *
from main_funcs import *


class Conclusion:
    def returning_from_technique(self):
        if player.weapon == short_sword_mordhau:
            player.weapon = short_sword
        elif player.weapon == long_sword_mordhau:
            player.weapon = long_sword
        elif player.weapon == two_handed_sword_mordhau:
            player.weapon = two_handed_sword

        return self.end_call()

    def end_call(self):
        # TODO Upgrade end calls
        end_call = random.randint(0, 1)
        if end_call == 0:
            slow_print("Zabili jste ho.\n")
        elif end_call == 1:
            slow_print("Tohle už nepřežil.\n")

        return
