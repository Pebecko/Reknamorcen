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
