import time
import sys


def wrong_input(call):
    if call == r:
        call = random.randint(1)

    if call is 1:
        error_call = "Špatný vstup, zkuste to znovu.\n"
    else:
        error_call = "Špatný error call"
    return error_call


def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    print("")
    time.sleep(0.08)


class Travelling:
    def __init__(self, x, y, last_direction, last_health, healing_potion_count):
        self.x = x
        self.y = y
        self.last_direction = last_direction
        self.last_health = last_health
        self.healing_potion_count = healing_potion_count

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
                slow_print("Právě odcházíte.")
                time.sleep(2)
                quit()
            elif self.x == 3 and self.y == 2:
                self.room_two()
            elif self.x == 3 and self.y == 3:
                self.room_one_spawn_one()

    def get_coordinates(self) -> object:
        if self.last_direction is "North":
            self.y -= 1
        elif self.last_direction is "East":
            self.x += 1
        elif self.last_direction is "South":
            self.y += 1
        elif self.last_direction is "West":
            self.x -= 1
        return

    def room_type_n(self):
        if self.last_direction is None:
            slow_print("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")

        elif self.last_direction is "South":
            slow_print("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")

        input()

        self.last_direction = "North"

        self.get_coordinates()

        return

    def room_type_e(self):
        if self.last_direction is None:
            slow_print("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        elif self.last_direction is "West":
            slow_print("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")

        input()

        self.last_direction = "East"

        self.get_coordinates()

        return

    def room_type_s(self):
        if self.last_direction is None:
            slow_print("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")

        elif self.last_direction is "North":
            slow_print("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")

        input()

        self.last_direction = "South"

        self.get_coordinates()

        return

    def room_type_w(self):
        if self.last_direction is None:
            slow_print("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")

        elif self.last_direction is "East":
            slow_print("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")

        input()

        self.last_direction = "East"

        self.get_coordinates()

        return

    def room_type_ne(self):
        if self.last_direction is None:
            slow_print("Můžete jít [r]ovně, nebo v[p]ravo.\n")
            direction_choice = input()
            if direction_choice is "r":
                self.last_direction = "North"

            elif direction_choice is "p":
                self.last_direction = "East"

        elif self.last_direction is "South":
            slow_print("Můžete jít [z]pět, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "North"

            elif direction_choice is "l":
                self.last_direction = "East"

        elif self.last_direction is "West":
            slow_print("Můžete jít [z]pět, nebo v[p]ravo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "East"

            elif direction_choice is "p":
                self.last_direction = "North"

            self.get_coordinates()

        return

    def room_type_ns(self):
        if self.last_direction is None:
            slow_print("Můžete jít [r]ovně, nebo v[z]ad.\n")
            direction_choice = input()
            if direction_choice is "r":
                self.last_direction = "North"

            elif direction_choice is "z":
                self.last_direction = "South"

        elif self.last_direction is "South":
            slow_print("Můžete jít [z]pět, nebo [r]ovně.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "North"

            elif direction_choice is "r":
                self.last_direction = "South"

        elif self.last_direction is "North":
            slow_print("Můžete jít [z]pět, nebo [r]ovně.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "South"

            elif direction_choice is "r":
                self.last_direction = "North"

            self.get_coordinates()

        return

    def room_type_nw(self):
        if self.last_direction is None:
            while True:
                slow_print("Můžete jít [r]ovně, nebo v[l]evo.\n")
                direction_choice = input()
                if direction_choice is "r":
                    self.last_direction = "North"
                    break
                elif direction_choice is "l":
                    self.last_direction = "West"
                    break
                else:
                    slow_print(wrong_input(r))

        elif self.last_direction is "South":
            slow_print("Můžete jít [z]pět, nebo v[p]ravo.\n")
            direction_choice = input()
            while True:
                if direction_choice is "z":
                    self.last_direction = "North"
                    break
                elif direction_choice is "p":
                    self.last_direction = "West"
                    break
                else:
                    slow_print(wrong_input(r))

        elif self.last_direction is "East":
            slow_print("Můžete jít [z]pět, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "West"

            elif direction_choice is "l":
                self.last_direction = "North"

            self.get_coordinates()

        return

    def room_type_es(self):
        if self.last_direction is None:
            slow_print("Můžete jít [r]ovně, nebo v[p]ravo.\n")
            direction_choice = input()
            if direction_choice is "r":
                self.last_direction = "East"

            elif direction_choice is "p":
                self.last_direction = "South"

        elif self.last_direction is "North":
            slow_print("Můžete jít [z]pět, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "South"

            elif direction_choice is "l":
                self.last_direction = "East"

        elif self.last_direction is "West":
            slow_print("Můžete jít [z]pět, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "East"

            elif direction_choice is "l":
                self.last_direction = "South"

        self.get_coordinates()

        return

    def room_type_ew(self):
        if self.last_direction is None:
            slow_print("Můžete jít [r]ovně, nebo v[z]ad.\n")
            direction_choice = input()
            if direction_choice is "r":
                self.last_direction = "East"

            elif direction_choice is "z":
                self.last_direction = "West"

        elif self.last_direction is "East":
            slow_print("Můžete jít [z]pět, nebo [r]ovně.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "West"

            elif direction_choice is "r":
                self.last_direction = "East"

        elif self.last_direction is "West":
            slow_print("Můžete jít [z]pět, nebo [r]ovně.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "East"

            elif direction_choice is "r":
                self.last_direction = "West"

        self.get_coordinates()

        return

    def room_type_sw(self):
        if self.last_direction is None:
            slow_print("Můžete jít [r]ovně, nebo v[p]ravo.\n")
            direction_choice = input()
            if direction_choice is "r":
                self.last_direction = "South"

            elif direction_choice is "p":
                self.last_direction = "West"

        elif self.last_direction is "North":
            slow_print("Můžete jít [z]pět, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "South"

            elif direction_choice is "l":
                self.last_direction = "West"

        elif self.last_direction is "East":
            slow_print("Můžete jít [z]pět, nebo v[p]ravo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "West"

            elif direction_choice is "p":
                self.last_direction = "South"

        self.get_coordinates()

        return

    def room_type_nes(self):
        if self.last_direction is None:
            slow_print("Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n")
            direction_choice = input()
            if direction_choice is "r":
                self.last_direction = "North"

            elif direction_choice is "p":
                self.last_direction = "East"

            elif direction_choice is "z":
                self.last_direction = "South"

        elif self.last_direction is "South":
            slow_print("Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "North"

            elif direction_choice is "l":
                self.last_direction = "East"

            elif direction_choice is "r":
                self.last_direction = "South"

        elif self.last_direction is "West":
            slow_print("Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "East"

            elif direction_choice is "p":
                self.last_direction = "North"

            elif direction_choice is "l":
                self.last_direction = "South"

        elif self.last_direction is "North":
            slow_print("Můžete jít [z]pět, [r]ovně, nebo v[p]ravo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "South"

            elif direction_choice is "r":
                self.last_direction = "North"

            elif direction_choice is "p":
                self.last_direction = "East"

        self.get_coordinates()

        return

    def room_type_new(self):
        if self.last_direction is None:
            slow_print("Můžete jít [r]ovně, v[p]ravo, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "r":
                self.last_direction = "North"

            elif direction_choice is "p":
                self.last_direction = "East"

            elif direction_choice is "l":
                self.last_direction = "West"

        elif self.last_direction is "South":
            slow_print("Můžete jít [z]pět, v[l]evo, nebo v[p]ravo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "North"

            elif direction_choice is "l":
                self.last_direction = "East"

            elif direction_choice is "p":
                self.last_direction = "West"

        elif self.last_direction is "West":
            slow_print("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "East"

            elif direction_choice is "p":
                self.last_direction = "North"

            elif direction_choice is "r":
                self.last_direction = "West"

        elif self.last_direction is "East":
            slow_print("Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "West"

            elif direction_choice is "r":
                self.last_direction = "East"

            elif direction_choice is "l":
                self.last_direction = "North"

        self.get_coordinates()

        return

    def room_type_nsw(self):
        if self.last_direction is None:
            slow_print("Můžete jít [r]ovně, v[l]evo, nebo v[z]ad.\n")
            direction_choice = input()
            if direction_choice is "r":
                self.last_direction = "North"

            elif direction_choice is "l":
                self.last_direction = "West"

            elif direction_choice is "z":
                self.last_direction = "South"

        elif self.last_direction is "South":
            slow_print("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "North"

            elif direction_choice is "p":
                self.last_direction = "West"

            elif direction_choice is "r":
                self.last_direction = "South"

        elif self.last_direction is "East":
            slow_print("Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "West"

            elif direction_choice is "l":
                self.last_direction = "North"

            elif direction_choice is "p":
                self.last_direction = "South"

        elif self.last_direction is "North":
            slow_print("Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "South"

            elif direction_choice is "r":
                self.last_direction = "North"

            elif direction_choice is "l":
                self.last_direction = "West"

        self.get_coordinates()

        return

    def room_type_esw(self):
        if self.last_direction is None:
            slow_print("Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n")
            direction_choice = input()
            if direction_choice is "r":
                self.last_direction = "East"

            elif direction_choice is "p":
                self.last_direction = "South"

            elif direction_choice is "z":
                self.last_direction = "West"

        elif self.last_direction is "West":
            slow_print("Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "East"

            elif direction_choice is "l":
                self.last_direction = "South"

            elif direction_choice is "r":
                self.last_direction = "West"

        elif self.last_direction is "East":
            slow_print("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "West"

            elif direction_choice is "r":
                self.last_direction = "East"

            elif direction_choice is "p":
                self.last_direction = "South"

        elif self.last_direction is "North":
            slow_print("Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n")
            direction_choice = input()
            if direction_choice is "z":
                self.last_direction = "South"

            elif direction_choice is "r":
                self.last_direction = "North"

            elif direction_choice is "l":
                self.last_direction = "West"

        self.get_coordinates()

        return

    def room_type_nesw(self):
        pass

        self.get_coordinates()

        return

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


path = Travelling(0, 2, None, 1, 0)
print(path.room_picking())

input()
