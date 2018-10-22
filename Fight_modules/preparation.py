from character_stats import *
from main_funcs import *


class Preparation:
    def opponent_creation(self, opponent_level):
        if opponent_level == 0:
            num = 2
            if player.difficulty == "hard":
                num = 3
            opponent_level = random.randint(1, num)

        if opponent_level == 1:
            opponent_number = random.randint(0, 0)
            if opponent_number == 0:
                opponent = opponent_7

        elif opponent_level == 2:
            opponent_number = random.randint(0, 1)
            if opponent_number == 0:
                opponent = opponent_3
            else:
                opponent = opponent_5

        elif opponent_level == 3:
            opponent_number = random.randint(0, 0)
            if opponent_number == 0:
                opponent = opponent_1

        elif opponent_level == 4:
            opponent_number = random.randint(0, 0)
            if opponent_number == 0:
                pass

        elif opponent_level == 5:
            opponent_number = random.randint(0, 0)
            if opponent_number == 0:
                pass

        else:
            opponent_number = random.randint(0, 0)
            if opponent_number == 0:
                pass

        opponent.health = random.randint(opponent.lowest_health, opponent.highest_health)
        opponent.max_health = opponent.health
        opponent.weapon = opponent.weapons[random.randint(0, len(opponent.weapons) - 1)]
        opponent.helmet = opponent.helmets[random.randint(0, len(opponent.helmets) - 1)]
        opponent.weapon = opponent.weapons[random.randint(0, len(opponent.armors) - 1)]

        return opponent

    def first_fight_action(self, opponent):
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
            if random.randint(0, loudness) < 10:
                first_opponent_action = "attack"

        return first_opponent_action

    def special_fight_techniques(self):
        if "mordhau" in player.weapon.special_abilities:
            while True:
                slow_print("Chcete si meč [o]točit, abyste s ním mohli mlátit spíše než sekat, nebo [n]e??")
                style_decision = base_options()
                if style_decision == "o":
                    if player.weapon == short_sword:
                        player.weapon = short_sword_mordhau
                    elif player.weapon == long_sword:
                        player.weapon = long_sword_mordhau
                    elif player.weapon == two_handed_sword:
                        player.weapon = two_handed_sword_mordhau
                    break
                elif style_decision == "n":
                    break
                elif style_decision != "skip":
                    wrong_input(0)

            return
