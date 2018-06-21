from Reknamorcen.character_stats import *
from Reknamorcen.main_funcs import *


class Fight:
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

    def __init__(self, opponent_level):
        self.opponent_level = opponent_level

    def fight(self):
        opponent = self.opponent_creation()
        slow_print("Stojí před vámi {}, {}. A jeho zbraň je {}, {}.\n".format(opponent.name, opponent.info,
                                                                              opponent.weapon.name,
                                                                              opponent.weapon.info))

        last_action = self.first_fight_action(opponent)

        self.special_fight_techniques()

        while opponent.health > 0:
            if player.health <= 0:
                player_killed()
            self.fight_status(opponent)

            # útok na soupeře
            if last_action == "defence":
                last_action = self.strike_direction_choosing(opponent)

            # test part
            last_action = "defence"

            # obrana před soupeřovým útokem
            """
            else:
                last_action = self.random_num_definition(self.guard_choosing)
            """

        # ukončovací hláška
        self.opponent_action = ""
        self.opponent_last_action_I = ""
        self.opponent_last_action_II = ""
        self.last_attack_zone = ""
        end_call = random.randint(0, 1)
        if end_call == 0:
            slow_print("Zabili jste ho.\n")
        elif end_call == 1:
            slow_print("Tohle už nepřežil.\n")

    # preparation
    def opponent_creation(self):
        opponent_difficulty = self.opponent_level
        if opponent_difficulty == 0:
            num = 2
            if player.difficulty == "hard":
                num = 3
            opponent_difficulty = random.randint(1, num)

        if opponent_difficulty == 1:
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

        elif self.opponent_level == 2:
            opponent_number = random.randint(0, 0)
            if opponent_number == 0:
                ork.health = random.randint(ork.lowest_health, ork.highest_health)
                ork.max_health = ork.health
                ork.weapon = two_handed_axe
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

        elif opponent_difficulty == 3:
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
        if "helmet" in player.gear:
            loudness += 3
        if "armor" in player.gear:
            loudness += 5
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

    def fight_bonuses(self):
        # short sword
        ss_first_lvl = 0
        ss_second_lvl = 0
        ss_human_boost = 0
        ss_elf_boost = 0
        if short_sword.xp >= 50 and ss_first_lvl < 1:
            short_sword.stamina += 1
            short_sword.damage += 0.5
            ss_first_lvl += 1
        if short_sword.xp >= 150 and ss_second_lvl < 1:
            short_sword.stamina_regain += 0.5
            ss_second_lvl += 1
        if player.char is "human" and ss_human_boost < 1:
            short_sword.damage += 0.5
            short_sword.stamina += 1
            ss_human_boost += 1
        if player.char is "elf" and ss_elf_boost < 1:
            short_sword.stamina += 1
            short_sword.stamina_regain += 0.5
            ss_elf_boost += 1

        # two handed axe

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

    # attack
    def strike_direction_choosing(self, opponent):
        strike_type = "stab"
        strike_dir = "body"
        if "cut" and "stab" in player.weapon.damage_type:
            slow_print("Chcete [b]odat, nebo [s]ekat?")
            while True:
                attack_type = base_options()
                if attack_type == "b":
                    slow_print("Chcete bodat do [t]ěla, nebo na [h]lavu?")
                    while True:
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
                    strike_type = "chop"
                    slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
                    while True:
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
            slow_print("Chcete bodat do [t]ěla, nebo na [h]lavu?")
            while True:
                attack_direction = base_options()
                if attack_direction == "t":
                    break
                elif attack_direction == "h":
                    strike_dir = "head"
                    break
                elif attack_direction != "skip":
                    wrong_input(0)
        elif "cut" in player.weapon.damage_type:
            strike_type = "chop"
            slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
            while True:
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
            slow_print("Chcete ho praštit do [h]lavy, nebo do [b]řicha?")
            while True:
                attack_direction = base_options()
                if attack_direction == "b":
                    break
                elif attack_direction == "h":
                    strike_dir = "head"
                    break
                elif attack_direction is "skip":
                    pass
                else:
                    wrong_input(0)
        elif "smash" in player.weapon.damage_type:
            strike_type = "smash"
            slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
            while True:
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
                elif attack_direction is "skip":
                    pass
                else:
                    wrong_input(0)

        return self.attack_output(strike_type, strike_dir, opponent)

    def opponent_defence_action(self, opponent, strike_type, strike_dir):
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

            if "stab" in opponent.weapon.damage_type:
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

            if self.player_last_attack_direction_I is "body" or self.player_last_attack_direction_I is "head":
                lower_split -= 4
                higher_split -= 8
                special_split -= 12
            elif self.player_last_attack_direction_I is "side":
                lower_split += 6
                higher_split += 3
            elif self.player_last_attack_direction_I is "belly":
                lower_split -= 3
                higher_split -= 6
            elif self.player_last_attack_direction_II is "head":
                lower_split -= 3
                higher_split += 3

            if self.player_attack_direction is "body" or self.player_attack_direction is "head":
                lower_split -= 5
                higher_split -= 10
                special_split -= 15
            elif self.player_attack_direction is "side":
                lower_split += 8
                higher_split += 4
            elif self.player_attack_direction is "belly":
                lower_split -= 4
                higher_split -= 8
            elif self.player_last_attack_direction_II is "head":
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
                  self.opponent_last_direction_I, ",", self.opponent_last_action_II, "-", self.opponent_last_direction_II)

        return

    def attack_output(self, strike_type, strike_dir, opponent):
        # generating random number
        random_num = random.randint(0, 100)

        self.opponent_defence_action(opponent, strike_type, strike_dir)

        # editing of levels
        if self.opponent_action is "":
            lower_border = -200
            middle_border = -200
            higher_border = 60
            if player.difficulty is "easy":
                higher_border = 45

            if self.player_attack_direction is "head":
                higher_border += 6

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
                lower_border = 15
                middle_border = 35
                higher_border = 70
                if player.difficulty is "easy":
                    lower_border = 8
                    middle_border = 30
                    higher_border = 60
            else:  # player weapon type is heavy
                lower_border = 35
                middle_border = 70
                higher_border = 90
                if player.difficulty is "easy":
                    lower_border = 25
                    middle_border = 60
                    higher_border = 85

            # opponent weapon effects
            if opponent.weapon.weapon_class is "unarmed":
                lower_border += 12
                middle_border += 10
                higher_border += 8
            elif opponent.weapon.weapon_type is "light":
                lower_border += 4
                middle_border += 3
                higher_border += 2
            else:  # player weapon type is heavy
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

            # player armor effects
            if "helmet" in player.gear:
                lower_border += 1
                higher_border += 1
            if "armor" in player.gear:
                lower_border += 3
                middle_border += 2
                higher_border += 2

            # opponent armor effects
            if "helmet" in opponent.gear:
                lower_border -= 4
                middle_border -= 3
                higher_border -= 3
            if "armor" in opponent.gear:
                lower_border += 6
                middle_border += 5
                higher_border += 5

            lower_border += opponent.dodge_effectiveness
            middle_border += opponent.dodge_effectiveness
            higher_border += opponent.dodge_effectiveness
        else:
            # setting base levels depending on player weapon
            if player.weapon.weapon_class is "unarmed":
                lower_border = 50
                middle_border = 90
                higher_border = 100
                if player.difficulty is "easy":
                    lower_border = -200
                    middle_border = -200
                    higher_border = 20
            elif player.weapon.weapon_type is "light":
                lower_border = 40
                middle_border = 70
                higher_border = 90
                if player.difficulty is "easy":
                    lower_border = 30
                    middle_border = 60
                    higher_border = 85
            else:  # player weapon type is heavy
                lower_border = 20
                middle_border = 45
                higher_border = 75
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
            else:  # player weapon type is heavy
                lower_border += 15
                middle_border += 15
                higher_border += 10

            # player armor effects
            if "helmet" in player.gear:
                lower_border += 1
                higher_border += 1
            if "armor" in player.gear:
                lower_border += 3
                middle_border += 2
                higher_border += 2

            # opponent armor effects
            if "helmet" in opponent.gear:
                lower_border -= 1
                middle_border -= 1
                higher_border -= 1
            if "armor" in opponent.gear:
                lower_border += 2
                middle_border += 1
                higher_border += 1

            lower_border += opponent.block_effectiveness
            middle_border += opponent.block_effectiveness
            higher_border += opponent.block_effectiveness

        # debug part
        if player.test is True:
            print(random_num, lower_border, middle_border, higher_border)
            time.sleep(1)

        # result
        last_action = "attack"
        """
        if random_num <= lower_border:
            self.attack_major_fail()
            last_action = "defence"
        elif random_num < higher_border:
            self.attack_minor_success(strike_dir, strike_type)
        else:
            self.attack_major_success(strike_dir, strike_type)
        """
        return last_action

    # defence

    # conclusion
    def returning_from_technique(self):
        if player.weapon is short_sword_mordhau:
            player.weapon = short_sword

        return


fight = Fight(2)
fight.fight()
input()
