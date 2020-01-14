from Promts_stats.opponent_stats import Opponent
from Promts_stats.weapon_stats import Fists
from character_stats import player
from main_funcs import slow_print, base_options, wrong_input
import random


# TODO defence effects
class DefenceConclusion:
    def defence_major_fail(self, opponent):
        slow_print("Soupeř vás těžce zranil.")
        player.health -= 0.8 * opponent.weapon.damage

        return

    def defence_minor_fail(self, opponent):
        slow_print("Soupeř vás lehce zranil.")
        player.health -= opponent.weapon.damage * 0.4

        return

    def defence_minor_success(self, opponent):
        slow_print("Soupeř vás nezranil")

        return

    def defence_major_success(self, opponent):
        slow_print("Soupeřův útok vás nezranil a vrátili jste mu ránu.")

        opponent.health -= 0.8 * player.weapon.damage

        return


class DefenceEvaluation:
    def __init__(self):
        self.def_conc = DefenceConclusion()

        self.lower_border = 30
        self.middle_border = 60
        self.higher_border = 80

    def border_setting(self, lower_border, middle_border, higher_border):
        self.lower_border = lower_border
        self.middle_border = middle_border
        self.higher_border = higher_border

    def border_addition(self, lower_iterator=0.0, middle_iterator=0.0, higher_iterator=0.0):
        self.lower_border += lower_iterator
        self.middle_border += middle_iterator
        self.higher_border += higher_iterator

    def border_multiplication(self, number, lower_multiplier=0.0, middle_multiplier=0.0, higher_multiplier=0.0):
        self.lower_border += (number * lower_multiplier)
        self.middle_border += (number * middle_multiplier)
        self.higher_border += (number * higher_multiplier)

    def fistfight(self):
        # TODO Add fistfight
        pass

    def defence_none(self, opponent, strike_dir, strike_power):
        self.border_setting(45, -200, -200)

        if strike_dir is "head":
            self.higher_border -= 5

        self.border_multiplication(opponent.helmet.heaviness, -0.2, -0.2, -0.2)
        self.border_multiplication(opponent.helemt.visibility, -3.5, -3, -4)

        self.border_multiplication(opponent.armor.heaviness, -0.5, -0.4, -0.4)

        if strike_power == "small":
            self.higher_border += 12
        elif strike_power == "medium":
            self.higher_border -= 3
        elif strike_power == "high":
            self.higher_border -= 18

        return

    def defence_dodge(self, opponent, strike_dir, strike_power, defence_dir):
        if opponent.weapon.weapon_class == "unarmed":
            self.border_setting(40, 80, 90)
        elif opponent.weapon.weapon_type == "light":
            self.border_setting(35, 65, 85)
        elif opponent.weapon.weapon_type == "medium":
            self.border_setting(20, 55, 75)
        else:
            self.border_setting(10, 40, 70)

        if player.weapon.weapon_class == "unarmed":
            self.border_addition(-8, -9, -8)
        elif player.weapon.weapon_type == "light":
            self.border_addition(-4, -6, -5)
        elif player.weapon.weapon_type == "medium":
            self.border_addition(2, 3, 3.5)
        elif player.weapon.weapon_type == "heavy":
            self.border_addition(6, 8, 9)
        elif player.weapon.weapon_type == "super_heavy":
            self.border_addition(11, 14, 17)

        if defence_dir == "back":
            if strike_dir == "body" or strike_dir == "head":
                self.border_addition(9, 12, 11)
            else:
                self.border_addition(-11, -15, -14)
        elif defence_dir == "left":
            if strike_dir == "belly":
                self.border_addition(12, 15, 13)
            elif strike_dir == "body" or strike_dir == "head":
                self.border_addition(-13, -18, -17)
            else:
                self.border_addition(-10, -17, -13)
        else:
            if strike_dir == "side":
                self.border_addition(11, 14, 13)
            elif strike_dir == "body" or strike_dir is "head":
                self.border_addition(-11, -17, -16)
            else:
                self.border_addition(-9, -16, -15)

        self.border_multiplication(opponent.helmet.heaviness, -0.3, -0.2, -0.2)
        self.border_multiplication(opponent.helmet.visibility, -3, -2.5, -3)

        self.border_multiplication(opponent.armor.heaviness, -0.3, -0.4, -0.4)

        self.border_multiplication(player.helmet.heaviness, 0.7, 0.8, 0.9)
        self.border_multiplication(player.helmet.visibility, 1, 1.5, 1.5)

        self.border_multiplication(player.armor.heaviness, 1, 1.2, 1.3)

        if strike_power == "small":
            self.border_addition(7, 9, 8)
        elif strike_power == "medium":
            self.border_addition(-3, -4, -3)
        elif strike_power == "high":
            self.border_addition(-9, -13, -11)

        if "extra_dodge" in player.weapon.special_abilities:
            self.border_addition(-4, -5, -5)
        if "weak_dodge" in player.weapon.special_abilities:
            self.border_addition(4, 5, 5)

        if "extra_dodge" in player.helmet.special_abilities:
            self.border_addition(-3, -4, -4)
        if "weak_dodge" in player.weapon.special_abilities:
            self.border_addition(3, 4, 4)

        if "extra_dodge" in player.armor.special_abilities:
            self.border_addition(-5, -6, -6)
        if "weak_dodge" in player.weapon.special_abilities:
            self.border_addition(5, 6, 6)

        return self.opponent_char_effects(opponent)

    def defence_block(self, opponent, strike_dir, strike_power, defence_dir):
        # TODO Finish block level changing
        return self.opponent_char_effects(opponent)

    def opponent_char_effects(self, opponent):
        # TODO Finnish opponent char effects
        return self.player_char_effects()

    def player_char_effects(self):
        # TODO Finnish player char effects
        return

    def defence_output(self, opponent, defence_type, defence_dir, strike_type, strike_dir, strike_power):
        # TODO Make def output cleaner
        # generating random number
        random_num = random.randint(0, 100)

        # editing of levels
        if defence_type == "":
            self.defence_none(opponent, strike_dir, strike_power)
        elif player.weapon == Fists():
            self.fistfight()
        elif defence_type == "dodge":
            self.defence_dodge(opponent, strike_dir, strike_power, defence_dir)
        else:
            if opponent.weapon != opponent.unarmed_weapon and player.weapon == Fists():
                self.defence_none(opponent, strike_dir, strike_power)
            self.defence_block(opponent, strike_dir, strike_power, defence_dir)

        if player.difficulty == "easy":
            self.border_addition(-10, -10, -10)
        if player.difficulty == "nightmare":
            self.border_addition(5, 5, 5)

        # borders rounding part
        self.lower_border = round(self.lower_border, 1)
        self.middle_border = round(self.middle_border, 1)
        self.higher_border = round(self.higher_border, 1)

        # debug part
        if player.test is True:
            print(random_num, self.lower_border, self.middle_border, self.higher_border)

        # result
        last_action = "defence"
        if random_num <= self.lower_border:
            self.def_conc.defence_major_fail(opponent)
        elif random_num <= self.middle_border:
            self.def_conc.defence_minor_fail(opponent)
        elif random_num <= self.higher_border:
            self.def_conc.defence_minor_success(opponent)
        else:
            last_action = "attack"
            self.def_conc.defence_major_success(opponent)

        return last_action


