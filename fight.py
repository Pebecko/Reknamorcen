from Reknamorcen.character_stats import *
from Reknamorcen.main_funcs import *


class Preparation:
    def opponent_creation(self, opponent_level):
        if opponent_level == 0:
            num = 2
            if player.difficulty == "hard":
                num = 3
            opponent_difficulty = random.randint(1, num)

        if opponent_level == 1:
            opponent_number = random.randint(0, 1)
            if opponent_number == 0:
                self.opponent = "kostlivec"
                self.opponent_health = random.randint(5, 7)
                self.opponent_info = ""
                self.opponent_defence = ["block"]

                opponent_weapon_number = random.randint(1, 2)
                if opponent_weapon_number == 1:
                    self.opponent_weapon = "se zrezlým mečem"
                    self.opponent_weapon_type = "light"
                    self.opponent_damage_type = ["cut"]
                    self.opponent_strength = 4
                elif opponent_weapon_number == 2:
                    self.opponent_weapon = "beze zbraně"
                    self.opponent_weapon_type = "light"
                    self.opponent_damage_type = ["smash"]
                    self.opponent_strength = 2

            elif opponent_number == 1:
                self.opponent = "pavouk"
                self.opponent_health = random.randint(3, 5)
                self.opponent_info = ""
                self.opponent_weapon = "s kusadly"
                self.opponent_weapon_type = "light"
                self.opponent_defence = ["dodge"]
                self.opponent_damage_type = ["stab"]
                self.opponent_strength = random.randint(3, 5)

            elif opponent_number == 2:
                self.opponent = "goblin"

        elif opponent_level == 2:
            opponent_number = random.randint(0, 0)
            if opponent_number == 0:
                ork.health = random.randint(ork.lowest_health, ork.highest_health)
                ork.max_health = ork.health
                ork.weapon = two_handed_axe
                ork.helmet = rusty_ork_helmet
                opponent = ork

                opponent_weapon_number = random.randint(0, 1)
                if opponent_weapon_number == 0:
                    self.opponent_weapon = "s ohromným sekáčkem"
                    self.opponent_weapon_type = "heavy"
                    self.opponent_damage_type = ["cut"]
                    self.opponent_strength = 6
                elif opponent_weapon_number == 1:
                    self.opponent_weapon = "beze zbraně"
                    self.opponent_weapon_type = "light"
                    self.opponent_damage_type = ["smash"]
                    self.opponent_strength = 3
                    self.opponent_defence = ["dodge"]

        elif opponent_level == 3:
            opponent_number = random.randint(0, 0)
            if opponent_number == 0:
                self.opponent = "trol"
                self.opponent_health = random.randint(35, 50)
                self.opponent_info = ""
                self.opponent_defence = []

                opponent_weapon_number = random.randint(0, 1)
                if opponent_weapon_number == 0:
                    self.opponent_weapon = "s tunelovým sloupem"
                    self.opponent_weapon_type = "heavy"
                    self.opponent_damage_type = ["smash"]
                    self.opponent_strength = random.randint(12, 16)
                elif opponent_weapon_number == 1:
                    self.opponent_weapon = "beze zbraně"
                    self.opponent_weapon_type = "heavy"
                    self.opponent_damage_type = ["smash"]
                    self.opponent_strength = random.randint(8, 10)

        else:
            self.opponent = "reknamorcenova stráž"
            self.opponent_health = random.randint(12, 18)
            self.opponent_info = ""
            self.opponent_defence = ["dodge", "block"]
            self.opponent_gear = ["helmet", "armor"]
            opponent_weapon_number = random.randint(0, 1)
            if opponent_weapon_number == 0:
                self.opponent_weapon = "s obouručním mečem"
                self.opponent_stamina = random.randint(5, 7)
                self.opponent_stamina_growth = random.randint(1, 3) / 2
                self.opponent_weapon_type = "heavy"
                self.opponent_damage_type = ["stab", "cut"]
                self.opponent_strength = 9
            elif opponent_weapon_number == 1:
                self.opponent_weapon = "s krátkým mečem"
                self.opponent_stamina = random.randint(6, 8)
                self.opponent_stamina_growth = random.randint(2, 4) / 2
                self.opponent_weapon_type = "light"
                self.opponent_damage_type = ["stab", "cut"]
                self.opponent_strength = 6

        return opponent

    def first_fight_action(self, opponent):
        loudness = 0
        loudness += opponent.awareness
        if player.char == "dwarf":
            loudness += 3
        elif player.char == "human":
            loudness += 2
        loudness += player.helmet.loudness
        loudness += player.armor.loudness
        first_opponent_action = "defence"
        if loudness > 16:
            first_opponent_action = "attack"
        elif loudness > 8:
            if random.randint(0, loudness) < 8:
                first_opponent_action = "attack"

        return first_opponent_action

    def special_fight_techniques(self):
        if "mordhau" in player.weapon.special_abilities:
            while True:
                slow_print("Chcete si meč [o]tčit, abyste s ním molhy mlátit spíše než sekat, nebo [n]e??")
                style_decision = base_options()
                if style_decision == "o":
                    player.weapon = short_sword_mordhau
                    break
                elif style_decision == "n":
                    break
                elif style_decision != "skip":
                    wrong_input(0)

            return


