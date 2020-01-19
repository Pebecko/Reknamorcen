from game.character_stats.player_stats import player
from game.important_modules.main_funcs import slow_print
from random import randint
from game.equipment_stats.weapon_stats import ShortSword, ShortSwordMordhau, LongSword, LongSwordMordhau, TwoHandedSword, \
    TwoHandedSwordMordhau



class Conclusion:
    def returning_from_technique(self):
        if player.weapon == ShortSwordMordhau:
            player.weapon = ShortSword(player.weapon.hit_points)
        elif player.weapon == LongSwordMordhau:
            player.weapon = LongSword(player.weapon.hit_points)
        elif player.weapon == TwoHandedSwordMordhau:
            player.weapon = TwoHandedSword(player.weapon.hit_points)

        return self.end_call()

    def end_call(self):
        # TODO Upgrade end calls
        end_call = randint(0, 1)
        if end_call == 0:
            slow_print("Zabili jste ho.\n")
        elif end_call == 1:
            slow_print("Tohle už nepřežil.\n")

        return
