import time
import random
from Recnamorcen.main_funcs import *
from Recnamorcen.fight import *
from Recnamorcen.travel import *


class Game:
    # fight variables
    room_three_fight = 0
    room_four_fight = 0
    first_fight = random.randint(0, 1)

    # player
    short_sword_xp = 0
    two_handed_axe_xp = 0
    dagger_xp = 0
    unarmed_xp = 0
    difficulty = ""
    max_health = 1
    health = 1
    last_health = 1
    stamina = 1
    player_gear = []
    character = ""
    weapon = "twoHandedAxe"
    damage_type = []
    weapon_type = ""
    healing_potion_count = 0

    # opponent
    opponent = ""
    opponent_health = 1
    opponent_max_health = 1
    opponent_stamina = 1
    opponent_max_stamina = 1
    opponent_stamina_growth = 1
    opponent_info = ""
    opponent_weapon = ""
    opponent_defence = []
    opponent_weapon_type = ""
    opponent_damage_type = []
    opponent_strength = 1
    opponent_action = ""
    opponent_gear = []
    last_attack_zone = ""

    def __init__(self):
        self.x = 0
        self.y = 0
        self.last_direction = None

        if self.weapon == "shortSword":
            self.damage_type = ["cut", "stab"]
            self.weapon_type = "light"
            self.strength = 5
            self.stamina = 8
            self.stamina_growth = 1.5
            if self.character == "human":
                self.strength += 0.5
                self.stamina += 1
                self.stamina_growth += 0.5
            if 50 < self.short_sword_xp:
                self.stamina += 1
                if 150 <= self.short_sword_xp:
                    self.stamina_growth += 0.5
        elif self.weapon == "twoHandedAxe":
            self.damage_type = ["cut"]
            self.weapon_type = "heavy"
            self.strength = 8
            self.stamina = 6
            self.stamina_growth = 1
            if self.character == "dwarf":
                self.strength += 2
            if 50 < self.two_handed_axe_xp:
                self.stamina += 1
                if 150 <= self.two_handed_axe_xp:
                    self.stamina_growth += 0.5
        elif self.weapon == "dagger":
            self.damage_type = ["cut", "stab"]
            self.weapon_type = "light"
            self.strength = 3
            self.stamina = 9
            self.stamina_growth = 2
            if self.character == "elf":
                self.stamina += 2
                self.stamina_growth += 0.5
            if 50 < self.dagger_xp:
                self.stamina += 1
                if 150 <= self.dagger_xp:
                    self.stamina_growth += 0.5
        elif self.weapon == "fists":
            self.damage_type = ["smash"]
            self.weapon_type = "light"
            if self.character == "dwarf":
                self.stamina = 14
                self.strength = 3
                self.stamina_growth = 2.5
            elif self.character == "human":
                self.stamina = 16
                self.strength = 2
                self.stamina_growth = 2.5
            elif self.character == "elf":
                self.stamina = 18
                self.strength = 1.5
                self.stamina_growth = 3
            if 20 < self.unarmed_xp:
                self.stamina += 2
                if 50 <= self.unarmed_xp:
                    self.stamina_growth += 0.5
                    self.strength += 1

        self.max_stamina = self.stamina

    def headline(self):
        time.sleep(0.3)
        slow_print("Vítejte v Reknamorcenovi  -  verze Alpha 0.133\n")
        return self.introduction()

    def introduction(self):
        time.sleep(0.8)
        while True:
            starting_option = input("Chcete začít [h]rát, [n]ačíst uloženou hru, [o]tevřít patch notes nebo "
                                    "si [p]řečíst návod?  -  (pro vybrání možnosti opište slovo v hranaté "
                                    "závorce a zmáčkněte enter.)\n")
            while True:
                if starting_option == "h":
                    return self.difficulty_selection()
                elif starting_option == "n":
                    slow_print("Načítání stále ještě není implementováno.\n"
                               "\nMůžete si vybrat jinou možnost:\n")
                    break
                elif starting_option == "o":
                    slow_print("Patch Notes zatím nejsou k dispozici.\n"
                               "\nMůžete si vybrat jinou možnost:\n")
                    break
                elif starting_option == "p":
                    slow_print("Návod zatím ještě není k dispozici. \n"
                               "\nMůžete si vybrat jinou možnost:\n")
                    input()
                    break
                else:
                    wrong_input(0)
                starting_option = input()

    def difficulty_selection(self):
        slow_print("Vyberte prosím obtížnost: \n")
        time.sleep(0.2)
        slow_print("    [l]ehká - možnost ukládání, málo a lehých soubojů.\n"
                   "    [s]třední - možnost ukládání, málo těžkých soubojů.\n"
                   "    [t]ěžká - bez ukládání, hodně a těžkých soubojů.\n")
        while True:
            difficulty_selection = input()
            if difficulty_selection == "t":
                slow_print("Vybrali jste si těžkou obtížnost, teď už vám můžeme popřát jen hodně štěstí.")
                self.difficulty = "hard"
                break
            elif difficulty_selection == "s":
                slow_print("Vybrali jste si střední obtížnost, doufám že si to užijete.")
                self.difficulty = "medium"
                break
            elif difficulty_selection == "l":
                slow_print("Vybrali jste si lehkou obtížnost, popřál bych vám hodně štěstí, ale nebudete ho "
                           "potřebovat.")
                self.difficulty = "easy"
                break
            else:
                wrong_input(0)

        return self.character_selection()

    def character_selection(self):
        slow_print("Vyberte si postavu: \n"
                   "    [t]rpaslík\n"
                   "    [č]lověk\n"
                   "    [e]lf\n")
        while True:
            character_selection = input()
            if character_selection == "t":
                slow_print("Jste trpaslík, trpaslíci jsou malá a velice silná stvoření. Vydrží spoustu ran a dokonce"
                           " mají i přirozenou ochranu proti otravě, ale nejsou moc mrštní.\n")
                self.max_health = 24
                self.last_health = 24
                self.health = 24
                return self.dwarf_introduction()
            elif character_selection == "č":
                slow_print("Jste člověk, vaše rasa je vysoká a když už dá někomu ránu pěstí tak to i zabolí, ale silou"
                           " se nevyrovná trpaslíkům a mrštností elfům. Daloby se říct, že je to taková zlatá střední"
                           " cesta.\n")
                self.max_health = 20
                self.last_health = 20
                self.health = 20
                return self.human_introduction()
            elif character_selection == "e":
                slow_print("Jste elf, jste ohromně mrštný, tak že vyhýbat se útokům nepřátel je pro vás"
                           " hračka. Ovšem když přijde na hrubou sílu tak ta vám trochu schází.\n")
                self.max_health = 18
                self.last_health = 18
                self.health = 18
                return self.elf_introduction()
            else:
                wrong_input(0)

    def dwarf_introduction(self):
        self.x = 3
        self.y = 3
        self.last_direction = None

        return self.room_picking()

    def human_introduction(self):
        self.x = 3
        self.y = 2
        self.last_direction = None

        return self.room_picking()

    def elf_introduction(self):
        self.x = 0
        self.y = 2
        self.last_direction = None

        return self.room_picking()

    def rolling_dice(self):
        dice_roll = random.randint(1, 7)

        if dice_roll >= 6:
            slow_print("Padla 6")
            # slow_print("\"Ty máš ale štěstí!\"\n")
            return 1

        elif dice_roll <= 5:
            slow_print("Padla " + str(dice_roll))
            slow_print("\"Smůla, házíš znovu.\"\n")
            return 0

    # fight
    def fight(self, opponent_level):
        # určí první akci souboje
        last_action = self.first_fight_action()

        # vytvoří protivníka a uvede ho
        self.opponent_creation(opponent_level)
        print("Stojí před vámi", self.opponent, self.opponent_weapon)

        # samotný souboj
        while self.opponent_health > 0:
            # když hráč ztratí všechen život
            if self.health <= 0:
                self.player_killed()

            # oznámí stav o životě a výdrži hráče a protivníka
            self.fight_status()

            # útok na soupeře
            if last_action == "defence":
                last_action = self.random_num_definition(self.strike_direction_choosing)

            # obrana před soupeřovým útokem
            else:
                last_action = self.random_num_definition(self.guard_choosing)

        # ukončovací hláška
        self.last_attack_zone = ""
        end_call = random.randint(0, 1)
        if end_call == 0:
            slow_print("Zabili jste ho.\n")
        elif end_call == 1:
            slow_print("Tohle už nepřežil.\n")

    def attack_output(self, random_num, higher_border, lower_border, strike_type, strike_dir):
        # editing of levels
        if (self.opponent_weapon == "beze zbraně" or self.opponent_weapon == "kusadla") and self.opponent_defence != []:
            self.opponent_action = "Protivník se snažil vaší ráně uskočit."
            if "block" in self.opponent_defence:
                higher_border -= 30
                lower_border -= 3
            elif "dodge" in self.opponent_defence:
                if self.weapon_type == "heavy":
                    lower_border += 15
                    higher_border += 3
                elif self.weapon_type == "light":
                    higher_border -= 8
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
        else:
            self.opponent_action = "Protivník se vaší ráně nijak nebránil."
            higher_border -= 25
            lower_border -= 3
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

        return last_action

    def strike_direction_choosing(self, random_num, higher_border, lower_border):
        strike_type = "stab"
        strike_dir = "body"
        if "cut" and "stab" in self.damage_type:
            slow_print("Chcete [b]odat, nebo [s]ekat?")
            while True:
                attack_type = input()
                if attack_type == "b":
                    slow_print("Chcete bodat do [t]ěla, nebo na [h]lavu?")
                    while True:
                        attack_direction = input()
                        if attack_direction == "t":
                            break
                        elif attack_direction == "h":
                            strike_dir = "head"
                            break
                        else:
                            wrong_input(0)
                elif attack_type == "s":
                    strike_type = "chop"
                    slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
                    while True:
                        attack_direction = input()
                        if attack_direction == "o" or attack_direction == "b":
                            break
                        elif attack_direction == "h":
                            strike_dir = "head"
                            break
                        else:
                            wrong_input(0)
                    break
                else:
                    wrong_input(0)
        elif "stab" in self.damage_type:
            slow_print("Chcete bodat do [t]ěla, nebo na [h]lavu?")
            while True:
                attack_direction = input()
                if attack_direction == "t":
                    break
                elif attack_direction == "h":
                    strike_dir = "head"
                    break
                else:
                    wrong_input(0)
        elif "cut" in self.damage_type:
            strike_type = "chop"
            slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
            while True:
                attack_direction = input()
                if attack_direction == "h":
                    strike_dir = "head"
                    break
                elif attack_direction == "o" or attack_direction == "b":
                    break
                else:
                    wrong_input(0)
        elif self.weapon == "fists":
            strike_type = "punch"
            slow_print("Chcete ho praštit do [h]lavy, nebo do [b]řicha?")
            while True:
                attack_direction = input()
                if attack_direction == "b":
                    break
                elif attack_direction == "h":
                    strike_dir = "head"
                    break
                else:
                    wrong_input(0)
        elif "smash" in self.damage_type:
            strike_type = "smash"
            slow_print("Chcete zaútočit na b[o]k, [b]řicho, nebo na [h]lavu?\n")
            while True:
                attack_direction = input()
                if attack_direction == "o" or attack_direction == "b":
                    break
                elif attack_direction == "h":
                    strike_dir = "head"
                    break
                else:
                    wrong_input(0)

        return self.attack_output(random_num, higher_border, lower_border, strike_type, strike_dir)

    def attack_major_fail(self):
        slow_print(self.opponent_action)
        time.sleep(0.4)
        if self.opponent_action == "Protivník se snažil vaši ránu zablokovat.":
            if self.weapon != "fists":
                slow_print("Což se mu povedlo ve chvíli, kdy už jste počítali, že ho zasáhnete plnou silou a tak "
                           "vás to, že vaše zbraň zastavila o jeho rozhodilo, že než jste se vzpamatovali, "
                           "zasadil vám ránu.\n")
            else:
                slow_print("")
        elif self.opponent_action == "Protivník se snažil vaší ráně uskočit.":
            if self.opponent_weapon != "fists":
                slow_print("Což se mu povedlo ve chvíli, kdy už jste počítali, že ho zasáhnete plnou silou a tak "
                           "vás to rozhodilo, že než jste se vzpamatovali, zasadil vám ránu.\n")
            else:
                slow_print("")
        self.health -= self.opponent_strength

        return

    def attack_minor_success(self, strike_dir, strike_type):
        damage = 0
        slow_print(self.opponent_action)
        time.sleep(0.4)
        slow_print("Ale nebyl do rychlý a tak se vám mu podařilo zasadit ránu, ale ne příliš velkou.\n")
        if strike_dir == "head":
            if "helmet" in self.opponent_gear:
                damage += self.strength // 4 + 1
                if strike_type == "smash":
                    damage += 1
                elif strike_type == "chop":
                    damage -= 2
                if self.weapon_type == "heavy":
                    damage += 1.5
            else:
                damage += self.strength // 2 + 1.5
                if strike_type == "chop":
                    damage += 2
        else:
            if "armor" in self.opponent_gear:
                damage += self.strength // 4
                if strike_type == "smash":
                    damage += 1
                elif strike_type == "chop":
                    damage -= 2
                if self.weapon_type == "heavy":
                    damage += 1.5
            else:
                damage += self.strength // 2
                if strike_type == "chop":
                    damage += 2
        if damage < 0:
            damage = 0
        self.opponent_health -= damage

        return

    def attack_major_success(self, strike_dir, strike_type):
        damage = 0
        slow_print(self.opponent_action)
        time.sleep(0.4)
        slow_print("Ovšem vám se povedlo váš útok provést tak rychle a dát do něj tolik síly, že se vám povedlo"
                   " soupeře zasáhnou tak tvrdě, že ho to muselo opravdu bolet.\n")
        if strike_dir == "head":
            if "helmet" in self.opponent_gear:
                damage += self.strength // 2 + 1
                if strike_type == "smash":
                    damage += 2
                elif strike_type == "chop":
                    damage -= 1
                if self.weapon_type == "heavy":
                    damage += 1.5
            else:
                damage += self.strength + 1.5
                if strike_type == "chop":
                    damage += 3
        else:
            if "armor" in self.opponent_gear:
                damage += self.strength // 4
                if strike_type == "smash":
                    damage += 2
                elif strike_type == "chop":
                    damage -= 1
                if self.weapon_type == "heavy":
                    damage += 1.5
            else:
                damage += self.strength // 2
                if strike_type == "chop":
                    damage += 3
        if damage < 0:
            damage = 0
        self.opponent_health -= damage

        return

    def defence_output(self, random_num, higher_border, lower_border, defence_type, expected_attack):
        opponent_attack_zone = random.randint(0, 29)
        lower_one = 9
        higher_one = 19
        if "helmet" in self.player_gear and "armor" not in self.player_gear:
            lower_one -= 3
            higher_one -= 6
        elif "helmet" not in self.player_gear and "armor" in self.player_gear:
            lower_one += 3
            higher_one += 6
        if self.last_attack_zone == "belly":
            lower_one -= 4
            higher_one -= 2
        elif self.last_attack_zone == "side":
            lower_one += 2
            higher_one -= 2
        elif self.last_attack_zone == "head":
            higher_one += 4
            lower_one += 2

        # editing of levels
        if opponent_attack_zone < lower_one:
            # břicho
            slow_print("Nepřítel vám zaútočil na vaše břicho.")
            self.last_attack_zone = "belly"
            if defence_type == "dodge":
                if expected_attack == "right":
                    lower_border += 20
                    higher_border += 10
                elif expected_attack == "left":
                    lower_border -= 5
                    higher_border -= 15
                elif expected_attack == "down":
                    higher_border -= 5
            elif defence_type == "block":
                if expected_attack == "right":
                    higher_border += 5
                elif expected_attack == "left":
                    lower_border -= 5
                    higher_border -= 20
                elif expected_attack == "down":
                    higher_border += 8
                    lower_border += 5
        elif opponent_attack_zone < higher_one:
            slow_print("Nepřítel vám zaútočil na váš bok.")
            self.last_attack_zone = "side"
            # bok
            if defence_type == "dodge":
                if expected_attack == "left":
                    lower_border += 20
                    higher_border += 10
                elif expected_attack == "right":
                    lower_border -= 5
                    higher_border -= 15
                elif expected_attack == "down":
                    higher_border -= 5
            elif defence_type == "block":
                if expected_attack == "left":
                    higher_border += 5
                elif expected_attack == "right":
                    lower_border -= 5
                    higher_border -= 20
                elif expected_attack == "down":
                    higher_border += 5
                    lower_border += 3
        else:
            slow_print("Nepřítel vám zaútočil na hlavu.")
            self.last_attack_zone = "head"
            # hlava
            if defence_type == "dodge":
                if expected_attack == "right":
                    lower_border -= 5
                    higher_border -= 15
                elif expected_attack == "left":
                    lower_border -= 5
                    higher_border -= 15
                elif expected_attack == "down":
                    higher_border += 10
                    lower_border += 15
            elif defence_type == "block":
                if expected_attack == "right":
                    lower_border += 5
                    higher_border += 3
                elif expected_attack == "down":
                    lower_border -= 5
                    higher_border -= 20
                elif expected_attack == "left":
                    higher_border += 8
                    lower_border += 5

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
        last_action = "defence"
        if random_num <= lower_border:
            slow_print("Teď se vám to nepovedlo a dostali jste od soupeře ránu.")
            self.health -= self.opponent_strength
        elif lower_border < random_num < higher_border:
            if self.difficulty == "easy":
                slow_print("Povedlo se vám to a soupeř vás nezranil.")
                self.health -= self.opponent_strength
            else:
                slow_print("Povedlo se vám se jakš takš ubránit a soupeř vás zranil jen lehce")
                self.health -= self.opponent_strength / 3
        elif higher_border <= random_num:
            slow_print("Povedlo se vám to tak dobře, že jste ještě naoplátku zasáhli soupeře.")
            last_action = "attack"
            self.opponent_health -= self.strength

        return last_action

    def guard_choosing(self, random_num, higher_border, lower_border):
        slow_print("Chcete se spíše snažit soupeřův útok [z]ablokovat, nebo se mu [v]yhnou?\n")
        while True:
            defence_choice = input()
            if defence_choice == "z":
                defence_type = "block"
                return self.blocking(random_num, higher_border, lower_border, defence_type)
            elif defence_choice == "v":
                defence_type = "dodge"
                return self.dodging(random_num, higher_border, lower_border, defence_type)
            else:
                wrong_input(0)

    def dodging(self, random_num, higher_border, lower_border, defence_type):
        slow_print("Kterým směrem chcete uskočit, do[l]eva, do[p]rava, nebo do[z]adu?")
        while True:
            move_choice = input()
            if move_choice == "l":
                expected_attack = "right"
                break
            elif move_choice == "z":
                expected_attack = "down"
                break
            elif move_choice == "p":
                expected_attack = "left"
                break
            else:
                wrong_input(0)

        return self.defence_output(random_num, higher_border, lower_border, defence_type, expected_attack)

    def blocking(self, random_num, higher_border, lower_border, defence_type):
        slow_print("Kam přepokládáte, že soupeř zaútočí na [h]lavu, na b[o]k, nebo na [b]řicho?")
        while True:
            block_choice = input()
            if block_choice == "h":
                expected_attack = "down"
                break
            elif block_choice == "o":
                expected_attack = "right"
                break
            elif block_choice == "b":
                expected_attack = "left"
                break
            else:
                wrong_input(0)

        return self.defence_output(random_num, higher_border, lower_border, defence_type, expected_attack)

    def random_num_definition(self, func):
        random_num = random.randint(0, 100)

        # setting base levels
        if self.difficulty == "easy":
            lower_border = 15  # 5
            higher_border = 65  # 85
        else:
            lower_border = 25  # 15
            higher_border = 75  # 95

        return func(random_num, higher_border, lower_border)

    def opponent_creation(self, opponent_difficulty):
        if opponent_difficulty == 0:
            num = 2
            if self.difficulty == "hard":
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

        elif opponent_difficulty == 2:
            opponent_number = random.randint(0, 0)
            if opponent_number == 0:
                self.opponent = "ork"
                self.opponent_health = random.randint(16, 26)
                self.opponent_info = ""
                self.opponent_defence = ["block"]

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

        self.opponent_max_health = self.opponent_health
        self.opponent_max_stamina = self.opponent_stamina
        return

    def fight_status(self):
        if self.opponent_max_health - self.opponent_max_health / 16 < self.opponent_health:
            opponent_health_state = "bez zranění"
        elif self.opponent_max_health - self.opponent_max_health / 4 < self.opponent_health:
            opponent_health_state = "lehce zraněn"
        elif self.opponent_max_health - self.opponent_max_health / 1.5 < self.opponent_health:
            opponent_health_state = "středně zraněn"
        elif self.opponent_max_health - self.opponent_max_health / 0.5 < self.opponent_health:
            opponent_health_state = "těžce zraněn"
        else:
            opponent_health_state = "velmi těžce zraněn"
        opponent_stamina_state = "plný energie"
        time.sleep(0.3)
        slow_print("    Váš život: " + str(self.health) + "/" + str(self.last_health))
        slow_print("    Vaše energie: " + str(self.stamina) + "/" + str(self.max_stamina) + "\n")
        time.sleep(0.3)
        slow_print("    Soupeř vypadá " + opponent_health_state
                   + "    " + str(self.opponent_health) + "/" + str(self.opponent_max_health))
        slow_print("    Soupeř vypadá " + opponent_stamina_state
                   + "    " + str(self.opponent_stamina) + "/" + str(self.opponent_max_stamina) + "\n")
        time.sleep(0.25)

        return

    def first_fight_action(self):
        loudness = 3
        if self.character == "dwarf":
            loudness += 3
        elif self.character == "human":
            loudness += 2
        if "helmet" in self.player_gear:
            loudness += 3
        if "armor" in self.player_gear:
            loudness += 5
        first_opponent_action = "defence"
        if loudness > 10:
            first_opponent_action = "attack"
        elif loudness > 5:
            if random.randint(0, loudness) < 6:
                first_opponent_action = "attack"

        return first_opponent_action

    def player_killed(self):
        time.sleep(0.6)
        slow_print("Jste mrtev.\n")
        time.sleep(0.8)
        slow_print("Chcete [z]ačít znovu, nebo [o]dejít?")
        escape_result = input()
        if escape_result == "o":
            shutdown()
        elif escape_result == "z":
            self.introduction()
        else:
            wrong_input(0)

    # travelling
    def room_picking(self):
        while True:
            if self.x == 0 and self.y == 2:
                self.room_six_spawn_two()
            elif self.x == 1 and self.y == 2:
                self.room_five()
            elif self.x == 2 and self.y == 2:
                self.room_three()
            elif self.x == 2 and self.y == 1:
                self.room_four_exit()
            elif self.x == 2 and self.y == 0:
                slow_print("Šlápli jste na past a ze zdi vystřelily otrávené šipky, ale měli jste štěstí a netrefily"
                           " vás, ale najednou vidíte před sebou jak se na vás něco ohromného otáčí.")
                self.fight(3)
                slow_print("Tohle je konec dema, na pokračování si musíte počkat.")
                time.sleep(2)
                quit()
            elif self.x == 3 and self.y == 2:
                self.room_two()
            elif self.x == 3 and self.y == 3:
                self.room_one_spawn_one()

    def get_coordinates(self):
        if self.last_direction is "North":
            self.y -= 1
        elif self.last_direction is "East":
            self.x += 1
        elif self.last_direction is "South":
            self.y += 1
        elif self.last_direction is "West":
            self.x -= 1
        return

    def room_pattern_one(self, last_dir_old1, last_dir_new1):
        if self.last_direction is None:
            slow_print("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        elif self.last_direction is "{}".format(last_dir_old1):
            slow_print("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

        self.last_direction = "{}".format(last_dir_new1)
        return self.get_coordinates()

    def room_pattern_two(self, msg1, msg2, msg3, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                         last_dir_old1, last_dir_old2, last_dir_new1, last_dir_new2):
        while True:
            if self.last_direction is None:
                slow_print("{}".format(msg1))
                direction_choice = input()
                if direction_choice is "{}".format(pl_opt1):
                    self.last_direction = "{}".format(last_dir_new1)
                    break
                elif direction_choice is "{}".format(pl_opt2):
                    self.last_direction = "{}".format(last_dir_new2)
                    break
                else:
                    wrong_input(0)

            elif self.last_direction is "{}".format(last_dir_old1):
                slow_print("{}".format(msg2))
                direction_choice = input()
                if direction_choice is "{}".format(pl_opt3):
                    self.last_direction = "{}".format(last_dir_new1)
                    break
                elif direction_choice is "{}".format(pl_opt4):
                    self.last_direction = "{}".format(last_dir_new2)
                    break
                else:
                    wrong_input(0)

            elif self.last_direction is "{}".format(last_dir_old2):
                slow_print("{}".format(msg3))
                direction_choice = input()
                if direction_choice is "{}".format(pl_opt5):
                    self.last_direction = "{}".format(last_dir_new2)
                    break
                elif direction_choice is "{}".format(pl_opt6):
                    self.last_direction = "{}".format(last_dir_new1)
                    break
                else:
                    wrong_input(0)

        return self.get_coordinates()

    def room_pattern_three(self, msg1, msg2, msg3, msg4, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6, pl_opt7,
                           pl_opt8, pl_opt9, pl_opt10, pl_opt11, pl_opt12, last_dir_old1, last_dir_old2, last_dir_old3,
                           last_dir_new1, last_dir_new2, last_dir_new3):
        while True:
            if self.last_direction is None:
                slow_print(msg1)
                direction_choice = input()
                if direction_choice is pl_opt1:
                    self.last_direction = last_dir_new1
                    break
                elif direction_choice is pl_opt2:
                    self.last_direction = last_dir_new2
                    break
                elif direction_choice is pl_opt3:
                    self.last_direction = last_dir_new3
                    break
                else:
                    wrong_input(0)

            elif self.last_direction is last_dir_old1:
                slow_print(msg2)
                direction_choice = input()
                if direction_choice is pl_opt4:
                    self.last_direction = last_dir_new1
                    break
                elif direction_choice is pl_opt5:
                    self.last_direction = last_dir_new2
                    break
                elif direction_choice is pl_opt6:
                    self.last_direction = last_dir_new3
                    break
                else:
                    wrong_input(0)

            elif self.last_direction is last_dir_old2:
                slow_print(msg3)
                direction_choice = input()
                if direction_choice is pl_opt7:
                    self.last_direction = last_dir_new2
                    break
                elif direction_choice is pl_opt8:
                    self.last_direction = last_dir_new1
                    break
                elif direction_choice is pl_opt9:
                    self.last_direction = last_dir_new3
                    break
                else:
                    wrong_input(0)

            elif self.last_direction is last_dir_old3:
                slow_print(msg4)
                direction_choice = input()
                if direction_choice is pl_opt10:
                    self.last_direction = last_dir_new3
                    break
                elif direction_choice is pl_opt11:
                    self.last_direction = last_dir_new2
                    break
                elif direction_choice is pl_opt12:
                    self.last_direction = last_dir_new1
                    break
                else:
                    wrong_input(0)

        return self.get_coordinates()

    def room_type_n(self):
        last_dir_old1 = "South"
        last_dir_new1 = "North"

        return self.room_pattern_one(last_dir_old1, last_dir_new1)

    def room_type_e(self):
        last_dir_old1 = "West"
        last_dir_new1 = "East"

        return self.room_pattern_one(last_dir_old1, last_dir_new1)

    def room_type_s(self):
        last_dir_old1 = "North"
        last_dir_new1 = "South"

        return self.room_pattern_one(last_dir_old1, last_dir_new1)

    def room_type_w(self):
        last_dir_old1 = "East"
        last_dir_new1 = "West"

        return self.room_pattern_one(last_dir_old1, last_dir_new1)

    def room_type_ne(self):
        msg1 = "Můžete jít [r]ovně, nebo v[p]ravo.\n"
        pl_opt1 = "r"
        last_dir_new1 = "North"
        pl_opt2 = "p"
        last_dir_new2 = "East"

        last_dir_old1 = "South"
        msg2 = "Můžete jít [z]pět, nebo v[l]evo.\n"
        pl_opt3 = "z"
        pl_opt4 = "l"

        last_dir_old2 = "West"
        msg3 = "Můžete jít [z]pět, nebo v[p]ravo.\n"
        pl_opt5 = "z"
        pl_opt6 = "p"

        return self.room_pattern_two(msg1, msg2, msg3, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                     last_dir_old1, last_dir_old2, last_dir_new1, last_dir_new2)

    def room_type_ns(self):
        msg1 = "Můžete jít [r]ovně, nebo v[z]ad.\n"
        pl_opt1 = "r"
        last_dir_new1 = "North"
        pl_opt2 = "z"
        last_dir_new2 = "South"

        last_dir_old1 = "South"
        msg2 = "Můžete jít [z]pět, nebo [r]ovně.\n"
        pl_opt3 = "z"
        pl_opt4 = "r"

        last_dir_old2 = "North"
        msg3 = "Můžete jít [z]pět, nebo [r]ovně.\n"
        pl_opt5 = "z"
        pl_opt6 = "r"

        return self.room_pattern_two(msg1, msg2, msg3, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                     last_dir_old1, last_dir_old2, last_dir_new1, last_dir_new2)

    def room_type_nw(self):
        msg1 = "Můžete jít [r]ovně, nebo v[l]evo.\n"
        pl_opt1 = "r"
        last_dir_new1 = "North"
        pl_opt2 = "l"
        last_dir_new2 = "West"

        last_dir_old1 = "South"
        msg2 = "Můžete jít [z]pět, nebo v[p]ravo.\n"
        pl_opt3 = "z"
        pl_opt4 = "p"

        last_dir_old2 = "East"
        msg3 = "Můžete jít [z]pět, nebo v[l]evo.\n"
        pl_opt5 = "z"
        pl_opt6 = "l"

        return self.room_pattern_two(msg1, msg2, msg3, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                     last_dir_old1, last_dir_old2, last_dir_new1, last_dir_new2)

    def room_type_es(self):
        msg1 = "Můžete jít [r]ovně, nebo v[p]ravo.\n"
        pl_opt1 = "r"
        last_dir_new1 = "East"
        pl_opt2 = "p"
        last_dir_new2 = "South"

        last_dir_old1 = "West"
        msg2 = "Můžete jít [z]pět, nebo v[l]evo.\n"
        pl_opt3 = "z"
        pl_opt4 = "l"

        last_dir_old2 = "North"
        msg3 = "Můžete jít [z]pět, nebo v[p]ravo.\n"
        pl_opt5 = "z"
        pl_opt6 = "p"

        return self.room_pattern_two(msg1, msg2, msg3, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                     last_dir_old1, last_dir_old2, last_dir_new1, last_dir_new2)

    def room_type_ew(self):
        msg1 = "Můžete jít [r]ovně, nebo v[z]ad.\n"
        pl_opt1 = "r"
        last_dir_new1 = "East"
        pl_opt2 = "z"
        last_dir_new2 = "West"

        last_dir_old1 = "West"
        msg2 = "Můžete jít [z]pět, nebo [r]ovně.\n"
        pl_opt3 = "z"
        pl_opt4 = "r"

        last_dir_old2 = "East"
        msg3 = "Můžete jít [z]pět, nebo [r]ovně.\n"
        pl_opt5 = "z"
        pl_opt6 = "r"

        return self.room_pattern_two(msg1, msg2, msg3, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                     last_dir_old1, last_dir_old2, last_dir_new1, last_dir_new2)

    def room_type_sw(self):
        msg1 = "Můžete jít [r]ovně, nebo v[p]ravo.\n"
        pl_opt1 = "r"
        last_dir_new1 = "South"
        pl_opt2 = "p"
        last_dir_new2 = "West"

        last_dir_old1 = "North"
        msg2 = "Můžete jít [z]pět, nebo v[l]evo.\n"
        pl_opt3 = "z"
        pl_opt4 = "l"

        last_dir_old2 = "East"
        msg3 = "Můžete jít [z]pět, nebo v[p]ravo.\n"
        pl_opt5 = "z"
        pl_opt6 = "p"

        return self.room_pattern_two(msg1, msg2, msg3, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                     last_dir_old1, last_dir_old2, last_dir_new1, last_dir_new2)

    def room_type_nes(self):
        msg1 = "Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n"
        pl_opt1 = "r"  # 1
        last_dir_new1 = "North"
        pl_opt2 = "p"  # 2
        last_dir_new2 = "East"
        pl_opt3 = "z"  # 3
        last_dir_new3 = "South"

        last_dir_old1 = "South"
        msg2 = "Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n"
        pl_opt4 = "z"  # 1
        pl_opt5 = "l"  # 2
        pl_opt6 = "r"  # 3

        last_dir_old2 = "West"
        msg3 = "Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n"
        pl_opt7 = "z"  # 2
        pl_opt8 = "p"  # 1
        pl_opt9 = "l"  # 3

        last_dir_old3 = "North"
        msg4 = "Můžete jít [z]pět, [r]ovně, nebo v[p]ravo.\n"
        pl_opt10 = "z"  # 3
        pl_opt11 = "p"  # 2
        pl_opt12 = "r"  # 1

        return self.room_pattern_three(msg1, msg2, msg3, msg4, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                       pl_opt7, pl_opt8, pl_opt9, pl_opt10, pl_opt11, pl_opt12, last_dir_old1,
                                       last_dir_old2, last_dir_old3, last_dir_new1, last_dir_new2, last_dir_new3)

    def room_type_new(self):
        msg1 = "Můžete jít [r]ovně, v[p]ravo, nebo v[l]evo.\n"
        pl_opt1 = "r"  # 1
        last_dir_new1 = "North"
        pl_opt2 = "p"  # 2
        last_dir_new2 = "East"
        pl_opt3 = "l"  # 3
        last_dir_new3 = "West"

        last_dir_old1 = "South"
        msg2 = "Můžete jít [z]pět, v[l]evo, nebo v[p]ravo.\n"
        pl_opt4 = "z"  # 1
        pl_opt5 = "l"  # 2
        pl_opt6 = "p"  # 3

        last_dir_old2 = "West"
        msg3 = "Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n"
        pl_opt7 = "z"  # 2
        pl_opt8 = "p"  # 1
        pl_opt9 = "r"  # 3

        last_dir_old3 = "East"
        msg4 = "Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n"
        pl_opt10 = "z"  # 3
        pl_opt11 = "r"  # 2
        pl_opt12 = "l"  # 1

        return self.room_pattern_three(msg1, msg2, msg3, msg4, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                       pl_opt7, pl_opt8, pl_opt9, pl_opt10, pl_opt11, pl_opt12, last_dir_old1,
                                       last_dir_old2, last_dir_old3, last_dir_new1, last_dir_new2, last_dir_new3)

    def room_type_nsw(self):
        msg1 = "Můžete jít [r]ovně, v[l]evo, nebo v[z]ad.\n"
        pl_opt1 = "r"  # 1
        last_dir_new1 = "North"
        pl_opt2 = "l"  # 2
        last_dir_new2 = "West"
        pl_opt3 = "z"  # 3
        last_dir_new3 = "South"

        last_dir_old1 = "South"
        msg2 = "Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n"
        pl_opt4 = "z"  # 1
        pl_opt5 = "p"  # 2
        pl_opt6 = "r"  # 3

        last_dir_old2 = "North"
        msg3 = "Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n"
        pl_opt7 = "l"  # 2
        pl_opt8 = "r"  # 1
        pl_opt9 = "z"  # 3

        last_dir_old3 = "East"
        msg4 = "Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n"
        pl_opt10 = "p"  # 3
        pl_opt11 = "z"  # 2
        pl_opt12 = "l"  # 1

        return self.room_pattern_three(msg1, msg2, msg3, msg4, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                       pl_opt7, pl_opt8, pl_opt9, pl_opt10, pl_opt11, pl_opt12, last_dir_old1,
                                       last_dir_old2, last_dir_old3, last_dir_new1, last_dir_new2, last_dir_new3)

    def room_type_esw(self):
        msg1 = "Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n"
        pl_opt1 = "r"  # 1
        last_dir_new1 = "East"
        pl_opt2 = "p"  # 2
        last_dir_new2 = "South"
        pl_opt3 = "z"  # 3
        last_dir_new3 = "West"

        last_dir_old1 = "West"
        msg2 = "Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n"
        pl_opt4 = "z"  # 1
        pl_opt5 = "l"  # 2
        pl_opt6 = "r"  # 3

        last_dir_old2 = "North"
        msg3 = "Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n"
        pl_opt7 = "z"  # 2
        pl_opt8 = "p"  # 1
        pl_opt9 = "l"  # 3

        last_dir_old3 = "East"
        msg4 = "Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n"
        pl_opt10 = "z"  # 3
        pl_opt11 = "p"  # 2
        pl_opt12 = "r"  # 1

        return self.room_pattern_three(msg1, msg2, msg3, msg4, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                                       pl_opt7, pl_opt8, pl_opt9, pl_opt10, pl_opt11, pl_opt12, last_dir_old1,
                                       last_dir_old2, last_dir_old3, last_dir_new1, last_dir_new2, last_dir_new3)

    def room_type_nesw(self):
        while True:
            if self.last_direction is None:
                slow_print("Můžete jít [r]ovně, v[p]ravo, v[l]evo, nebo v[z]ad.\n")
                direction_choice = input()
                if direction_choice is "r":
                    self.last_direction = "North"
                    break
                elif direction_choice is "p":
                    self.last_direction = "East"
                    break
                elif direction_choice is "z":
                    self.last_direction = "South"
                    break
                elif direction_choice is "l":
                    self.last_direction = "West"
                    break
                else:
                    wrong_input(0)

            elif self.last_direction is "North":
                slow_print("Můžete jít [z]pět, v[l]evo, v[p]ravo, nebo [r]ovně.\n")
                direction_choice = input()
                if direction_choice is "z":
                    self.last_direction = "South"
                    break
                elif direction_choice is "l":
                    self.last_direction = "West"
                    break
                elif direction_choice is "r":
                    self.last_direction = "North"
                    break
                elif direction_choice is "p":
                    self.last_direction = "East"
                    break
                else:
                    wrong_input(0)

            elif self.last_direction is "East":
                slow_print("Můžete jít [z]pět, v[l]evo, v[p]ravo, nebo [r]ovně.\n")
                direction_choice = input()
                if direction_choice is "z":
                    self.last_direction = "West"
                    break
                elif direction_choice is "l":
                    self.last_direction = "North"
                    break
                elif direction_choice is "r":
                    self.last_direction = "East"
                    break
                elif direction_choice is "p":
                    self.last_direction = "South"
                    break
                else:
                    wrong_input(0)

            elif self.last_direction is "South":
                slow_print("Můžete jít [z]pět, v[l]evo, v[p]ravo, nebo [r]ovně.\n")
                direction_choice = input()
                if direction_choice is "z":
                    self.last_direction = "North"
                    break
                elif direction_choice is "l":
                    self.last_direction = "East"
                    break
                elif direction_choice is "r":
                    self.last_direction = "South"
                    break
                elif direction_choice is "p":
                    self.last_direction = "West"
                    break
                else:
                    wrong_input(0)

            elif self.last_direction is "West":
                slow_print("Můžete jít [z]pět, v[l]evo, v[p]ravo, nebo [r]ovně.\n")
                direction_choice = input()
                if direction_choice is "z":
                    self.last_direction = "East"
                    break
                elif direction_choice is "l":
                    self.last_direction = "South"
                    break
                elif direction_choice is "r":
                    self.last_direction = "West"
                    break
                elif direction_choice is "p":
                    self.last_direction = "North"
                    break
                else:
                    wrong_input(0)

        return self.get_coordinates()

    def room_one_spawn_one(self):
        self.room_type_n()

        return

    def room_two(self):
        self.room_type_sw()

        return

    def room_three(self):
        if self.first_fight == 0:
            if self.room_three_fight == 0:
                self.fight(0)
            self.room_three_fight += 1
        # last_health = fight(last_health)

        # healingPotionEffects = healingPotionUse(last_health)
        # last_health = healingPotionEffects[0]
        # healing_potion_count = healingPotionEffects[-1]

        self.room_type_new()

        return

    def room_four_exit(self):
        if self.first_fight == 1:
            if self.room_four_fight == 0:
                self.fight(0)
            self.room_four_fight += 1

        self.room_type_ns()

        return

    def room_five(self):
        self.room_type_ew()

        return

    def room_six_spawn_two(self):
        self.room_type_e()

        return


path = Game(0, 0)
# print(path.room_picking())
print(path.headline())

input()
