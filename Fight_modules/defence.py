from character_stats import *
from main_funcs import *


class DefenceConclusion:
    def defence_major_fail(self, opponent):
        slow_print("Soupeř vás těžce zranil.")
        player.health -= opponent.weapon.damage

        return

    def defence_minor_fail(self, opponent):
        slow_print("Soupeř vás lehce zranil.")
        player.health -= opponent.weapon.damage * 0.5

        return

    def defence_minor_success(self, opponent):
        slow_print("Soupeř vás nezranil")

        return

    def defence_major_success(self, opponent):
        slow_print("Soupeřův útok vás nezranil a vrátili jste mu ránu.")

        opponent.health -= player.weapon.damage

        return


class DefenceEvaluation:
    def_conc = DefenceConclusion()

    def defence_output(self, opponent, defence_type, defence_direction, strike_type, strike_dir, strike_power):
        random_num = random.randint(0, 100)
        lower_border = 25
        middle_border = 50
        higher_border = 75

        last_action = "defence"
        if random_num <= lower_border:
            self.def_conc.defence_major_fail(opponent)
            last_action = "attack"
        elif random_num <= middle_border:
            self.def_conc.defence_minor_fail(opponent)
        elif random_num <= higher_border:
            self.def_conc.defence_minor_success(opponent)
        else:
            self.def_conc.defence_major_success(opponent)

        return  last_action


class DefencePreparation:
    def_eval = DefenceEvaluation()

    opponent = Opponent()
    opponent_action = ""
    opponent_direction = ""
    opponent_power = ""

    player_action = ""
    player_direction = ""

    def opponent_attack_action(self, opponent):
        self.opponent = opponent

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
            self.opponent_action = "smash"
        elif "smash" in opponent.weapon.damage_type:
            self.opponent_action = "smash"

        return self.opponent_attack_direction()

    def opponent_attack_direction(self):
        if self.opponent_action == "stab":
            if random.randint(0, 4) < 3:
                self.opponent_direction = "body"
            else:
                self.opponent_direction = "head"
        else:
            rand_num = random.randint(0, 4)
            if rand_num < 2:
                self.opponent_direction = "belly"
            elif rand_num < 4:
                self.opponent_direction = "side"
            else:
                self.opponent_direction = "head"

        return self.opponent_attack_power()

    def opponent_attack_power(self):
        rand_num = random.randint(0, 2)

        self.opponent_power = self.opponent.attack_power[random.randint(0, len(self.opponent.attack_power) - 1)]

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
                    wrong_input(0)
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
                    wrong_input(0)

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
                    wrong_input(0)

        return self.def_eval.defence_output(self.opponent, self.player_action, self.player_direction,
                                            self.opponent_action, self.opponent_direction, self.opponent_power)
