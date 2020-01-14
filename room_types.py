from main_funcs import slow_print, base_options, wrong_input
from coordinates import Coordinates
from fight import Fight
from character_stats import player
from items import Items



class Room:
    fighting = Fight(player)

    def __init__(self, coordinates=Coordinates(), fight=None, items=Items()):
        self.coordinates = coordinates
        self.fight = fight
        self.items = items

    def basic_functions(self):
        self.fights()

        self.health_potion()
        return

    def fights(self):
        if self.fight is None:
            player.last_fight = False
        else:
            self.fighting.main(self.fight)
            player.last_fight = True
            self.fight = None

        return

    def health_potion(self):
        while self.items.health_potions > 0:
            if self.items.health_potions == 1:
                slow_print("Na zemi leží 1 léčící lektvar. Chcete si ho [v]zít, nebo [n]e?\n")
            elif self.items.health_potions < 5:
                slow_print("Na zemi leží {} léčící lektvary. Chcete si je [v]zít, nebo [n]e?\n"
                           "".format(self.items.health_potions))

            else:
                slow_print("Na zemi leží {} léčících lektvarů. Chcete si je [v]zít, nebo [n]e?\n"
                           "".format(self.items.health_potions))
            potion_choice = base_options()
            if potion_choice == "v":
                player.health_potions += self.items.health_potions
                self.items.health_potions = 0
            elif potion_choice == "n":
                break
            elif potion_choice != "skip":
                wrong_input()

    @staticmethod
    def get_coordinates():
        if player.last_direction is "North":
            player.coordinates.y += 1
        elif player.last_direction is "East":
            player.coordinates.x += 1
        elif player.last_direction is "South":
            player.coordinates.y -= 1
        elif player.last_direction is "West":
            player.coordinates.x -= 1
        return

    # TODO Make function for picking up thing and putting them down


