from fight import *


class RoomTypes:
    def get_coordinates(self):
        if player.last_direction is "North":
            player.y -= 1
        elif player.last_direction is "East":
            player.x += 1
        elif player.last_direction is "South":
            player.y += 1
        elif player.last_direction is "West":
            player.x -= 1
        return

    def room_pattern_one(self, last_dir_old1, last_dir_new1):
        while True:
            if player.last_direction is None:
                slow_print("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
            elif player.last_direction is "{}".format(last_dir_old1):
                slow_print("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
            direction_choice = base_options()
            if direction_choice != "skip":
                break

        player.last_direction = "{}".format(last_dir_new1)

        return self.get_coordinates()

    def room_pattern_two(self, msg1, msg2, msg3, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6,
                         last_dir_old1, last_dir_old2, last_dir_new1, last_dir_new2):
        while True:
            if player.last_direction is None:
                slow_print("{}".format(msg1))
                direction_choice = base_options()
                if direction_choice is "{}".format(pl_opt1):
                    player.last_direction = "{}".format(last_dir_new1)
                    break
                elif direction_choice is "{}".format(pl_opt2):
                    player.last_direction = "{}".format(last_dir_new2)
                    break
                elif direction_choice != "skip":
                    wrong_input(0)

            elif player.last_direction is "{}".format(last_dir_old1):
                slow_print("{}".format(msg2))
                direction_choice = base_options()
                if direction_choice is "{}".format(pl_opt3):
                    player.last_direction = "{}".format(last_dir_new1)
                    break
                elif direction_choice is "{}".format(pl_opt4):
                    player.last_direction = "{}".format(last_dir_new2)
                    break
                elif direction_choice != "skip":
                    wrong_input(0)

            elif player.last_direction is "{}".format(last_dir_old2):
                slow_print("{}".format(msg3))
                direction_choice = base_options()
                if direction_choice is "{}".format(pl_opt5):
                    player.last_direction = "{}".format(last_dir_new2)
                    break
                elif direction_choice is "{}".format(pl_opt6):
                    player.last_direction = "{}".format(last_dir_new1)
                    break
                elif direction_choice != "skip":
                    wrong_input(0)

        return self.get_coordinates()

    def room_pattern_three(self, msg1, msg2, msg3, msg4, pl_opt1, pl_opt2, pl_opt3, pl_opt4, pl_opt5, pl_opt6, pl_opt7,
                           pl_opt8, pl_opt9, pl_opt10, pl_opt11, pl_opt12, last_dir_old1, last_dir_old2, last_dir_old3,
                           last_dir_new1, last_dir_new2, last_dir_new3):
        while True:
            if player.last_direction is None:
                slow_print(msg1)
                direction_choice = base_options()
                if direction_choice is pl_opt1:
                    player.last_direction = last_dir_new1
                    break
                elif direction_choice is pl_opt2:
                    player.last_direction = last_dir_new2
                    break
                elif direction_choice is pl_opt3:
                    player.last_direction = last_dir_new3
                    break
                elif direction_choice != "skip":
                    wrong_input(0)

            elif player.last_direction is last_dir_old1:
                slow_print(msg2)
                direction_choice = base_options()
                if direction_choice is pl_opt4:
                    player.last_direction = last_dir_new1
                    break
                elif direction_choice is pl_opt5:
                    player.last_direction = last_dir_new2
                    break
                elif direction_choice is pl_opt6:
                    player.last_direction = last_dir_new3
                    break
                elif direction_choice != "skip":
                    wrong_input(0)

            elif player.last_direction is last_dir_old2:
                slow_print(msg3)
                direction_choice = base_options()
                if direction_choice is pl_opt7:
                    player.last_direction = last_dir_new2
                    break
                elif direction_choice is pl_opt8:
                    player.last_direction = last_dir_new1
                    break
                elif direction_choice is pl_opt9:
                    player.last_direction = last_dir_new3
                    break
                elif direction_choice != "skip":
                    wrong_input(0)

            elif player.last_direction is last_dir_old3:
                slow_print(msg4)
                direction_choice = base_options()
                if direction_choice is pl_opt10:
                    player.last_direction = last_dir_new3
                    break
                elif direction_choice is pl_opt11:
                    player.last_direction = last_dir_new2
                    break
                elif direction_choice is pl_opt12:
                    player.last_direction = last_dir_new1
                    break
                elif direction_choice != "skip":
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
            if player.last_direction is None:
                slow_print("Můžete jít [r]ovně, v[p]ravo, v[l]evo, nebo v[z]ad.\n")
                direction_choice = input()
                if direction_choice is "r":
                    player.last_direction = "North"
                    break
                elif direction_choice is "p":
                    player.last_direction = "East"
                    break
                elif direction_choice is "z":
                    player.last_direction = "South"
                    break
                elif direction_choice is "l":
                    player.last_direction = "West"
                    break
                else:
                    wrong_input(0)

            elif player.last_direction is "North":
                slow_print("Můžete jít [z]pět, v[l]evo, v[p]ravo, nebo [r]ovně.\n")
                direction_choice = input()
                if direction_choice is "z":
                    player.last_direction = "South"
                    break
                elif direction_choice is "l":
                    player.last_direction = "West"
                    break
                elif direction_choice is "r":
                    player.last_direction = "North"
                    break
                elif direction_choice is "p":
                    player.last_direction = "East"
                    break
                else:
                    wrong_input(0)

            elif player.last_direction is "East":
                slow_print("Můžete jít [z]pět, v[l]evo, v[p]ravo, nebo [r]ovně.\n")
                direction_choice = input()
                if direction_choice is "z":
                    player.last_direction = "West"
                    break
                elif direction_choice is "l":
                    player.last_direction = "North"
                    break
                elif direction_choice is "r":
                    player.last_direction = "East"
                    break
                elif direction_choice is "p":
                    player.last_direction = "South"
                    break
                else:
                    wrong_input(0)

            elif player.last_direction is "South":
                slow_print("Můžete jít [z]pět, v[l]evo, v[p]ravo, nebo [r]ovně.\n")
                direction_choice = input()
                if direction_choice is "z":
                    player.last_direction = "North"
                    break
                elif direction_choice is "l":
                    player.last_direction = "East"
                    break
                elif direction_choice is "r":
                    player.last_direction = "South"
                    break
                elif direction_choice is "p":
                    player.last_direction = "West"
                    break
                else:
                    wrong_input(0)

            elif player.last_direction is "West":
                slow_print("Můžete jít [z]pět, v[l]evo, v[p]ravo, nebo [r]ovně.\n")
                direction_choice = input()
                if direction_choice is "z":
                    player.last_direction = "East"
                    break
                elif direction_choice is "l":
                    player.last_direction = "South"
                    break
                elif direction_choice is "r":
                    player.last_direction = "West"
                    break
                elif direction_choice is "p":
                    player.last_direction = "North"
                    break
                else:
                    wrong_input(0)

        return self.get_coordinates()


class Rooms:
    fighting = Fight()
    r_types = RoomTypes()

    room_six_health_potions = True
    room_two_fight = False  # 1
    room_four_fight = True  # 2
    room_six_fight = True  # 2
    room_seven_fight = False  # 1
    room_eight_fight = True  # 3
    room_twelve_fight = False  # 1


    def room_one_spawn_one(self):
        self.r_types.room_type_n()

        player.last_fight = False

        return

    def room_two(self):
        if self.room_two_fight is True:
            self.fighting.main_(1)
            self.room_two_fight = False

            player.last_fight = True

        self.r_types.room_type_sw()

        return

    def room_three(self):

        player.last_fight = False

        self.r_types.room_type_nesw()

        return

    def room_four(self):
        if self.room_four_fight is True:
            self.fighting.main_(2)
            self.room_four_fight = False

            player.last_fight = True

        self.r_types.room_type_ns()

        return

    def room_five(self):
        player.last_fight = False

        self.r_types.room_type_ew()

        return

    def room_six(self):
        if self.room_six_fight is True:
            self.fighting.main_(2)
            self.room_six_fight = False

            player.last_fight = True

        if self.room_six_health_potions is True:
            while True:
                slow_print("Na zemi leží 2 léčící lektvary. Chcete si je [v]zít, nebo [n]e?\n")
                potion_choice = base_options()
                if potion_choice == "v":
                    player.health_potions += 2
                    self.room_six_health_potions = False
                    break
                elif potion_choice == "n":
                    break
                elif potion_choice != "skip":
                    wrong_input(0)

        self.r_types.room_type_e()

        return

    def room_seven(self):
        if self.room_seven_fight is True:
            self.fighting.main_(1)
            self.room_seven_fight = False

            player.last_fight = True

        self.r_types.room_type_ns()

        return

    def room_eight(self):
        if self.room_eight_fight is True:
            self.fighting.main_(3)
            self.room_eight_fight = False

            player.last_fight = True

        self.r_types.room_type_nsw()

        return

    def room_nine(self):
        player.last_fight = False

        self.r_types.room_type_n()

        return

    def room_ten_exit(self):
        player.last_fight = False

        slow_print("Vstoupili jste do další místnosti, vidíte před sebou schody vedoucí směrem dolů...\n")

        time.sleep(2)

        shutdown()

        self.r_types.room_type_e()

        return

    def room_eleven(self):
        player.last_fight = False

        self.r_types.room_type_ns()

        return

    def room_twelve(self):
        if self.room_twelve_fight is True:
            self.fighting.main_(1)
            self.room_twelve_fight = False

            player.last_fight = True

        self.r_types.room_type_sw()

        return

    def room_thirteen_spawn_two(self):
        player.last_fight = False

        self.r_types.room_type_e()

        return


class RoomChanging:
    rooms = Rooms()

    def room_picking(self):
        while True:
            if player.x == 0 and player.y == 2:
                self.rooms.room_six()
            elif player.x == 1 and player.y == 2:
                self.rooms.room_five()
            elif player.x == 2 and player.y == 2:
                self.rooms.room_three()
            elif player.x == 2 and player.y == 1:
                self.rooms.room_four()
            elif player.x == 2 and player.y == 0:
                self.rooms.room_eleven()
            elif player.x == 2 and player.y == -1:
                self.rooms.room_twelve()
            elif player.x == 1 and player.y == -1:
                self.rooms.room_thirteen_spawn_two()
            elif player.x == 3 and player.y == 2:
                self.rooms.room_two()
            elif player.x == 3 and player.y == 3:
                self.rooms.room_one_spawn_one()
            elif player.x == 2 and player.y == 3:
                self.rooms.room_seven()
            elif player.x == 2 and player.y == 4:
                self.rooms.room_eight()
            elif player.x == 2 and player.y == 5:
                self.rooms.room_nine()
            elif player.x == 1 and player.y == 4:
                self.rooms.room_ten_exit()
            else:
                # control part
                print("Na x - {} a y - {} nic není.".format(player.x, player.y))


path = RoomChanging()
path.room_picking()

input()
