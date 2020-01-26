from game.important_modules.main_funcs import slow_print
from random import randint
from game.equipment_stats.weapon_stats import ShortSword, ShortSwordMordhau, LongSword, LongSwordMordhau, TwoHandedSword, \
    TwoHandedSwordMordhau


class Conclusion:
    def __init__(self, player):
        self.player = player

    def main(self):
        self.returning_from_technique()

        self.end_call()

        return

    # TODO - Make mordhau automatic
    def returning_from_technique(self):
        if isinstance(self.player.weapon, ShortSwordMordhau):
            self.player.weapon = ShortSword(self.player.weapon.hit_points)
        elif isinstance(self.player.weapon, LongSwordMordhau):
            self.player.weapon = LongSword(self.player.weapon.hit_points)
        elif isinstance(self.player.weapon, TwoHandedSwordMordhau):
            self.player.weapon = TwoHandedSword(self.player.weapon.hit_points)

        return

    @staticmethod
    def end_call():
        # TODO Upgrade end calls
        end_call = randint(0, 1)
        if end_call == 0:
            slow_print("Zabili jste ho.\n")
        elif end_call == 1:
            slow_print("Tohle už nepřežil.\n")

        return