class Attack:
    last_attack_zone = ""
    opponent_action = ""
    opponent_last_action_I = ""
    opponent_last_action_II = ""
    opponent_direction = ""
    opponent_last_direction_I = ""
    opponent_last_direction_II = ""
    player_attack_direction = ""
    player_last_attack_direction_I = ""
    player_last_attack_direction_II = ""
    player_attack_type = ""
    player_last_attack_type_I = ""
    player_last_attack_type_II = ""

    def strike_direction_choosing(self, opponent):
        strike_type = "stab"
        strike_dir = "body"
        if "cut" and "stab" in player.weapon.damage_type:
            while True:
                slow_print("Chcete [b]odat, nebo [s]ekat?")
                attack_type = base_options()
                if attack_type == "b":
                    while True:
                        slow_print("Chcete bodat do [t]ěla, nebo na [h]lavu?")
                        attack_direction = base_options()
                        if attack_direction == "t":
                            break
                        elif attack_direction == "h":
                            strike_dir = "head"
                            break
                        elif attack_direction != "skip":
                            wrong_input(0)
                    break
                elif attack_type == "s":
                    strike_type = "cut"
                    while True:
                        slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
                        attack_direction = base_options()
                        if attack_direction == "o":
                            strike_dir = "side"
                            break
                        elif attack_direction == "b":
                            strike_dir = "belly"
                            break
                        elif attack_direction == "h":
                            strike_dir = "head"
                            break
                        elif attack_direction != "skip":
                            wrong_input(0)
                    break
                elif attack_type != "skip":
                    wrong_input(0)
        elif "stab" in player.weapon.damage_type:
            while True:
                slow_print("Chcete bodat do [t]ěla, nebo na [h]lavu?")
                attack_direction = base_options()
                if attack_direction == "t":
                    break
                elif attack_direction == "h":
                    strike_dir = "head"
                    break
                elif attack_direction != "skip":
                    wrong_input(0)
        elif "cut" in player.weapon.damage_type:
            strike_type = "cut"
            while True:
                slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
                attack_direction = base_options()
                if attack_direction == "h":
                    strike_dir = "head"
                    break
                elif attack_direction == "o":
                    strike_dir = "side"
                    break
                elif attack_direction == "b":
                    strike_dir = "belly"
                    break
                elif attack_direction != "skip":
                    wrong_input(0)
        elif player.weapon is fists:
            strike_type = "punch"
            while True:
                slow_print("Chcete ho praštit do [h]lavy, nebo do [b]řicha?")
                attack_direction = base_options()
                if attack_direction == "b":
                    break
                elif attack_direction == "h":
                    strike_dir = "head"
                    break
                elif attack_direction != "skip":
                    wrong_input(0)
        elif "smash" in player.weapon.damage_type:
            strike_type = "smash"
            while True:
                slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
                attack_direction = base_options()
                if attack_direction == "o":
                    strike_dir = "side"
                    break
                elif attack_direction == "b":
                    strike_dir = "belly"
                    break
                elif attack_direction == "h":
                    strike_dir = "head"
                    break
                elif attack_direction != "skip":
                    wrong_input(0)

        return self.attack_output(strike_type, strike_dir, opponent)

    def opponent_defence_action(self, opponent, strike_dir):
        # opponent action choosing
        if opponent.defence is []:
            self.opponent_action = ""
        elif "dodge" in opponent.defence and "block" not in opponent.defence:
            self.opponent_action = "dodge"
        elif "block" in opponent.defence and "dodge" not in opponent.defence:
            self.opponent_action = "block"
        else:
            opponent_action_num = random.randint(0, 39)
            split = 20
            # player weapon effects
            if "stab" in player.weapon.damage_type:
                split += 1
            if player.weapon.weapon_type is "light":
                split += 4
            elif player.weapon.weapon_type is "heavy":
                split -= 4

            # opponent weapon effects
            if opponent.weapon.weapon_type is "light":
                split -= 2
            elif opponent.weapon.weapon_type is "heavy":
                split += 2

            # last player attack types effects
            if self.player_last_attack_type_II is "stab":
                split -= 2
            if self.player_last_attack_type_I is "stab":
                split -= 3
            if self.player_attack_type is "stab":
                split -= 4

            self.player_last_attack_type_II = self.player_last_attack_type_I
            self.player_last_attack_type_I = self.player_attack_type
            self.player_attack_type = strike_dir

            # opponent last actions effects
            if self.opponent_last_action_II is "dodge":
                split += 1
            elif self.opponent_last_action_II is "block":
                split -= 1
            if self.opponent_last_action_I is "dodge":
                split += 2
            elif self.opponent_last_action_I is "block":
                split -= 2
            if self.opponent_action is "dodge":
                split += 3
            elif self.opponent_action is "block":
                split -= 3

            self.opponent_last_action_II = self.opponent_last_action_I
            self.opponent_last_action_I = self.opponent_action

            if opponent_action_num < split:
                self.opponent_action = "block"
            else:
                self.opponent_action = "dodge"

        # opponent defence direction choosing
        if self.opponent_action is "dodge":
            direction_num = random.randint(0, 59)
            lower_split = 20
            higher_split = 40

            # changing levels depending on last opponents directions
            if self.opponent_last_direction_II is "left" or self.opponent_last_direction_II is "terca":
                lower_split -= 2
                higher_split -= 1
            elif self.opponent_last_direction_II is "back" or self.opponent_last_direction_II is "kvinta":
                lower_split += 1
                higher_split -= 1
            elif self.opponent_last_direction_II is "right" or self.opponent_last_direction_II is "kvarta":
                lower_split += 1
                higher_split += 2

            if self.opponent_last_direction_I is "left" or self.opponent_last_direction_I is "terca":
                lower_split -= 2
                higher_split -= 1
            elif self.opponent_last_direction_I is "back" or self.opponent_last_direction_I is "kvinta":
                lower_split += 1
                higher_split -= 1
            elif self.opponent_last_direction_I is "right" or self.opponent_last_direction_I is "kvarta":
                lower_split += 1
                higher_split += 2

            if self.opponent_direction is "left" or self.opponent_direction is "terca":
                lower_split -= 4
                higher_split -= 2
            elif self.opponent_direction is "back" or self.opponent_direction is "kvinta":
                lower_split += 2
                higher_split -= 2
            elif self.opponent_direction is "right" or self.opponent_direction is "kvarta":
                lower_split += 2
                higher_split += 4

            # changing levels depending on last players directions
            if self.player_last_attack_direction_II is "body" or self.player_last_attack_direction_II is "head":
                lower_split += 3
                higher_split -= 3
            elif self.player_last_attack_direction_II is "side":
                lower_split -= 2
                higher_split += 1
            elif self.player_last_attack_direction_II is "belly":
                lower_split -= 1
                higher_split += 2

            if self.player_last_attack_direction_I is "body" or self.player_last_attack_direction_I is "head":
                lower_split += 4
                higher_split -= 4
            elif self.player_last_attack_direction_I is "side":
                lower_split -= 4
                higher_split += 2
            elif self.player_last_attack_direction_I is "belly":
                lower_split -= 2
                higher_split += 4

            if self.player_attack_direction is "body" or self.player_attack_direction is "head":
                lower_split += 5
                higher_split -= 5
            elif self.player_attack_direction is "side":
                lower_split -= 6
                higher_split += 3
            elif self.player_attack_direction is "belly":
                lower_split -= 3
                higher_split += 6

            if self.player_attack_direction is "body" or self.player_attack_direction is "head":
                lower_split += 5
                higher_split -= 5
            elif self.player_attack_direction is "side":
                lower_split -= 6
                higher_split += 3
            elif self.player_attack_direction is "belly":
                lower_split -= 3
                higher_split += 6

            self.opponent_last_direction_II = self.opponent_last_direction_I
            self.opponent_last_direction_I = self.opponent_direction

            self.player_last_attack_direction_II = self.player_last_attack_direction_I
            self.player_last_attack_direction_I = self.player_attack_direction
            self.player_attack_direction = strike_dir

            if direction_num < lower_split:
                self.opponent_direction = "left"
            elif direction_num < higher_split:
                self.opponent_direction = "back"
            else:
                self.opponent_direction = "right"
        elif self.opponent_action is "block":
            direction_num = random.randint(0, 64)
            lower_split = 20
            higher_split = 40
            special_split = 60

            if "stab" in player.weapon.damage_type:
                lower_split -= 1
                higher_split -= 2
                special_split -= 3

            # changing levels depending on last opponents directions
            if self.opponent_last_direction_II is "left" or self.opponent_last_direction_II is "terca":
                lower_split -= 2
                higher_split -= 1
            elif self.opponent_last_direction_II is "back" or self.opponent_last_direction_II is "kvinta":
                lower_split += 1
                higher_split -= 1
            elif self.opponent_last_direction_II is "right" or self.opponent_last_direction_II is "kvarta":
                lower_split += 1
                higher_split += 2
            elif self.opponent_last_direction_II is "second":
                lower_split += 2
                higher_split += 1
                special_split += 3

            if self.opponent_last_direction_I is "left" or self.opponent_last_direction_I is "terca":
                lower_split -= 2
                higher_split -= 1
            elif self.opponent_last_direction_I is "back" or self.opponent_last_direction_I is "kvinta":
                lower_split += 1
                higher_split -= 1
            elif self.opponent_last_direction_I is "right" or self.opponent_last_direction_I is "kvarta":
                lower_split += 1
                higher_split += 2
            elif self.opponent_last_direction_I is "second":
                lower_split += 2
                higher_split += 1
                special_split += 3

            if self.opponent_direction is "left" or self.opponent_direction is "terca":
                lower_split -= 4
                higher_split -= 2
            elif self.opponent_direction is "back" or self.opponent_direction is "kvinta":
                lower_split += 2
                higher_split -= 2
            elif self.opponent_direction is "right" or self.opponent_direction is "kvarta":
                lower_split += 2
                higher_split += 4
            elif self.opponent_direction is "second":
                lower_split += 4
                higher_split += 2
                special_split += 6

            # changing levels depending on last players directions
            if self.player_last_attack_direction_II is "body":
                lower_split -= 3
                higher_split -= 6
                special_split -= 9
            elif self.player_last_attack_direction_II is "side":
                lower_split += 4
                higher_split += 2
            elif self.player_last_attack_direction_II is "belly":
                lower_split -= 2
                higher_split -= 4
            elif self.player_last_attack_direction_II is "head":
                lower_split -= 2
                higher_split += 2

            if self.player_last_attack_direction_I is "body":
                lower_split -= 4
                higher_split -= 8
                special_split -= 12
            elif self.player_last_attack_direction_I is "side":
                lower_split += 6
                higher_split += 3
            elif self.player_last_attack_direction_I is "belly":
                lower_split -= 3
                higher_split -= 6
            elif self.player_last_attack_direction_I is "head":
                lower_split -= 3
                higher_split += 3

            if self.player_attack_direction is "body":
                lower_split -= 5
                higher_split -= 10
                special_split -= 15
            elif self.player_attack_direction is "side":
                lower_split += 8
                higher_split += 4
            elif self.player_attack_direction is "belly":
                lower_split -= 4
                higher_split -= 8
            elif self.player_attack_direction is "head":
                lower_split -= 4
                higher_split += 4

            self.opponent_last_direction_II = self.opponent_last_direction_I
            self.opponent_last_direction_I = self.opponent_direction

            self.player_last_attack_direction_II = self.player_last_attack_direction_I
            self.player_last_attack_direction_I = self.player_attack_direction
            self.player_attack_direction = strike_dir

            if direction_num < lower_split:
                self.opponent_direction = "terca"
            elif direction_num < higher_split:
                self.opponent_direction = "kvinta"
            elif direction_num < special_split:
                self.opponent_direction = "kvarta"
            else:
                self.opponent_direction = "second"

        # action debug
        if player.test is True:
            print(self.opponent_action, "-", self.opponent_direction, ",", self.opponent_last_action_I, "-",
                  self.opponent_last_direction_I, ",", self.opponent_last_action_II, "-",
                  self.opponent_last_direction_II)

        return

    def attack_major_fail(self, strike_dir, opponent):
        multiplier = 1
        if self.opponent_action == "block":
            if random.randint(0, 4) == 0:
                block_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
            elif random.randint(0, 3) != 0:
                block_output = "Ale váš útok trval příliš dlouho byl příliš čitelný takže vaši ránu vykryl."
                opponent.weapon.hit_points -= 2 * player.weapon.damage
            else:
                block_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"

            if self.opponent_direction == "terca":
                block_message = "bok"
                if strike_dir == "side":
                    block_output = "A tak se mu povedlo váš útok zablokovat"
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif self.opponent_direction == "kvinta":
                block_message = "hlavu"
                if strike_dir == "head":
                    block_output = "A tak se mu povedlo váš útok zablokovat"
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif self.opponent_direction == "kvarta":
                block_message = "břicho"
                if strike_dir == "belly":
                    block_output = "A tak se mu povedlo váš útok zablokovat"
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            else:
                block_message = "proti bodání"
                block_output = "A jak vytáčel svou zbraň tak zachytil tu vaši a tím odklonil váš úder"
                opponent.weapon.hit_points -= 0.5 * player.weapon.damage

            slow_print("Soupeř se snažil krýt {}. {}.".format(block_message, block_output))
        else:
            if self.opponent_direction == "left":
                dodge_message = "doleva"
                if strike_dir == "belly":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku."
            elif self.opponent_direction == "back":
                dodge_message = "dozadu"
                if strike_dir == "head" or strike_dir == "body":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku."
            else:
                dodge_message = "doprava"
                if strike_dir == "side":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku."
            slow_print("Soupeř se snažil uhnout {}. {}.".format(dodge_message, dodge_output))

        if player.helmet.name != "" and player.armor.name == "":
            slow_print("Poté co váš útok nezasáhl soupeře vás nechal plně odkrytého a tím dal soupeři možnost vás"
                       " zasáhnout plnou silou. Váš soupeř se rozhodl vám jít po těle.\n")
            if "smash" in opponent.weapon.damage_type:
                multiplier -= player.armor.smash_damage_reduction * 0.05
            elif "cut" in opponent.weapon.damage_type:
                multiplier -= player.armor.cut_damage_reduction * 0.09
            elif "stab" in opponent.weapon.damage_type:
                multiplier -= player.armor.stab_damage_reduction * 0.09
        else:
            slow_print("Váš nepovedený útok vás nechal úplně otevřeného soupeřovým útokům, na to byl váš soupeř"
                       " připraven a tak vám ihned zasadil ránu do hlavy.\n")
            multiplier += 0.2
            if "smash" in opponent.weapon.damage_type:
                multiplier -= player.helmet.smash_damage_reduction * 0.05
            elif "cut" in opponent.weapon.damage_type:
                multiplier -= player.helmet.cut_damage_reduction * 0.09
            elif "stab" in opponent.weapon.damage_type:
                multiplier -= player.helmet.stab_damage_reduction * 0.09

        player.health -= multiplier * opponent.weapon.damage

        return

    def attack_minor_fail(self, strike_dir, opponent):
        if self.opponent_action == "block":
            if random.randint(0, 5) == 0:
                block_output = "Ale vám se nepodařilo odhadnout vzdálenost a tak jste promáchli"
            elif random.randint(0, 4) != 0:
                block_output = "Ale váš útok trval příliš dlouho a byl příliš čitelný" \
                               " takže si počkal a vykryl vaši ránu."
                opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif opponent.helmet.name != "" and strike_dir == "head" and self.opponent_direction != "kvinta":
                block_output = "Ale na poslední chvíli stihl zdvihnout zbraň a čásstečně vám úder vykrýt a tu sílu" \
                               " kterou nevykryl zbraní absorbovala jeho helma."
                opponent.weapon.hit_points -= player.weapon.damage
                opponent.helmet.hit_points -= 1.5 * player.weapon.damage
            else:
                block_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"

            if self.opponent_direction == "terca":
                block_message = "bok"
                if strike_dir == "side":
                    block_output = "Takže vám vaši ránu vykryl."
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif self.opponent_direction == "kvinta":
                block_message = "hlavu"
                if strike_dir == "head":
                    block_output = "Takže vám vaši ránu vykryl."
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            elif self.opponent_direction == "kvarta":
                block_message = "břicho"
                if strike_dir == "belly":
                    block_output = "Takže vám vaši ránu vykryl."
                    opponent.weapon.hit_points -= 2 * player.weapon.damage
            else:
                block_message = "proti bodání"
                block_output = "A jak vytáčel svou zbraň tak zachytil tu vaši a tím odklonil váš úder"
                opponent.weapon.hit_points -= 0.5 * player.weapon.damage

            slow_print("Váš soupeř se snažil krýt {}. {}.".format(block_message, block_output))
        else:
            if self.opponent_direction == "left":
                dodge_message = "doleva"
                if strike_dir == "belly":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš zbrklý a tak se vám nepodařilo odhadnout správně" \
                                       " vzdálenost, takže jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku."
            elif self.opponent_direction == "back":
                dodge_message = "dozadu"
                if strike_dir == "head" or strike_dir == "body":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš zbrklý a tak se vám nepodařilo odhadnout správně" \
                                       " vzdálenost, takže jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku."
            else:
                dodge_message = "doprava"
                if strike_dir == "side":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš zbrklý a tak se vám nepodařilo odhadnout správně" \
                                       " vzdálenost, takže jste promáchli"
                    else:
                        dodge_output = "Ale vaše zbraň vám trochu sklouzla v prstech a netrefili jste se"
                else:
                    dodge_output = "A tak se mu povedlo vyhnout se vašemu útoku."

            slow_print("Soupeř se snažil uhnout {}. {}.".format(dodge_message, dodge_output))

        slow_print("Měli jste ovšem štěstí, protože soupeř svoji obranu provedl dosti nešikovně, byl celý ztuhlý a mimo"
                   " bylanc, takže když viděl že vy jste se po útoku ihned vzpamatovali, ani se nepokoušel odseknout\n")

        return

    def attack_minor_success(self, strike_dir, strike_type, opponent):
        multiplier = 0.5
        slow_print("Váš útok supeře jen lehce zranil.\n")

        if strike_dir == "head":
            if strike_type == "cut":
                multiplier -= opponent.helmet.cut_damage_reduction * 0.05
            elif strike_type == "smash":
                multiplier -= opponent.helmet.smash_damage_reduction * 0.03
            elif strike_type == "stab":
                multiplier -= opponent.helmet.stab_damage_reduction * 0.05
        else:
            if strike_type == "cut":
                multiplier -= opponent.armor.cut_damage_reduction * 0.05
            elif strike_type == "smash":
                multiplier -= opponent.armor.smash_damage_reduction * 0.03
            elif strike_type == "stab":
                multiplier -= opponent.armor.stab_damage_reduction * 0.05

        opponent.health -= multiplier * player.weapon.damage

    def attack_major_success(self, strike_dir, strike_type, opponent):
        multiplier = 1
        slow_print("Váš útok supeře těžce zranil.\n")
        if strike_dir == "head":
            if strike_type == "cut":
                multiplier -= opponent.helmet.cut_damage_reduction * 0.09
            elif strike_type == "smash":
                multiplier -= opponent.helmet.smash_damage_reduction * 0.06
            elif strike_type == "stab":
                multiplier -= opponent.helmet.stab_damage_reduction * 0.09
        else:
            if strike_type == "cut":
                multiplier -= opponent.armor.cut_damage_reduction * 0.09
            elif strike_type == "smash":
                multiplier -= opponent.armor.smash_damage_reduction * 0.06
            elif strike_type == "stab":
                multiplier -= opponent.armor.stab_damage_reduction * 0.09

        opponent.health -= multiplier * player.weapon.damage

    def attack_output(self, strike_type, strike_dir, opponent):
        # generating random number
        random_num = random.randint(0, 100)

        self.opponent_defence_action(opponent, strike_dir)

        # editing of levels
        if self.opponent_action is "":
            lower_border = -200
            middle_border = -200
            higher_border = 60
            if player.difficulty is "easy":
                higher_border = 45

            # player target effect
            if self.player_attack_direction is "head":
                higher_border += 6

            # player helmet effects
            lower_border += 0.2 * player.helmet.heaviness
            middle_border += 0.2 * player.helmet.heaviness
            higher_border += 0.2 * player.helmet.heaviness

            lower_border += 3.5 * player.helmet.visibility
            middle_border += 3 * player.helmet.visibility
            higher_border += 4 * player.helmet.visibility

            # player armor effects
            lower_border += 0.5 * player.armor.heaviness
            middle_border += 0.4 * player.armor.heaviness
            higher_border += 0.4 * player.armor.heaviness

        elif self.opponent_action is "dodge":
            # setting base levels depending on player weapon
            if player.weapon.weapon_class is "unarmed":
                lower_border = 10
                middle_border = 25
                higher_border = 75
                if player.difficulty is "easy":
                    lower_border = 3
                    middle_border = 20
                    higher_border = 65
            elif player.weapon.weapon_type is "light":
                lower_border = 10
                middle_border = 25
                higher_border = 65
                if player.difficulty is "easy":
                    lower_border = 3
                    middle_border = 20
                    higher_border = 55
            else:  # player weapon type is heavy
                lower_border = 30
                middle_border = 60
                higher_border = 85
                if player.difficulty is "easy":
                    lower_border = 20
                    middle_border = 50
                    higher_border = 80

            # opponent weapon effects
            if opponent.weapon.weapon_class is "unarmed":
                lower_border += 12
                middle_border += 10
                higher_border += 8
            elif opponent.weapon.weapon_type is "light":
                lower_border += 4
                middle_border += 3
                higher_border += 2
            else:  # opponent weapon type is heavy
                lower_border -= 4
                middle_border -= 3
                higher_border -= 1

            # opponent defence direction and player attack direction and type effects
            if self.opponent_direction is "back":
                if strike_dir is "body" or strike_dir is "head":
                    lower_border -= 12
                    middle_border -= 15
                    higher_border -= 13
                else:
                    lower_border += 16
                    middle_border += 21
                    higher_border += 7
            elif self.opponent_direction is "left":
                if strike_dir is "belly":
                    lower_border -= 24
                    middle_border -= 21
                    higher_border -= 9
                elif strike_dir is "body" or strike_dir is "head":
                    lower_border += 16
                    middle_border += 15
                    higher_border += 10
            else:
                if strike_dir is "side":
                    lower_border -= 26
                    middle_border -= 22
                    higher_border -= 10
                elif strike_dir is "body" or strike_dir is "head":
                    lower_border += 14
                    middle_border += 13
                    higher_border += 8

            # player helmet effects
            lower_border += 0.4 * player.helmet.heaviness
            middle_border += 0.3 * player.helmet.heaviness
            higher_border += 0.2 * player.helmet.heaviness

            lower_border += 3 * player.helmet.visibility
            middle_border += 2.5 * player.helmet.visibility
            higher_border += 3 * player.helmet.visibility

            # player armor effects
            lower_border += 0.6 * player.armor.heaviness
            middle_border += 0.5 * player.armor.heaviness
            higher_border += 0.5 * player.armor.heaviness

            # opponent helmet effects
            lower_border -= 0.8 * opponent.helmet.heaviness
            middle_border -= 0.6 * opponent.helmet.heaviness
            higher_border -= 0.5 * opponent.helmet.heaviness

            lower_border -= 1.5 * opponent.helmet.visibility
            middle_border -= 1 * opponent.helmet.visibility
            higher_border -= 1 * opponent.helmet.visibility

            # opponent armor effects
            lower_border -= 1 * opponent.armor.heaviness
            middle_border -= 0.9 * opponent.armor.heaviness
            higher_border -= 0.8 * opponent.armor.heaviness

            # opponent dodge skill effects
            lower_border += opponent.dodge_effectiveness
            middle_border += opponent.dodge_effectiveness
            higher_border += opponent.dodge_effectiveness

        else:  # opponent action is block
            # setting base levels depending on player weapon
            if player.weapon.weapon_class is "unarmed":
                lower_border = 60
                middle_border = 90
                higher_border = 100
                if player.difficulty is "easy":
                    lower_border = 45
                    middle_border = 80
                    higher_border = 90
            elif player.weapon.weapon_type is "light":
                lower_border = 30
                middle_border = 65
                higher_border = 90
                if player.difficulty is "easy":
                    lower_border = 20
                    middle_border = 60
                    higher_border = 85
            else:  # player weapon type is heavy
                lower_border = 15
                middle_border = 35
                higher_border = 65
                if player.difficulty is "easy":
                    lower_border = 10
                    middle_border = 60
                    higher_border = 85

            # opponent weapon effects
            if opponent.weapon.weapon_class is "unarmed":
                lower_border -= 200
                middle_border -= 200
                higher_border -= 60
            elif opponent.weapon.weapon_type is "light":
                lower_border -= 15
                middle_border -= 20
                higher_border -= 15
            else:  # opponent weapon type is heavy
                lower_border += 15
                middle_border += 15
                higher_border += 10

            # player helmet effects
            lower_border += (0.2 * player.helmet.heaviness)
            middle_border += (0.2 * player.helmet.heaviness)
            higher_border += (0.2 * player.helmet.heaviness)

            lower_border += (3.5 * player.helmet.visibility)
            middle_border += (3 * player.helmet.visibility)
            higher_border += (4 * player.helmet.visibility)

            # player armor effects
            lower_border += (0.5 * player.armor.heaviness)
            middle_border += (0.4 * player.armor.heaviness)
            higher_border += (0.4 * player.armor.heaviness)

            # opponent helmet effects
            lower_border -= (0.3 * opponent.helmet.heaviness)
            middle_border -= (0.2 * opponent.helmet.heaviness)
            higher_border -= (0.2 * opponent.helmet.heaviness)

            lower_border -= (3 * opponent.helmet.visibility)
            middle_border -= (2.5 * opponent.helmet.visibility)
            higher_border -= (3 * opponent.helmet.visibility)

            # opponent armor effects
            lower_border -= (0.5 * opponent.armor.heaviness)
            middle_border -= (0.4 * opponent.armor.heaviness)
            higher_border -= (0.4 * opponent.armor.heaviness)

            # opponent action effects
            if self.opponent_direction == "kvinta":
                if strike_dir is "head":
                    lower_border += 24
                    middle_border += 20
                    higher_border += 17
                elif strike_dir is "body":
                    lower_border -= 8
                    middle_border -= 5
                    higher_border -= 3
                elif strike_dir is "belly":
                    lower_border -= 14
                    middle_border -= 12
                    higher_border -= 16
                else:  # player strike direction is side
                    lower_border -= 13
                    middle_border -= 11
                    higher_border -= 14
            elif self.opponent_direction == "kvarta":
                if strike_dir is "head":
                    lower_border -= 15
                    middle_border -= 11
                    higher_border -= 16
                elif strike_dir is "body":
                    lower_border += 3
                    middle_border -= 6
                    higher_border -= 7
                elif strike_dir is "belly":
                    lower_border += 26
                    middle_border += 21
                    higher_border += 18
                else:  # player strike direction is side
                    lower_border -= 14
                    middle_border -= 8.0
                    higher_border -= 15
            elif self.opponent_direction == "terca":
                if strike_dir is "head":
                    lower_border -= 14
                    middle_border -= 20
                    higher_border -= 15
                elif strike_dir is "body":
                    lower_border -= 5
                    middle_border -= 8.0
                    higher_border -= 11
                elif strike_dir is "belly":
                    lower_border -= 12
                    middle_border -= 7
                    higher_border -= 13
                else:  # player strike direction is side
                    lower_border += 31
                    middle_border += 27
                    higher_border += 24
            else:  # opponent block is second
                if strike_dir is "head":
                    lower_border -= 8
                    middle_border -= 15
                    higher_border -= 18
                elif strike_dir is "body":
                    lower_border += 28
                    middle_border += 26
                    higher_border += 25
                elif strike_dir is "belly":
                    lower_border += 17
                    middle_border += 15
                    higher_border += 12
                else:  # player strike direction is side
                    lower_border -= 19
                    middle_border -= 17
                    higher_border -= 16

            # opponent block skill effects
            lower_border += opponent.block_effectiveness
            middle_border += opponent.block_effectiveness
            higher_border += opponent.block_effectiveness

        # rounding part
        lower_border = round(lower_border, 1)
        middle_border = round(middle_border, 1)
        higher_border = round(higher_border, 1)

        # debug part
        if player.test is True:
            print(random_num, lower_border, middle_border, higher_border)
            time.sleep(1)

        # result
        last_action = "attack"

        if random_num <= lower_border:
            self.attack_major_fail(strike_dir, opponent)
            last_action = "defence"
        elif random_num <= middle_border:
            self.attack_minor_fail(strike_dir, opponent)
            last_action = "defence"
        elif random_num <= higher_border:
            self.attack_minor_success(strike_dir, strike_type, opponent)
        else:
            self.attack_major_success(strike_dir, strike_type, opponent)

        return last_action