class DefencePreparation:
    def __init__(self):
        self.def_eval = DefenceEvaluation()

        self.opponent = Opponent()
        self.opponent_action = ""
        self.opponent_direction = ""
        self.opponent_power = ""

        self.player_action = ""
        self.player_direction = ""

    def opponent_attack_action(self, opponent):
        self.opponent = opponent

        # TODO Make proper action choosing AI
        if "cut" in opponent.weapon.damage_type and "stab" in opponent.weapon.damage_type:
            if random.randint(0, 4) < 3:
                self.opponent_action = "cut"
            else:
                self.opponent_action = "stab"
        elif "cut" in opponent.weapon.damage_type:
            self.opponent_action = "cut"
        elif "stab" in opponent.weapon.damage_type:
            self.opponent_action = "stab"
        elif opponent.weapon.weapon_class == "unarmed":
            self.opponent_action = "punch"
        elif "smash" in opponent.weapon.damage_type:
            self.opponent_action = "smash"

        return self.opponent_attack_direction()

    def opponent_attack_direction(self):
        # TODO Make proper direction choosing AI
        if self.opponent_action == "stab" or self.opponent_action == "punch":
            if random.randint(0, 4) < 3:
                self.opponent_direction = "body"
            else:
                self.opponent_direction = "head"
        else:
            rand_num = random.randint(0, 7)
            if rand_num < 3:
                self.opponent_direction = "belly"
            elif rand_num < 6:
                self.opponent_direction = "side"
            else:
                self.opponent_direction = "head"

        return self.opponent_attack_power()

    def opponent_attack_power(self):
        # TODO Make proper power choosing AI
        self.opponent_power = self.opponent.attack_power[random.randint(0, len(self.opponent.attack_power) - 1)]

        if player.test is True:
            print(self.opponent_action, "-", self.opponent_direction, "-", self.opponent_power)

        return self.defence_action_choosing()

    def defence_action_choosing(self):
        # hráč si vybírá jestli bude krýt nebo uskakovat
        if player.weapon.weapon_type != "unarmed":
            while True:
                defence_type_options = base_options("Chcete soupeřův úder [b]lokovat, nebo se mu pokusit [v]yhnout?\n")
                if defence_type_options == "b":
                    self.player_action = "block"
                    break
                elif defence_type_options == "v":
                    self.player_action = "dodge"
                    break
                elif defence_type_options != "skip":
                    wrong_input()
        elif self.opponent.weapon.weapon_type == "unarmed":
            self.player_action = "dodge"
        else:
            slow_print("Beze zbraně nemůžete krýt soupeřův útok musíte uhnout!\n")
            self.player_action = "dodge"

        return self.defence_direction_choosing()

    def defence_direction_choosing(self):
        if self.player_action == "block":
            while True:
                block_direction = base_options("Myslíte, že soupeř zaútočí na [b]řicho, b[o]k, [h]lavu, nebo se bude"
                                               " snažit bo[d]at?\n")
                if block_direction == "b":
                    self.player_direction = "kvarta"
                    break
                elif block_direction == "o":
                    self.player_direction = "terca"
                    break
                elif block_direction == "h":
                    self.player_direction = "kvinta"
                    break
                elif block_direction == "d":
                    self.player_direction = "second"
                    break
                elif block_direction != "skip":
                    wrong_input()

        else:  # defence_type == "dodge"
            while True:
                dodge_direction = base_options("Chcete uskočil v[l]evo, v[p]ravo, nebo do[z]adu?\n")
                if dodge_direction == "l":
                    self.player_direction = "left"
                    break
                elif dodge_direction == "p":
                    self.player_direction = "right"
                    break
                elif dodge_direction == "z":
                    self.player_direction = "back"
                    break
                elif dodge_direction != "skip":
                    wrong_input()

        return self.def_eval.defence_output(self.opponent, self.player_action, self.player_direction,
                                            self.opponent_action, self.opponent_direction, self.opponent_power)
