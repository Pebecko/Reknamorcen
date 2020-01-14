from random import randint, choice
from Promts_stats.opponent_stats import Skeleton, SmallSpider, Zombie, OrkBoy
from main_funcs import slow_print, base_options, wrong_input
from character_stats import player
from Promts_stats.weapon_stats import ShortSword, ShortSwordMordhau, LongSword, LongSwordMordhau, TwoHandedSword, \
    TwoHandedSwordMordhau


class Preparation:
    def opponent_creation(self, opponent_level):
        if opponent_level == 0:
            num = 2
            if player.difficulty == "hard":
                num = 3
            opponent_level = randint(1, num)

        if opponent_level == 1:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                opponent = SmallSpider()

        elif opponent_level == 2:
            opponent_number = randint(0, 1)
            if opponent_number == 0:
                opponent = Skeleton()
            else:
                opponent = Zombie()

        elif opponent_level == 3:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                opponent = OrkBoy()

        elif opponent_level == 4:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                pass

        elif opponent_level == 5:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                pass

        else:
            opponent_number = randint(0, 0)
            if opponent_number == 0:
                pass

        opponent.health = randint(opponent.lowest_health, opponent.highest_health)
        opponent.max_health = opponent.health
        opponent.weapon = choice(opponent.weapons)
        opponent.helmet = choice(opponent.helmets)
        opponent.weapon = choice(opponent.weapons)

        return opponent

    @staticmethod
    def first_fight_action(opponent):
        loudness = opponent.awareness
        if player.last_fight is True:
            loudness += 4
        if player.char == "dwarf":
            loudness += 3
        elif player.char == "human":
            loudness += 2
        loudness += player.helmet.loudness
        loudness += player.armor.loudness
        first_opponent_action = "defence"
        if loudness > 20:
            first_opponent_action = "attack"
        elif loudness > 10:
            if randint(0, loudness) < 10:
                first_opponent_action = "attack"

        return first_opponent_action

    @staticmethod
    def special_fight_techniques():
        if "mordhau" in player.weapon.special_abilities:
            while True:
                slow_print("Chcete si meč [o]točit, abyste s ním mohli mlátit spíše než sekat, nebo [n]e??")
                style_decision = base_options()
                if style_decision == "o":
                    if player.weapon == ShortSword:
                        player.weapon = ShortSwordMordhau(player.weapon.hit_points)
                    elif player.weapon == LongSword:
                        player.weapon = LongSwordMordhau(player.weapon.hit_points)
                    elif player.weapon == TwoHandedSword:
                        player.weapon = TwoHandedSwordMordhau(player.weapon.hit_points)
                    break
                elif style_decision == "n":
                    break
                elif style_decision != "skip":
                    wrong_input()

            return