class Defence:
    pass


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


class Fight:
    preparation = Preparation()
    attack = Attack()
    defence = Defence()
    conclusion = Conclusion()

    def __init__(self, opponent_level):
        self.opponent_level = opponent_level

    def main_(self):
        # preparation
        opponent = self.preparation.opponent_creation(self.opponent_level)
        slow_print("Stojí před vámi {}, {}. A jeho zbraň je {}, {}.\n"
                   "".format(opponent.name, opponent.info, opponent.weapon.name, opponent.weapon.info))
        if opponent.armor.name != "":
            slow_print("Jeho brnění je {}, {}\n".format(opponent.armor.name, opponent.armor.info))
        if opponent.helmet.name != "":
            slow_print("Jeho helma je {}, {}\n".format(opponent.helmet.name, opponent.helmet.info))
        print("")

        last_action = self.preparation.first_fight_action(opponent)

        self.preparation.special_fight_techniques()

        # fight
        while opponent.health > 0:
            if player.health <= 0:
                player_killed()

            if player.helmet.hit_points <= 0 and player.helmet != no_helmet:
                player.helmet = no_helmet
                slow_print("Rozbila se vám helma.\n")
            if player.armor.hit_points <= 0 and player.armor != no_armor:
                player.armor = no_armor
                slow_print("Rozbilo se vám brnění.\n")
            if opponent.helmet.hit_points <= 0 and opponent.helmet != no_helmet:
                opponent.helmet = no_helmet
                slow_print("Vaše rána soupeři rozbila helmu.\n")
            if opponent.armor.hit_points <= 0 and opponent.armor != no_armor:
                opponent.armor = no_armor
                slow_print("Vaše rána soupeři rozbila brnění.\n")

            self.fight_status(opponent)

            # útok na soupeře
            if last_action == "defence":
                last_action = self.attack.strike_direction_choosing(opponent)

            # test part
            last_action = "defence"

            # obrana před soupeřovým útokem
            """
            else:
                last_action = self.random_num_definition(self.guard_choosing)
            """
        self.opponent_action = ""
        self.opponent_last_action_I = ""
        self.opponent_last_action_II = ""
        self.last_attack_zone = ""

        self.conclusion.returning_from_technique()

        return

    def fight_status(self, opponent):
        if opponent.max_health * 0.95 <= opponent.health:
            opponent_health_state = "bez zranění"
        elif opponent.max_health * 0.75 <= opponent.health:
            opponent_health_state = "lehce zraněn"
        elif opponent.max_health * 0.40 <= opponent.health:
            opponent_health_state = "středně zraněn"
        elif opponent.max_health * 0.20 <= opponent.health:
            opponent_health_state = "těžce zraněn"
        else:
            opponent_health_state = "velmi těžce zraněn"
        opponent_stamina_state = "plný energie"
        time.sleep(0.3)
        slow_print("    Váš život: " + str(player.health) + "/" + str(player.max_health))
        slow_print("    Vaše energie: " + str(player.weapon.stamina) + "/" + str(player.weapon.max_stamina) + "\n")
        time.sleep(0.3)
        slow_print("    Soupeř vypadá " + opponent_health_state)
        if player.test is True:
            print("        ", opponent.health, "/", opponent.max_health)
        slow_print("    Soupeř vypadá " + opponent_stamina_state + "\n")
        if player.test is True:
            print("        ", opponent.weapon.stamina, "/", opponent.weapon.max_stamina, "\n")
        time.sleep(0.25)

        return


"""
fight = Fight(2)
fight.main_()
"""