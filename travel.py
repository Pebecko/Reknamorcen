from Recnamorcen.main_funcs import *


class Travelling:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.last_direction = None

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
                # self.fight(3)
                slow_print("Tohle je konec dema, na pokračování si musíte počkat.")
                shutdown()
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
        # if self.first_fight == 0:
            # if self.room_three_fight == 0:
                # self.fight(0)
            # self.room_three_fight += 1

        self.room_type_new()

        return

    def room_four_exit(self):
        # if self.first_fight == 1:
            # if self.room_four_fight == 0:
                # self.fight(0)
            # self.room_four_fight += 1

        self.room_type_ns()

        return

    def room_five(self):
        self.room_type_ew()

        return

    def room_six_spawn_two(self):
        self.room_type_e()

        return


path = Travelling(3, 3)
print(path.room_picking())

input()
