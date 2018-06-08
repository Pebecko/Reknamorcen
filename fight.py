from Recnamorcen.character_stats import *
from Recnamorcen.main_funcs import *
# from Recnamorcen.reknamorcen import *


class Fight:
    last_attack_zone = ""
    opponent_action = ""
    opponent_last_action_I = ""
    opponent_last_action_II = ""

    def __init__(self, opponent_level):
        self.opponent_level = opponent_level

    def fight(self):
        opponent = self.opponent_creation()
        slow_print("Stojí před vámi " + str(opponent.name) + ", " + str(opponent.info) + ". " + "A jeho zbraň je " +
                   str(opponent.weapon.name) + ", " + str(opponent.weapon.info) + ".")

        last_action = self.first_fight_action(opponent)

        self.special_fight_techniques()

        while opponent.health > 0:
            if player.health <= 0:
                player_killed(self)
            self.fight_status(opponent)

            # útok na soupeře
            if last_action == "defence":
                last_action = self.strike_direction_choosing(opponent)

            # obrana před soupeřovým útokem
            else:
                last_action = self.random_num_definition(self.guard_choosing)

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
            slow_print("Chcete si meč [o]tčit, abyste s ním molhy mlátit spíše než sekat, nebo [n]e??")
            while True:
                style_decision = base_options()
                if style_decision == "o":
                    player.weapon = short_sword_mordhau
                    break
                elif style_decision == "n":
                    break
                elif style_decision is "skip":
                    pass
                else:
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
        slow_print("    Soupeř vypadá " + opponent_health_state
                   + "    " + str(opponent.health) + "/" + str(opponent.max_health))
        slow_print("    Soupeř vypadá " + opponent_stamina_state
                   + "    " + str(opponent.weapon.stamina) + "/" + str(opponent.weapon.max_stamina) + "\n")
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
                        elif attack_direction is "skip":
                            pass
                        else:
                            wrong_input(0)
                elif attack_type == "s":
                    strike_type = "chop"
                    slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
                    while True:
                        attack_direction = ()
                        if attack_direction == "o" or attack_direction == "b":
                            break
                        elif attack_direction == "h":
                            strike_dir = "head"
                            break
                        elif attack_direction is "skip":
                            pass
                        else:
                            wrong_input(0)
                    break
                elif attack_type is "skip":
                    pass
                else:
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
                elif attack_direction is "skip":
                    pass
                else:
                    wrong_input(0)
        elif "cut" in player.weapon.damage_type:
            strike_type = "chop"
            slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
            while True:
                attack_direction = base_options()
                if attack_direction == "h":
                    strike_dir = "head"
                    break
                elif attack_direction == "o" or attack_direction == "b":
                    break

                elif attack_direction is "skip":
                    pass
                else:
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
                if attack_direction == "o" or attack_direction == "b":
                    break
                elif attack_direction == "h":
                    strike_dir = "head"
                    break
                elif attack_direction is "skip":
                    pass
                else:
                    wrong_input(0)

        return self.attack_output(strike_type, strike_dir, opponent)

    def attack_output(self, strike_type, strike_dir, opponent):
        random_num = random.randint(0, 100)
        # opponent action
        if opponent.defence is []:
            self.opponent_action = ""
            lower_border = -200
            middle_border = -200
            higher_border = 45
            if player.difficulty is "easy":
                higher_border = 60
        elif "dodge" in opponent.defence and "block" not in opponent.defence:
            self.opponent_action = "dodge"
        elif "block" in opponent.defence and "dodge" not in opponent.defence:
            self.opponent_action = "block"
        else:
            opponent_action_num = random.randint(0, 19)
            split = 6
            if player.weapon.weapon_type is "light":
                split += 8
            if opponent.weapon.weapon_type is "light":
                split -= 2
            elif opponent.weapon.weapon_type is "heavy":
                split += 2

            if self.opponent_last_action_II is "dodge":
                split = +1
            elif self.opponent_last_action_II is "block":
                split = -1
            if self.opponent_last_action_I is "dodge":
                split = +2
            elif self.opponent_last_action_I is "block":
                split = -2
            if self.opponent_action is "dodge":
                split = +2
            elif self.opponent_action is "block":
                split = -2

            self.opponent_last_action_II = self.opponent_last_action_I
            self.opponent_last_action_I = self.opponent_action

            if opponent_action_num < split:
                self.opponent_action = "block"
            else:
                self.opponent_action = "dodge"

        # action test
        print(self.opponent_action, self.opponent_last_action_I, self.opponent_last_action_II)

        # editing of levels
        if self.opponent_action is "dodge":
            if opponent.weapon.weapon_class is "unarmed":
                lower_border = 35
                middle_border = 70
                higher_border = 90
                if player.difficulty is "easy":
                    lower_border = 25
                    middle_border = 60
                    higher_border = 85
            elif player.weapon.weapon_type is "light":
                lower_border = 35
                middle_border = 70
                higher_border = 90
                if player.difficulty is "easy":
                    lower_border = 25
                    middle_border = 60
                    higher_border = 85
            else:
                lower_border = 35
                middle_border = 70
                higher_border = 90
                if player.difficulty is "easy":
                    lower_border = 25
                    middle_border = 60
                    higher_border = 85

            if opponent.weapon.weapon_type is "light":
                lower_border += 5
                middle_border += 3
                higher_border += 3
            else:
                lower_border += 5
                middle_border += 3
                higher_border += 3

            if "helmet" in player.gear:
                lower_border += 3
                higher_border += 3
            if "armor" in player.gear:
                lower_border += 5
                middle_border += 3
                higher_border += 3

        elif self.opponent_action is "block":
            pass
        """
        if opponent.weapon.weapon_class is "unarmed":
            opponent_action = "dodge"
            if player.weapon.weapon_type == "heavy":
                lower_border = 35
                middle_border = 70
                higher_border = 90
                if player.difficulty is "easy":
                    lower_border = 25
                    middle_border = 60
                    higher_border = 85
            elif player.weapon.weapon_type == "light":
                lower_border = 10
                middle_border = 70
                higher_border = 90
            if "helmet" in self.opponent_gear:
                higher_border -= 3
            if "armor" in self.opponent_gear:
                higher_border -= 5
        elif self.weapon_type == "light" and "block" in self.opponent_defence:
            lower_border += 5
            self.opponent_action = "Protivník se snažil vaši ránu zablokovat."
            if self.opponent_weapon_type == "heavy":
                lower_border += 10
            if "helmet" in self.opponent_gear:
                higher_border -= 1
            if "armor" in self.opponent_gear:
                higher_border -= 3
            if strike_type == "stab":
                higher_border -= 5
                lower_border -= 5
            elif strike_type == "smash":
                higher_border -= 5
                lower_border -= 5
            elif strike_type == "punch":
                higher_border += 10
                lower_border += 10
        elif self.weapon_type == "light" and "dodge" in self.opponent_defence:
            higher_border -= 10
            self.opponent_action = "Protivník se snažil vaší ráně uskočit."
            if self.opponent_weapon_type == "light":
                lower_border += 5
            elif self.opponent_weapon_type == "heavy":
                higher_border -= 5
            if "helmet" in self.opponent_gear:
                higher_border -= 3
            if "armor" in self.opponent_gear:
                higher_border -= 5
            if strike_type == "stab":
                higher_border += 5
                lower_border += 5
            elif strike_type == "smash":
                higher_border += 5
                lower_border += 5
            elif strike_type == "punch":
                higher_border -= 3
                lower_border -= 3
        elif self.weapon_type == "heavy" and "dodge" in self.opponent_defence:
            lower_border += 10
            self.opponent_action = "Protivník se snažil vaší ráně uskočit."
            if self.opponent_weapon_type == "light":
                lower_border += 5
            if "helmet" in self.opponent_gear:
                higher_border -= 3
            if "armor" in self.opponent_gear:
                higher_border -= 5
            if strike_type == "stab":
                higher_border += 5
                lower_border += 5
            elif strike_type == "smash":
                higher_border += 5
                lower_border += 5
            elif strike_type == "punch":
                higher_border -= 3
                lower_border -= 3
        elif self.weapon_type == "heavy" and "block" in self.opponent_defence:
            higher_border -= 15
            self.opponent_action = "Protivník se snažil vaši ránu zablokovat."
            if self.opponent_weapon_type == "heavy":
                lower_border += 5
                higher_border += 5
            if "helmet" in self.opponent_gear:
                higher_border -= 1
            if "armor" in self.opponent_gear:
                higher_border -= 3
            if strike_type == "stab":
                higher_border -= 5
                lower_border -= 5
            elif strike_type == "smash":
                higher_border -= 5
                lower_border -= 5
            elif strike_type == "punch":
                higher_border += 10
                lower_border += 10
        if "helmet" in self.player_gear:
            lower_border += 5
        if "armor" in self.player_gear:
            lower_border += 8
        if strike_dir == "head":
            lower_border += 5
            higher_border += 3

        # safety part
        if self.difficulty == "easy":
            if higher_border < 55:
                higher_border = 55
            if 35 < lower_border:
                lower_border = 35
        else:
            if higher_border < 60:
                higher_border = 60
            if 50 < lower_border:
                lower_border = 50

        # debug part
        print(random_num, lower_border, higher_border)
        time.sleep(1)

        # result
        last_action = "attack"
        if random_num <= lower_border:
            self.attack_major_fail()
            last_action = "defence"
        elif random_num < higher_border:
            self.attack_minor_success(strike_dir, strike_type)
        else:
            self.attack_major_success(strike_dir, strike_type)
        """
        return

    # defence

    # conclusion
    def returning_from_technique(self):
        if player.weapon is short_sword_mordhau:
            player.weapon = short_sword

        return


fight = Fight(2)
fight.fight()
input()
