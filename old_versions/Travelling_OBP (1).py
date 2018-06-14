import time
import sys
import random


def wrong_input(call):
    if call == 0:
        call = random.randint(1, 4)

    if call is 1:
        error_call = "Špatný vstup, zkuste to znovu.\n"
    elif call is 2:
        error_call = "Špatná možnost, zkuste to znovu.\n"
    elif call is 3:
        error_call = "Nekompatibilní vstup, zkuste to znovu.\n"
    elif call is 4:
        error_call = "To co jste zadali nesouhlasí s možnostmi.\n"
    else:
        error_call = "Špatný error call"
    return slow_print(error_call)


def slow_print(s):
    time = 0.015
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(time)
    print("")
    time.sleep(0.08)


class Game:
    short_sword_xp = 0
    two_handed_axe_xp = 0
    dagger_xp = 0
    unarmed_xp = 0
    difficulty = ""
    max_health = 1
    health = 1
    last_health = 1
    character = ""
    weapon = "fists"
    damage_type = ""
    healing_potion_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.last_direction = None
        self.stab = False

        if self.weapon == "shortSword":
            self.damage_type = "cut"
            self.stab = True
            self.strength = 6
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
            self.damage_type = "cut"
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
            self.damage_type = "cut"
            self.stab = True
            self.strength = 5
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
            self.damage_type = "smash"
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

    def headline(self):
        time.sleep(0.3)
        slow_print("Vítejte v Reknamorcenovi  -  verze Alpha 0.108\n")
        return self.introduction()

    def introduction(self):
        time.sleep(0.8)
        while True:
            slow_print("Chcete začít [hrát],[načíst] uloženou hru, [otevřít] patch notes nebo si [přečíst] návod?"
                       "  -  (pro vybrání možnosti opište slovo v hranaté závorce a zmáčkněte enter.)\n")
            while True:
                starting_option = input()
                if starting_option == "hrát":
                    return self.difficulty_selection()
                elif starting_option == "načíst":
                    slow_print("Načítání stále ještě není implementováno.\n"
                               "\nMůžete si vybrat jinou možnost:\n")
                    break
                elif starting_option == "otevřít":
                    slow_print("Patch Notes zatím nejsou k dispozici.\n"
                               "\nMůžete si vybrat jinou možnost:\n")
                    break
                elif starting_option == "přečíst":
                    slow_print("Návod zatím ještě není k dispozici. \n"
                               "\nMůžete si vybrat jinou možnost:\n")
                    input()
                    break
                else:
                    wrong_input(0)

    def difficulty_selection(self):
        slow_print("Vyberte prosím obtížnost: \n")
        time.sleep(0.2)
        slow_print(" [lehká] - možnost ukládání, málo a lehých soubojů.\n"
                   " [střední] - možnost ukládání, málo těžkých soubojů.\n"
                   " [těžká] - bez ukládání, hodně a těžkých soubojů.\n")
        while True:
            difficulty_selection = input()
            if difficulty_selection == "těžká":
                slow_print("Vybrali jste si těžkou obtížnost, teď už vám můžeme popřát jen hodně štěstí.")
                self.difficulty = "hard"
                break
            elif difficulty_selection == "střední":
                slow_print("Vybrali jste si střední obtížnost, doufám že si to užijete.")
                self.difficulty = "medium"
                break
            elif difficulty_selection == "lehká":
                slow_print("Vybrali jste si lehkou obtížnost, popřál bych vám hodně štěstí, ale nebudete ho "
                           "potřebovat.")
                self.difficulty = "easy"
                break
            else:
                wrong_input(0)

        return self.character_selection()

    def character_selection(self):
        slow_print("Vyberte si postavu: \n"
                   "    [trpaslík]\n"
                   "    [člověk]\n"
                   "    [elf]\n")
        while True:
            character_selection = input()
            if character_selection == "trpaslík":
                slow_print("Jste trpaslík, trpaslíci jsou malá a velice silná stvoření. Vydrží spoustu ran a dokonce"
                           " mají i přirozenou ochranu proti otravě, ale nejsou moc mrštní.\n")
                self.max_health = 24
                self.last_health = 24
                self.health = 24
                return self.dwarf_introduction()
            elif character_selection == "člověk":
                slow_print("Jste člověk, vaše rasa je vysoká a když už dá nškomu ránu pěstí tak to i zabolí, ale silou"
                           " se nevyrovná trpaslíkům a mrštností elfům. Daloby se říct, že je to taková zlatá střední"
                           " cesta.\n")
                self.max_health = 20
                self.last_health = 20
                self.health = 20
                return self.human_introduction()
            elif character_selection == "elf":
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
        pass

    def elf_introduction(self):
        pass

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

    def defence_output(self):
        random_num = random.randint(0, 100)
        higher_border = 100
        lower_border = 0

        if self.difficulty == "hard":
            lower_border = 15
            higher_border = 95
        elif self.difficulty == "medium":
            lower_border = 10
            higher_border = 90
        elif self.difficulty == "easy":
            lower_border = 5
            higher_border = 85

        if self.difficulty == "hard":
            if higher_border < 65:
                higher_border = 65
            if 45 < lower_border:
                lower_border = 45
        elif self.difficulty == "medium":
            if higher_border < 60:
                higher_border = 60
            if 40 < lower_border:
                lower_border = 40
        elif self.difficulty == "easy":
            if higher_border < 55:
                higher_border = 55
            if 35 < lower_border:
                lower_border = 35

        # result
        if random_num <= lower_border:
            pass
        elif lower_border < random_num < higher_borger:
            pass
        elif random_num <= higher_border:
            pass

    def attack_output(self):
        random_num = random.randint(0, 100)
        higher_border = 100
        lower_border = 0

        if self.difficulty == "hard":
            lower_border = 15
            higher_border = 95
        elif self.difficulty == "medium":
            lower_border = 10
            higher_border = 90
        elif self.difficulty == "easy":
            lower_border = 5
            higher_border = 85

        if self.difficulty == "hard":
            if higher_border < 65:
                higher_border = 65
            if 45 < lower_border:
                lower_border = 45
        elif self.difficulty == "medium":
            if higher_border < 60:
                higher_border = 60
            if 40 < lower_border:
                lower_border = 40
        elif self.difficulty == "easy":
            if higher_border < 55:
                higher_border = 55
            if 35 < lower_border:
                lower_border = 35

        # result
        if random_num <= lower_border:
            pass
        elif lower_border < random_num < higher_borger:
            pass
        elif random_num <= higher_border:
            pass

    def player_killed(self):
        time.sleep(0.6)
        slow_print("Jste mrtev.\n")
        time.sleep(0.8)
        slow_print("Chcete [začít] znovu, nebo [odejít]?")
        escape_result = input()
        if escape_result == "odejít":
            slow_print("SHUTTING DOWN...\n")
            time.sleep(0.4)
            quit()
        elif escape_result == "začít":
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
                slow_print("Šlápli jste na past a ze zdi vystřelily otrávené šipky, které vás zabily.")
                self.player_killed()
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
        # last_health = fight(last_health)

        # healingPotionEffects = healingPotionUse(last_health)
        # last_health = healingPotionEffects[0]
        # healing_potion_count = healingPotionEffects[-1]

        self.room_type_new()

        return

    def room_four_exit(self):
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