# room patterns
class RoomPatternOne(Room):
    old_dir = ""
    new_dir = ""

    def pattern_one(self):
        while True:
            if player.last_direction is None:
                slow_print("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
            elif player.last_direction == self.old_dir:
                slow_print("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
            else:
                slow_print("Odkud jste to sakra přišli?")
            direction_choice = base_options()
            if direction_choice != "skip":
                break

        player.last_direction = self.new_dir

        self.get_coordinates()

        return


class RoomPatternTwo(Room):
    msg1 = ""
    msg2 = ""
    msg3 = ""
    pl_opt1 = ""
    pl_opt2 = ""
    pl_opt3 = ""
    pl_opt4 = ""
    pl_opt5 = ""
    pl_opt6 = ""
    last_dir_old1 = ""
    last_dir_old2 = ""
    last_dir_new1 = ""
    last_dir_new2 = ""

    def pattern_two(self):
        while True:
            if player.last_direction is None:
                slow_print(self.msg1)
                direction_choice = base_options()
                if direction_choice == self.pl_opt1:
                    player.last_direction = self.last_dir_new1
                    break
                elif direction_choice == self.pl_opt2:
                    player.last_direction = self.last_dir_new2
                    break
                elif direction_choice != "skip":
                    wrong_input()

            elif player.last_direction == self.last_dir_old1:
                slow_print(self.msg2)
                direction_choice = base_options()
                if direction_choice == self.pl_opt3:
                    player.last_direction = self.last_dir_new1
                    break
                elif direction_choice == self.pl_opt4:
                    player.last_direction = self.last_dir_new2
                    break
                elif direction_choice != "skip":
                    wrong_input()

            elif player.last_direction == self.last_dir_old2:
                slow_print(self.msg3)
                direction_choice = base_options()
                if direction_choice == self.pl_opt5:
                    player.last_direction = self.last_dir_new2
                    break
                elif direction_choice == self.pl_opt6:
                    player.last_direction = self.last_dir_new1
                    break
                elif direction_choice != "skip":
                    wrong_input()

        return self.get_coordinates()


class RoomPatternThree(Room):
    msg1 = ""
    msg2 = ""
    msg3 = ""
    msg4 = ""
    pl_opt1 = ""
    pl_opt2 = ""
    pl_opt3 = ""
    pl_opt4 = ""
    pl_opt5 = ""
    pl_opt6 = ""
    pl_opt7 = ""
    pl_opt8 = ""
    pl_opt9 = ""
    pl_opt10 = ""
    pl_opt11 = ""
    pl_opt12 = ""
    last_dir_old1 = ""
    last_dir_old2 = ""
    last_dir_old3 = ""
    last_dir_new1 = ""
    last_dir_new2 = ""
    last_dir_new3 = ""

    def pattern_three(self):
        while True:
            if player.last_direction is None:
                slow_print(self.msg1)
                direction_choice = base_options()
                if direction_choice == self.pl_opt1:
                    player.last_direction = self.last_dir_new1
                    break
                elif direction_choice == self.pl_opt2:
                    player.last_direction = self.last_dir_new2
                    break
                elif direction_choice == self.pl_opt3:
                    player.last_direction = self.last_dir_new3
                    break
                elif direction_choice != "skip":
                    wrong_input()

            elif player.last_direction == self.last_dir_old1:
                slow_print(self.msg2)
                direction_choice = base_options()
                if direction_choice == self.pl_opt4:
                    player.last_direction = self.last_dir_new1
                    break
                elif direction_choice == self.pl_opt5:
                    player.last_direction = self.last_dir_new2
                    break
                elif direction_choice == self.pl_opt6:
                    player.last_direction = self.last_dir_new3
                    break
                elif direction_choice != "skip":
                    wrong_input()

            elif player.last_direction == self.last_dir_old2:
                slow_print(self.msg3)
                direction_choice = base_options()
                if direction_choice == self.pl_opt7:
                    player.last_direction = self.last_dir_new2
                    break
                elif direction_choice == self.pl_opt8:
                    player.last_direction = self.last_dir_new1
                    break
                elif direction_choice == self.pl_opt9:
                    player.last_direction = self.last_dir_new3
                    break
                elif direction_choice != "skip":
                    wrong_input()

            elif player.last_direction == self.last_dir_old3:
                slow_print(self.msg4)
                direction_choice = base_options()
                if direction_choice == self.pl_opt10:
                    player.last_direction = self.last_dir_new3
                    break
                elif direction_choice == self.pl_opt11:
                    player.last_direction = self.last_dir_new2
                    break
                elif direction_choice == self.pl_opt12:
                    player.last_direction = self.last_dir_new1
                    break
                elif direction_choice != "skip":
                    wrong_input()

        return self.get_coordinates()


# room types
class RoomTypeN(RoomPatternOne):
    def type(self):
        self.basic_functions()

        self.old_dir = "South"
        self.new_dir = "North"

        self.pattern_one()


class RoomTypeE(RoomPatternOne):
    def type(self):
        self.basic_functions()

        self.old_dir = "West"
        self.new_dir = "East"

        self.pattern_one()


class RoomTypeS(RoomPatternOne):
    def type(self):
        self.basic_functions()

        self.old_dir = "North"
        self.new_dir = "South"

        self.pattern_one()


class RoomTypeW(RoomPatternOne):
    def type(self):
        self.basic_functions()

        self.old_dir = "East"
        self.new_dir = "West"

        self.pattern_one()


class RoomTypeNE(RoomPatternTwo):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, nebo v[p]ravo.\n"
        self.pl_opt1 = "r"
        self.last_dir_new1 = "North"
        self.pl_opt2 = "p"
        self.last_dir_new2 = "East"
        self.last_dir_old1 = "South"
        self.msg2 = "Můžete jít [z]pět, nebo v[l]evo.\n"
        self.pl_opt3 = "z"
        self.pl_opt4 = "l"
        self.last_dir_old2 = "West"
        self.msg3 = "Můžete jít [z]pět, nebo v[p]ravo.\n"
        self.pl_opt5 = "z"
        self.pl_opt6 = "p"

        self.pattern_two()


class RoomTypeNS(RoomPatternTwo):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, nebo v[z]ad.\n"
        self.pl_opt1 = "r"
        self.last_dir_new1 = "North"
        self.pl_opt2 = "z"
        self.last_dir_new2 = "South"
        self.last_dir_old1 = "South"
        self.msg2 = "Můžete jít [z]pět, nebo [r]ovně.\n"
        self.pl_opt3 = "z"
        self.pl_opt4 = "r"
        self.last_dir_old2 = "North"
        self.msg3 = "Můžete jít [z]pět, nebo [r]ovně.\n"
        self.pl_opt5 = "z"
        self.pl_opt6 = "r"

        self.pattern_two()

        return


class RoomTypeNW(RoomPatternTwo):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, nebo v[l]evo.\n"
        self.pl_opt1 = "r"
        self.last_dir_new1 = "North"
        self.pl_opt2 = "l"
        self.last_dir_new2 = "West"
        self.last_dir_old1 = "South"
        self.msg2 = "Můžete jít [z]pět, nebo v[p]ravo.\n"
        self.pl_opt3 = "z"
        self.pl_opt4 = "p"
        self.last_dir_old2 = "East"
        self.msg3 = "Můžete jít [z]pět, nebo v[l]evo.\n"
        self.pl_opt5 = "z"
        self.pl_opt6 = "l"

        self.pattern_two()

        return


class RoomTypeES(RoomPatternTwo):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, nebo v[p]ravo.\n"
        self.pl_opt1 = "r"
        self.last_dir_new1 = "East"
        self.pl_opt2 = "p"
        self.last_dir_new2 = "South"
        self.last_dir_old1 = "West"
        self.msg2 = "Můžete jít [z]pět, nebo v[l]evo.\n"
        self.pl_opt3 = "z"
        self.pl_opt4 = "l"
        self.last_dir_old2 = "North"
        self.msg3 = "Můžete jít [z]pět, nebo v[p]ravo.\n"
        self.pl_opt5 = "z"
        self.pl_opt6 = "p"

        self.pattern_two()

        return


class RoomTypeEW(RoomPatternTwo):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, nebo v[z]ad.\n"
        self.pl_opt1 = "r"
        self.last_dir_new1 = "East"
        self.pl_opt2 = "z"
        self.last_dir_new2 = "West"
        self.last_dir_old1 = "West"
        self.msg2 = "Můžete jít [z]pět, nebo [r]ovně.\n"
        self.pl_opt3 = "z"
        self.pl_opt4 = "r"
        self.last_dir_old2 = "East"
        self.msg3 = "Můžete jít [z]pět, nebo [r]ovně.\n"
        self.pl_opt5 = "z"
        self.pl_opt6 = "r"

        self.pattern_two()

        return


class RoomTypeSW(RoomPatternTwo):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, nebo v[p]ravo.\n"
        self.pl_opt1 = "r"
        self.last_dir_new1 = "South"
        self.pl_opt2 = "p"
        self.last_dir_new2 = "West"
        self.last_dir_old1 = "North"
        self.msg2 = "Můžete jít [z]pět, nebo v[l]evo.\n"
        self.pl_opt3 = "z"
        self.pl_opt4 = "l"
        self.last_dir_old2 = "East"
        self.msg3 = "Můžete jít [z]pět, nebo v[p]ravo.\n"
        self.pl_opt5 = "z"
        self.pl_opt6 = "p"

        self.pattern_two()

        return


class RoomTypeNES(RoomPatternThree):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n"
        self.pl_opt1 = "r"  # 1
        self.last_dir_new1 = "North"
        self.pl_opt2 = "p"  # 2
        self.last_dir_new2 = "East"
        self.pl_opt3 = "z"  # 3
        self.last_dir_new3 = "South"
        self.last_dir_old1 = "South"
        self.msg2 = "Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n"
        self.pl_opt4 = "z"  # 1
        self.pl_opt5 = "l"  # 2
        self.pl_opt6 = "r"  # 3
        self.last_dir_old2 = "West"
        self.msg3 = "Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n"
        self.pl_opt7 = "z"  # 2
        self.pl_opt8 = "p"  # 1
        self.pl_opt9 = "l"  # 3
        self.last_dir_old3 = "North"
        self.msg4 = "Můžete jít [z]pět, [r]ovně, nebo v[p]ravo.\n"
        self.pl_opt10 = "z"  # 3
        self.pl_opt11 = "p"  # 2
        self.pl_opt12 = "r"  # 1

        self.pattern_three()

        return


class RoomTypeNEW(RoomPatternThree):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, v[p]ravo, nebo v[l]evo.\n"
        self.pl_opt1 = "r"  # 1
        self.last_dir_new1 = "North"
        self.pl_opt2 = "p"  # 2
        self.last_dir_new2 = "East"
        self.pl_opt3 = "l"  # 3
        self.last_dir_new3 = "West"
        self.last_dir_old1 = "South"
        self.msg2 = "Můžete jít [z]pět, v[l]evo, nebo v[p]ravo.\n"
        self.pl_opt4 = "z"  # 1
        self.pl_opt5 = "l"  # 2
        self.pl_opt6 = "p"  # 3
        self.last_dir_old2 = "West"
        self.msg3 = "Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n"
        self.pl_opt7 = "z"  # 2
        self.pl_opt8 = "p"  # 1
        self.pl_opt9 = "r"  # 3
        self.last_dir_old3 = "East"
        self.msg4 = "Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n"
        self.pl_opt10 = "z"  # 3
        self.pl_opt11 = "r"  # 2
        self.pl_opt12 = "l"  # 1

        self.pattern_three()

        return


class RoomTypeNSW(RoomPatternThree):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, v[l]evo, nebo v[z]ad.\n"
        self.pl_opt1 = "r"  # 1
        self.last_dir_new1 = "North"
        self.pl_opt2 = "l"  # 2
        self.last_dir_new2 = "West"
        self.pl_opt3 = "z"  # 3
        self.last_dir_new3 = "South"
        self.last_dir_old1 = "South"
        self.msg2 = "Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n"
        self.pl_opt4 = "z"  # 1
        self.pl_opt5 = "p"  # 2
        self.pl_opt6 = "r"  # 3
        self.last_dir_old2 = "North"
        self.msg3 = "Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n"
        self.pl_opt7 = "l"  # 2
        self.pl_opt8 = "r"  # 1
        self.pl_opt9 = "z"  # 3
        self.last_dir_old3 = "East"
        self.msg4 = "Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n"
        self.pl_opt10 = "p"  # 3
        self.pl_opt11 = "z"  # 2
        self.pl_opt12 = "l"  # 1

        self.pattern_three()

        return


class RoomTypeESW(RoomPatternThree):
    def type(self):
        self.basic_functions()

        self.msg1 = "Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n"
        self.pl_opt1 = "r"  # 1
        self.last_dir_new1 = "East"
        self.pl_opt2 = "p"  # 2
        self.last_dir_new2 = "South"
        self.pl_opt3 = "z"  # 3
        self.last_dir_new3 = "West"
        self.last_dir_old1 = "West"
        self.msg2 = "Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n"
        self.pl_opt4 = "z"  # 1
        self.pl_opt5 = "l"  # 2
        self.pl_opt6 = "r"  # 3
        self.last_dir_old2 = "North"
        self.msg3 = "Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n"
        self.pl_opt7 = "z"  # 2
        self.pl_opt8 = "p"  # 1
        self.pl_opt9 = "l"  # 3
        self.last_dir_old3 = "East"
        self.msg4 = "Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n"
        self.pl_opt10 = "z"  # 3
        self.pl_opt11 = "p"  # 2
        self.pl_opt12 = "r"  # 1

        self.pattern_three()

        return


class RoomTypeNESW(Room):
    def type(self):
        self.basic_functions()

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
                    wrong_input()

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
                    wrong_input()

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
                    wrong_input()

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
                    wrong_input()

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
                    wrong_input()

        return self.get_coordinates()
