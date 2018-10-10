from character_stats import *
from main_funcs import *


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
                opponent = ork
                opponent.health = random.randint(opponent.lowest_health, opponent.highest_health)
                opponent.max_health = opponent.health
                opponent.weapon = opponent.weapons[random.randint(0, len(opponent.weapons) - 1)]
                opponent.helmet = helmet_2
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
    player_attack_power = ""
    player_last_attack_power_I = ""
    player_last_attack_power_II = ""

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
        while True:
            slow_print("Jakou moc se chcete rozmáchnout, [m]álo, [s]tředně, nebo [h]odně?\n")
            power_selection = base_options()
            if power_selection == "m":
                strike_power = "small"
                break
            elif power_selection == "s":
                strike_power = "medium"
                break
            elif power_selection == "h":
                strike_power = "high"
                break
            elif power_selection != "skip":
                wrong_input(0)

        return self.attack_output(strike_type, strike_dir, strike_power, opponent)

    def opponent_defence_action(self, opponent, strike_dir, strike_power):
        # opponent action choosing
        if opponent.defence == []:
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

            if self.player_last_attack_power_II == "low":
                split -= 1
            elif self.player_last_attack_power_II == "high":
                split += 1
            if self.player_last_attack_power_I == "low":
                split -= 2
            elif self.player_last_attack_power_I == "high":
                split += 2
            if self.player_attack_power == "low":
                split -= 3
            elif self.player_attack_power == "high":
                split += 3

            self.player_last_attack_power_II = self.player_last_attack_power_I
            self.player_last_attack_power_I = self.player_attack_power
            self.player_attack_power = strike_power

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
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.armor.smash_damage_reduction * 0.05
                else:
                    multiplier -= player.armor.smash_damage_reduction * 0.025
            elif "cut" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.armor.cut_damage_reduction * 0.09
                else:
                    multiplier -= player.armor.cut_damage_reduction * 0.045
            elif "stab" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.armor.stab_damage_reduction * 0.09
                else:
                    multiplier -= player.armor.stab_damage_reduction * 0.045
        else:
            slow_print("Váš nepovedený útok vás nechal úplně otevřeného soupeřovým útokům, na to byl váš soupeř"
                       " připraven a tak vám ihned zasadil ránu do hlavy.\n")
            multiplier += 0.2
            if "smash" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.helmet.smash_damage_reduction * 0.05
                else:
                    multiplier -= player.helmet.smash_damage_reduction * 0.025
            elif "cut" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.helmet.cut_damage_reduction * 0.09
                else:
                    multiplier -= player.helmet.cut_damage_reduction * 0.045
            elif "stab" in opponent.weapon.damage_type:
                if "armor_piercing" not in opponent.weapon.special_abilities:
                    multiplier -= player.helmet.stab_damage_reduction * 0.09
                else:
                    multiplier -= player.helmet.stab_damage_reduction * 0.045

        if "cut" in opponent.weapon.damage or "stab" in opponent.weapon.damage and "no_bleeding":
            if "bleeding_1" in player.special_abilities:
                player.special_abilities.remove("bleeding_1")
                player.special_abilities.append("bleeding_3")
                slow_print("Velmi těžce krvácíte.\n")
            elif "bleeding_2" in player.special_abilities:
                player.special_abilities.remove("bleeding_2")
                player.special_abilities.append("bleeding_3")
                slow_print("Velmi těžce krvácíte.\n")
            elif "bleeding_3" in player.special_abilities:
                slow_print("Velmi těžce krvácíte.\n")
            else:
                player.special_abilities.append("bleeding_2")
                slow_print("Začali jste těžce krvácíte.\n")


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
                block_output = "Ale na poslední chvíli stihl zdvihnout zbraň a částečně vám úder vykrýt a tu sílu" \
                               " kterou nevykryl zbraní absorbovala jeho helma."
                opponent.weapon.hit_points -= player.weapon.damage
                opponent.helmet.hit_points -= 1.5 * player.weapon.damage
                if "armor_piercing" in player.weapon.special_abilities:
                    opponent.helmet -= player.weapon.damage
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

    def attack_minor_success(self, strike_dir, strike_type, strike_power, opponent):
        multiplier = 0.5

        if self.opponent_action == "":
            slow_print("Soupeř se vám nijak nebránil, jenže vám se nepodařilo ho dobře trefit a tak jste ho"
                       " nezasáhli plnou silou.")
            multiplier += 0.25
        elif self.opponent_action == "block":
            block_message = ""
            if random.randint(0, 5) == 0:
                block_output = "Ale vy jste úplně neodhadli vzdálenost a tak jste soupeře jen lehce zasáhli"
            elif random.randint(0, 4) != 0:
                block_output = "Ale než ho vaše zbraň zasáhla stihl zareagovat a částečně váš úder zablokoval, takže" \
                               " jste ho jen lehce zranili."
                opponent.weapon.hit_points -= 1.5 * player.weapon.damage
            else:
                block_output = "Ale vaše zbraň vám trochu sklouzla v prstech a tím se váš útok trochu opozdil, což" \
                               " dalo soupeři čas na to vaši ránu ještě částečně vykrýt a tak jste mu způsobili jen" \
                               " malé zranění"

            if self.opponent_direction == "terca":
                block_message = "bok"
                if strike_dir == "side":
                    block_output = "Jeho kryt byl ovšem dost pomalý, takže ho váš úder částečně prorazil a zasáhl " \
                                   "soupeře, takže mu způsobil lehké zranění"
                    opponent.weapon.hit_points -= player.weapon.damage
            elif self.opponent_direction == "kvinta":
                block_message = "hlavu"
                if strike_dir == "head":
                    block_output = "Jeho kryt ovšem nebyl dost rychlý, takže ho váš úder částečně prorazil a zasáhl " \
                                   "soupeře, takže mu způsobil lehké zranění"
                    opponent.weapon.hit_points -= player.weapon.damage
            elif self.opponent_direction == "kvarta":
                block_message = "břicho"
                if strike_dir == "belly":
                    block_output = "Jeho kryt ovšem nebyl dost rychlý, a tak váš úder zablokoval jen částečně, takže" \
                                   " mu způsobil lehké zranění"
                    opponent.weapon.hit_points -= player.weapon.damage
            elif self.opponent_direction == "second":
                block_message = "proti bodání"
                if random.randint(0, 1) == 0 and self.opponent_direction != "side":
                    block_output = "Ale vatáčel ji příliš rychle takže vaši zbraň jen částečně odklonil a tak ho váš" \
                                   " útok lehce zranil"
                else:
                    block_output = "Ale vytáčel svou zbraň dost pomalu a tak nestihl úplně odklonit váš rychlý útok," \
                                   " který ho lehce zranil"
                opponent.weapon.hit_points -= 0.5 * player.weapon.damage

            slow_print("Váš soupeř se snažil krýt {}. {}.\n".format(block_message, block_output))
        else:
            if self.opponent_direction == "left":
                dodge_message = "doleva"
                if strike_dir == "belly":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš rychlý a tak ještě než soupeř uhnul máchli jste tam" \
                                       " kam jste předpokládali, že se dostane a se štěstím jste ho lehce zasáhli"
                    else:
                        dodge_output = "Ale váš útok trval dost dlouho takže se oponentovi téměř podařilo se mu" \
                                       " vyhnout, jen se štěstím jste ho lehce zasáhli"
                else:
                    dodge_output = "Vy jste si toho na poslední chvíli všimli a tak se vám ho povedlo alespoň lehce" \
                                   " zasáhnout"
            elif self.opponent_direction == "back":
                dodge_message = "dozadu"
                if strike_dir == "head" or strike_dir == "body":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok nebyl úplně tak dlouhý jak jste potřebovali a tak jste soupeře" \
                                       " zasáhli jen lehce"
                    else:
                        dodge_output = "Ale vy jste na soupeře zaútočili ve chvíli kdy začal uhýbat a už se vám" \
                                       " povedlo protáhnout útok jen trochu takže jste ho nezasáhli plnou silou"
                else:
                    dodge_output = "Vy jste si toho na poslední chvíli všimli a tak se vám ho povedlo alespoň lehce" \
                                   " zasáhnout"
            else:
                dodge_message = "doprava"
                if strike_dir == "side":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale váš útok byl příliš rychlý a tak ještě než soupeř uhnul máchli jste tam" \
                                       " kam jste předpokládali že se dostane a se štěstím jste ho lehce zasáhli"
                    else:
                        dodge_output = "Ale váš útok trval dost dlouho takže se oponentovi téměř podařilo se mu" \
                                       " vyhnout, jen se štěstím jste ho lehce zasáhli"
                else:
                    dodge_output = "Vy jste si toho na poslední chvíli všimli a tak se vám ho povedlo alespoň lehce" \
                                   " zasáhnout"

            slow_print("Soupeř se snažil uhnout {}. {}.".format(dodge_message, dodge_output))

        if strike_dir == "head":
            if opponent.helmet != no_helmet:
                opponent.helmet.hit_points -= 1.5 * player.weapon.damage
            if strike_type == "cut":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.cut_damage_reduction * 0.05
                else:
                    multiplier -= opponent.helmet.cut_damage_reduction * 0.025
            elif strike_type == "smash":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.smash_damage_reduction * 0.02
                else:
                    multiplier -= opponent.helmet.smash_damage_reduction * 0.01
            elif strike_type == "stab":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.stab_damage_reduction * 0.05
                else:
                    multiplier -= opponent.helmet.stab_damage_reduction * 0.025
        else:
            if opponent.armor != no_armor:
                opponent.armor.hit_points -= 1.5 * player.weapon.damage
            if strike_type == "cut":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.cut_damage_reduction * 0.05
                else:
                    multiplier -= opponent.armor.cut_damage_reduction * 0.025
            elif strike_type == "smash":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.smash_damage_reduction * 0.02
                else:
                    multiplier -= opponent.armor.smash_damage_reduction * 0.01
            elif strike_type == "stab":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.stab_damage_reduction * 0.05
                else:
                    multiplier -= opponent.armor.stab_damage_reduction * 0.025

        if strike_power == "low":
            multiplier -= 0.25
        elif strike_power == "high":
            multiplier += 0.25

        if "no_bleeding" not in opponent.special_abilities:
            if "bleeding_1" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_1")
                opponent.special_abilities.append("bleeding_2")
                slow_print("Váš soupeř těžce krvácí.\n")
            elif "bleeding_2" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_2")
                opponent.special_abilities.append("bleeding_3")
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            elif "bleeding_3" in opponent.special_abilities:
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            else:
                opponent.special_abilities.append("bleeding_1")
                slow_print("Váš soupeř začal lehce krvácet.\n")

        opponent.health -= multiplier * player.weapon.damage

    def attack_major_success(self, strike_dir, strike_type, strike_power, opponent):
        multiplier = 1

        if self.opponent_action == "":
            slow_print("Váš soupeř se vám nebránil a váš úder ho tvrdě zasáhl, takže jste ho velmi poranili.")
            multiplier += 0.5
        elif self.opponent_action == "block":
            block_message = ""
            if random.randint(0, 4) == 0:
                block_output = "Ale všiml si že sekáte jinam tak se ještě snažil svou zbraň nastavit tak aby váš úder" \
                               " vykryl ale už to nestihl a vy jste mu uštedřili silný úder"
            elif random.randint(0, 3) != 0:
                block_output = "Takže váš úder čistě prošel a tak zasáhl soupeře plnou silou"
            else:
                block_output = "Což vám dovolilo zasadit soupeři těžký zásah"

            if self.opponent_direction == "terca":
                block_message = "bok"
                if strike_dir == "side":
                    block_output = "Jeho kryt byl ovšem dost slabý a váš úder naopak velmi silný takže jste ho tvrdě" \
                                   " zasáhli"
                    opponent.weapon.hit_points -= 0.5 * player.weapon.damage
            elif self.opponent_direction == "kvinta":
                block_message = "hlavu"
                if strike_dir == "head":
                    block_output = "Ale pozdě vytočil svou zbraň a tak váše zbraň čistě prošla a zasáhla ho plnou silou"
                    opponent.weapon.hit_points -= 0.5 * player.weapon.damage
            elif self.opponent_direction == "kvarta":
                block_message = "břicho"
                if strike_dir == "belly":
                    block_output = "Jeho kryt byl ovšem dost slabý a váš úder naopak velmi silný takže jste ho tvrdě" \
                                   " zasáhli"
                    opponent.weapon.hit_points -= 0.5 * player.weapon.damage
            elif self.opponent_direction == "second":
                block_message = "proti bodání"
                if random.randint(0, 1) == 0 and self.opponent_direction != "side":
                    block_output = "Ale vatáčel ji hrozně rychle, takže vaši zbraň úplně minul a váš úder mohl" \
                                   " zasáhnout plnou silou"
                else:
                    block_output = "Ale vytáčel svou zbraň příliš pomalu, tím pádem jeho zbraň vaši ani neškrtla, než" \
                                   " se vám povedlo dokončit svůj bleskový úder"

            slow_print("Váš soupeř se snažil krýt {}. {}.\n".format(block_message, block_output))
        else:
            if self.opponent_direction == "left":
                dodge_message = "doleva"
                if strike_dir != "belly":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vášemu soupeři trvalo příliš dlouho než se rozhýbat a tak jste ho zasáhli"
                    else:
                        dodge_output = "Jenže váš soupež si špatně načasoval svůj pohyb a tak uhnul moc brzo čímž vám" \
                                       " dal ideální prostor pro výpad kterým jste mu uštědřili tvrdou ránu"
                else:
                    dodge_output = "Soupeř vám uskočil přímo do rány a tak jste ho zasáhli plnou silou"
            elif self.opponent_direction == "back":
                dodge_message = "dozadu"
                if strike_dir != "head" or strike_dir == "body":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vášemu soupeři trvalo příliš dlouho než se rozhýbat a tak jste ho zasáhli"
                    else:
                        dodge_output = "Jenže váš soupež si špatně načasoval svůj pohyb a tak uhnul moc brzo čímž vám" \
                                       " dal ideální prostor pro výpad kterým jste mu uštědřili tvrdou ránu"
                else:
                    dodge_output = "Soupeř vám uskočil přímo do rány a tak jste ho zasáhli plnou silou"
            else:
                dodge_message = "doprava"
                if strike_dir != "side":
                    if random.randint(0, 1) == 0:
                        dodge_output = "Ale vášemu soupeři trvalo příliš dlouho než se rozhýbat a tak jste ho zasáhli"
                    else:
                        dodge_output = "Jenže váš soupež si špatně načasoval svůj pohyb a tak uhnul moc brzo čímž vám" \
                                       " dal ideální prostor pro výpad kterým jste mu uštědřili tvrdou ránu"
                else:
                    dodge_output = "Soupeř vám uskočil přímo do rány a tak jste ho zasáhli plnou silou"

            slow_print("Soupeř se snažil uhnout {}. {}.".format(dodge_message, dodge_output))

        if strike_dir == "head":
            if opponent.helmet != no_helmet:
                opponent.helmet.hit_points -= 2.5 * player.weapon.damage
            if strike_type == "cut":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.cut_damage_reduction * 0.09
                else:
                    multiplier -= opponent.helmet.cut_damage_reduction * 0.045
            elif strike_type == "smash":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.smash_damage_reduction * 0.04
                else:
                    multiplier -= opponent.helmet.smash_damage_reduction * 0.02
            elif strike_type == "stab":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.helmet.stab_damage_reduction * 0.09
                else:
                    multiplier -= opponent.helmet.stab_damage_reduction * 0.045
        else:
            if opponent.armor != no_armor:
                opponent.armor.hit_points -= 2.5 * player.weapon.damage
            if strike_type == "cut":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.cut_damage_reduction * 0.09
                else:
                    multiplier -= opponent.armor.cut_damage_reduction * 0.045
            elif strike_type == "smash":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.smash_damage_reduction * 0.04
                else:
                    multiplier -= opponent.armor.smash_damage_reduction * 0.02
            elif strike_type == "stab":
                if "armor_piercing" not in player.weapon.special_abilities:
                    multiplier -= opponent.armor.stab_damage_reduction * 0.09
                else:
                    multiplier -= opponent.armor.stab_damage_reduction * 0.045

        if strike_power == "low":
            multiplier -= 0.5
        elif strike_power == "high":
            multiplier += 0.5

        if "no_bleeding" not in opponent.special_abilities:
            if "bleeding_1" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_1")
                opponent.special_abilities.append("bleeding_3")
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            elif "bleeding_2" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_2")
                opponent.special_abilities.append("bleeding_3")
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            elif "bleeding_3" in opponent.special_abilities:
                slow_print("Váš soupeř velmi těžce krvácí.\n")
            else:
                player.special_abilities.append("bleeding_2")
                slow_print("Váš soupeř začal těžce krvácet.\n")

        opponent.health -= multiplier * player.weapon.damage

    def attack_output(self, strike_type, strike_dir, strike_power, opponent):
        # generating random number
        random_num = random.randint(0, 100)

        self.opponent_defence_action(opponent, strike_dir, strike_power)

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

            # player attack power effects
            if strike_power == "small":
                higher_border -= 10
            elif strike_power == "high":
                higher_border += 15

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
                middle_border = 30
                higher_border = 60
                if player.difficulty is "easy":
                    lower_border = 5
                    middle_border = 25
                    higher_border = 50
            elif player.weapon.weapon_type is "medium":
                lower_border = 15
                middle_border = 35
                higher_border = 65
                if player.difficulty is "easy":
                    lower_border = 10
                    middle_border = 25
                    higher_border = 55
            else:
                lower_border = 20
                middle_border = 55
                higher_border = 70
                if player.difficulty is "easy":
                    lower_border = 25
                    middle_border = 45
                    higher_border = 60

            # opponent weapon effects
            if opponent.weapon.weapon_class is "unarmed":
                lower_border += 12
                middle_border += 10
                higher_border += 8
            elif opponent.weapon.weapon_type is "light":
                lower_border += 4
                middle_border += 3
                higher_border += 2
            elif opponent.weapon.weapon_type is "medium":
                lower_border -= 2
                middle_border -= 1
                higher_border -= 0.5
            elif opponent.weapon.weapon_type is "heavy":
                lower_border -= 4
                middle_border -= 3
                higher_border -= 1

            # opponent defence direction and player attack direction and type effects
            if self.opponent_direction is "back":
                if strike_dir is "body" or strike_dir is "head":
                    lower_border -= 18
                    middle_border -= 15
                    higher_border -= 13
                else:
                    lower_border += 9
                    middle_border += 21
                    higher_border += 17
            elif self.opponent_direction is "left":
                if strike_dir is "belly":
                    lower_border -= 24
                    middle_border -= 21
                    higher_border -= 11
                elif strike_dir is "body" or strike_dir is "head":
                    lower_border += 7
                    middle_border += 14
                    higher_border += 16
            else:
                if strike_dir is "side":
                    lower_border -= 26
                    middle_border -= 22
                    higher_border -= 13
                elif strike_dir is "body" or strike_dir is "head":
                    lower_border += 6
                    middle_border += 13
                    higher_border += 15

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

            # player attack power effects
            if strike_power == "small":
                lower_border -= 6
                middle_border -= 14
                higher_border -= 7
            elif strike_power == "medium":
                lower_border += 1
                middle_border += 7
                higher_border += 2
            elif strike_power == "high":
                lower_border += 4
                middle_border += 16
                higher_border += 9

            # player character effects
            if player.char == "elf":
                if "elf_debuff" in player.weapon.special_abilities:
                    lower_border += 2
                    middle_border += 3
                    higher_border += 3
                if "elf_buff" in player.weapon.special_abilities:
                    lower_border -= 2
                    middle_border -= 3
                    higher_border -= 3

                if "elf_debuff" in player.helmet.special_abilities:
                    lower_border += 3
                    middle_border += 4
                    higher_border += 4
                if "elf_buff" in player.helmet.special_abilities:
                    lower_border -= 3
                    middle_border -= 4
                    higher_border -= 4

                if "elf_debuff" in player.armor.special_abilities:
                    lower_border += 4
                    middle_border += 5
                    higher_border += 5
                if "elf_buff" in player.armor.special_abilities:
                    lower_border -= 4
                    middle_border -= 5
                    higher_border -= 5
            elif player.char == "dwarf":
                if "dwarf_debuff" in player.weapon.special_abilities:
                    lower_border += 2
                    middle_border += 3
                    higher_border += 3
                if "dwarf_buff" in player.weapon.special_abilities:
                    lower_border -= 2
                    middle_border -= 3
                    higher_border -= 3

                if "dwarf_debuff" in player.helmet.special_abilities:
                    lower_border += 3
                    middle_border += 4
                    higher_border += 4
                if "dwarf_buff" in player.helmet.special_abilities:
                    lower_border -= 3
                    middle_border -= 4
                    higher_border -= 4

                if "dwarf_debuff" in player.armor.special_abilities:
                    lower_border += 4
                    middle_border += 5
                    higher_border += 5
                if "dwarf_buff" in player.armor.special_abilities:
                    lower_border -= 4
                    middle_border -= 5
                    higher_border -= 5
            elif player.char == "human":
                if "human_debuff" in player.weapon.special_abilities:
                    lower_border += 2
                    middle_border += 3
                    higher_border += 3
                if "human_buff" in player.weapon.special_abilities:
                    lower_border -= 2
                    middle_border -= 3
                    higher_border -= 3

                if "human_debuff" in player.helmet.special_abilities:
                    lower_border += 3
                    middle_border += 4
                    higher_border += 4
                if "human_buff" in player.helmet.special_abilities:
                    lower_border -= 3
                    middle_border -= 4
                    higher_border -= 4

                if "human_debuff" in player.armor.special_abilities:
                    lower_border += 4
                    middle_border += 5
                    higher_border += 5
                if "human_buff" in player.armor.special_abilities:
                    lower_border -= 4
                    middle_border -= 5
                    higher_border -= 5

            # equipment special buffs and debuffs
            if "extra_dodge" in  player.weapon.special_abilities:
                lower_border -= 3
                middle_border -= 5
                higher_border -= 5
            if "weak_dodge" in player.weapon.special_abilities:
                lower_border += 3
                middle_border += 5
                higher_border += 5

            if "extra_dodge" in  player.helmet.special_abilities:
                lower_border -= 3
                middle_border -= 5
                higher_border -= 5
            if "weak_dodge" in player.weapon.special_abilities:
                lower_border += 3
                middle_border += 5
                higher_border += 5

            if "extra_dodge" in  player.armor.special_abilities:
                lower_border -= 4
                middle_border -= 6
                higher_border -= 6
            if "weak_dodge" in player.weapon.special_abilities:
                lower_border += 4
                middle_border += 6
                higher_border += 6

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
                lower_border = 25
                middle_border = 60
                higher_border = 95
                if player.difficulty is "easy":
                    lower_border = 20
                    middle_border = 55
                    higher_border = 85
            elif player.weapon.weapon_type is "medium":
                lower_border = 15
                middle_border = 50
                higher_border = 80
                if player.difficulty is "easy":
                    lower_border = 10
                    middle_border = 40
                    higher_border = 70
            else:  # player weapon type is heavy
                lower_border = 10
                middle_border = 40
                higher_border = 70
                if player.difficulty is "easy":
                    lower_border = 5
                    middle_border = 35
                    higher_border = 60

            # opponent weapon effects
            if opponent.weapon.weapon_class is "unarmed":
                lower_border -= 200
                middle_border -= 200
                higher_border -= 60
            elif opponent.weapon.weapon_type is "light":
                lower_border -= 10
                middle_border -= 13
                higher_border -= 8
            elif opponent.weapon.weapon_type is "medium":
                lower_border += 3
                middle_border += 3
                higher_border += 2
            else:  # opponent weapon type is heavy
                lower_border += 5
                middle_border += 12
                higher_border += 14

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
                    lower_border += 8
                    middle_border += 26
                    higher_border += 30
                elif strike_dir is "body":
                    lower_border -= 12
                    middle_border -= 16
                    higher_border -= 8
                elif strike_dir is "belly":
                    lower_border -= 18
                    middle_border -= 22
                    higher_border -= 16
                else:  # player strike direction is side
                    lower_border -= 20
                    middle_border -= 20
                    higher_border -= 14
            elif self.opponent_direction == "kvarta":
                if strike_dir is "head":
                    lower_border -= 20
                    middle_border -= 20
                    higher_border -= 16
                elif strike_dir is "body":
                    lower_border -= 8
                    middle_border -= 3
                    higher_border -= 4
                elif strike_dir is "belly":
                    lower_border += 9
                    middle_border += 29
                    higher_border += 34
                else:  # player strike direction is side
                    lower_border -= 17
                    middle_border -= 17
                    higher_border -= 13
            elif self.opponent_direction == "terca":
                if strike_dir is "head":
                    lower_border -= 17
                    middle_border -= 20
                    higher_border -= 16
                elif strike_dir is "body":
                    lower_border -= 13
                    middle_border -= 11
                    higher_border -= 8
                elif strike_dir is "belly":
                    lower_border -= 12
                    middle_border -= 7
                    higher_border -= 13
                else:  # player strike direction is side
                    lower_border += 11
                    middle_border += 33
                    higher_border += 37
            else:  # opponent block is second
                if strike_dir is "head":
                    lower_border -= 19
                    middle_border -= 17
                    higher_border -= 12
                elif strike_dir is "body":
                    lower_border += 8
                    middle_border += 29
                    higher_border += 33
                elif strike_dir is "belly":
                    lower_border -= 6
                    middle_border += 4
                    higher_border -= 2
                else:  # player strike direction is side
                    lower_border -= 17
                    middle_border -= 14
                    higher_border -= 11

            # opponent block skill effects
            lower_border += opponent.block_effectiveness
            middle_border += opponent.block_effectiveness
            higher_border += opponent.block_effectiveness

            # player attack power effects
            if strike_power == "small":
                lower_border += 3
                middle_border += 12
                higher_border += 9
            elif strike_power == "medium":
                lower_border -= 2
                middle_border -= 4
                higher_border -= 1
            elif strike_power == "high":
                lower_border -= 3
                middle_border -= 13
                higher_border -= 8

            # player character effects
            if player.char == "elf":
                if "elf_debuff" in player.weapon.special_abilities:
                    lower_border += 4
                    middle_border += 5
                    higher_border += 5
                if "elf_buff" in player.weapon.special_abilities:
                    lower_border -= 4
                    middle_border -= 5
                    higher_border -= 5
                if "elf_debuff" in player.helmet.special_abilities:
                    lower_border += 1
                    middle_border += 2
                    higher_border += 2
                if "elf_buff" in player.helmet.special_abilities:
                    lower_border -= 1
                    middle_border -= 2
                    higher_border -= 2
                if "elf_debuff" in player.armor.special_abilities:
                    lower_border += 2
                    middle_border += 3
                    higher_border += 3
                if "elf_buff" in player.armor.special_abilities:
                    lower_border -= 2
                    middle_border -= 3
                    higher_border -= 3
            elif player.char == "dwarf":
                if "dwarf_debuff" in player.weapon.special_abilities:
                    lower_border += 4
                    middle_border += 5
                    higher_border += 5
                if "dwarf_buff" in player.weapon.special_abilities:
                    lower_border -= 4
                    middle_border -= 5
                    higher_border -= 5
                if "dwarf_debuff" in player.helmet.special_abilities:
                    lower_border += 1
                    middle_border += 2
                    higher_border += 2
                if "dwarf_buff" in player.helmet.special_abilities:
                    lower_border -= 1
                    middle_border -= 2
                    higher_border -= 2
                if "dwarf_debuff" in player.armor.special_abilities:
                    lower_border += 2
                    middle_border += 3
                    higher_border += 3
                if "dwarf_buff" in player.armor.special_abilities:
                    lower_border -= 2
                    middle_border -= 3
                    higher_border -= 3
            elif player.char == "human":
                if "human_debuff" in player.weapon.special_abilities:
                    lower_border += 4
                    middle_border += 5
                    higher_border += 5
                if "human_buff" in player.weapon.special_abilities:
                    lower_border -= 4
                    middle_border -= 5
                    higher_border -= 5
                if "human_debuff" in player.helmet.special_abilities:
                    lower_border += 1
                    middle_border += 2
                    higher_border += 2
                if "human_buff" in player.helmet.special_abilities:
                    lower_border -= 1
                    middle_border -= 2
                    higher_border -= 2
                if "human_debuff" in player.armor.special_abilities:
                    lower_border += 2
                    middle_border += 3
                    higher_border += 3
                if "human_buff" in player.armor.special_abilities:
                    lower_border -= 2
                    middle_border -= 3
                    higher_border -= 3

            # equipment special buffs and debuffs
            if "extra_block" in  player.weapon.special_abilities:
                lower_border -= 3
                middle_border -= 5
                higher_border -= 5
            if "weak_block" in player.weapon.special_abilities:
                lower_border += 3
                middle_border += 5
                higher_border += 5

            if "extra_block" in  player.helmet.special_abilities:
                lower_border -= 3
                middle_border -= 5
                higher_border -= 5
            if "weak_block" in player.weapon.special_abilities:
                lower_border += 3
                middle_border += 5
                higher_border += 5

            if "extra_block" in  player.armor.special_abilities:
                lower_border -= 4
                middle_border -= 6
                higher_border -= 6
            if "weak_block" in player.weapon.special_abilities:
                lower_border += 4
                middle_border += 6
                higher_border += 6


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
        elif random_num <= higher_border:
            self.attack_minor_success(strike_dir, strike_type, strike_power, opponent)
        else:
            self.attack_major_success(strike_dir, strike_type, strike_power, opponent)

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

            self.fight_status(opponent)

            # útok na soupeře
            if last_action == "defence":
                if player.test is True:
                    print("Opponent weapon, helmet, armor info:", opponent.weapon.hit_points, opponent.helmet.hit_points,
                        opponent.armor.hit_points, "\n")
                last_action = self.attack.strike_direction_choosing(opponent)

            # test part
            last_action = "defence"

            # obrana před soupeřovým útokem
            """
            else:
                last_action = self.random_num_definition(self.guard_choosing)
            """

            self.special_effects(opponent)

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

    def special_effects(self, opponent):
        # player gear destruction
        if player.weapon.hit_points <= 0 and player.weapon.weapon_class != "unarmed":
            player.weapon = fists
            slow_print("Rozbila se vám zbraň.\n")
        if player.helmet.hit_points <= 0 and player.helmet != no_helmet:
            player.helmet = no_helmet
            slow_print("Rozbila se vám helma.\n")
        if player.armor.hit_points <= 0 and player.armor != no_armor:
            player.armor = no_armor
            slow_print("Rozbilo se vám brnění.\n")

        # opponent gear destruction
        if opponent.weapon.hit_points <= 0 and opponent.weapon.weapon_class != "unarmed":
            opponent.weapon = opponent.unarmed_weapon
            slow_print("Soupeřova zbraň nevydržela úder té vaší a roztříštila se na kusy.\n")
        if opponent.helmet.hit_points <= 0 and opponent.helmet != no_helmet:
            opponent.helmet = no_helmet
            slow_print("Vaše rána soupeři rozbila helmu.\n")
        if opponent.armor.hit_points <= 0 and opponent.armor != no_armor:
            opponent.armor = no_armor
            slow_print("Vaše rána soupeři rozbila brnění.\n")

        # rusty effect on opponent
        if "rusty" in opponent.helmet.special_abilities:
            if random.randint(0, 4) == 3:
                opponent.health -= 10
                "Váš soupeř se ošklivě pořezal o svoji helmu.\n"
        if "rusty" in opponent.armor.special_abilities:
            if random.randint(0, 3) == 3:
                opponent.health -= 10
                "Váš soupeř se ošklivě pořezal o svoje brnění.\n"

        # rusty effect on player
        if "rusty" in player.helmet.special_abilities:
            if random.randint(0, 4) == 3:
                player.health -= 10
                "Ošklivě jste se pořezali o svoji helmu.\n"
        if "rusty" in player.armor.special_abilities:
            if random.randint(0, 3) == 3:
                player.health -= 10
                "Ošklivě jste se pořezali o svoje brnění.\n"

        # bleeding effects
        if "no_bleeding" not in player.special_abilities:
            if "bleeding_1" in player.special_abilities:
                player.special_abilities.remove("bleeding_1")
                if "bleeding_resistance" in player.special_abilities:
                    player.health -= 5
                else:
                    player.health -= 15
            elif "bleeding_2" in player.special_abilities:
                player.special_abilities.remove("bleeding_2")
                player.special_abilities.append("bleeding_1")
                if "bleeding_resistance" in player.special_abilities:
                    player.health -= 10
                else:
                    player.health -= 25
            elif "bleeding_3" in player.special_abilities:
                player.special_abilities.remove("bleeding_3")
                player.special_abilities.append("bleeding_2")
                if "bleeding_resistance" in player.special_abilities:
                    player.health -= 20
                else:
                    player.health -= 40

        if "no_bleeding" not in opponent.special_abilities:
            if "bleeding_1" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_1")
                if "bleeding_resistance" in opponent.special_abilities:
                    opponent.health -= 5
                else:
                    opponent.health -= 15
            elif "bleeding_2" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_2")
                opponent.special_abilities.append("bleeding_1")
                if "bleeding_resistance" in opponent.special_abilities:
                    opponent.health -= 10
                else:
                    opponent.health -= 25
            elif "bleeding_3" in opponent.special_abilities:
                opponent.special_abilities.remove("bleeding_3")
                opponent.special_abilities.append("bleeding_2")
                if "bleeding_resistance" in opponent.special_abilities:
                    opponent.health -= 20
                else:
                    opponent.health -= 40

        return


"""
fight = Fight(2)
fight.main_()
"""