import random
import sys
import time
from character_stats import player


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
    writing_time = player.print_time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(writing_time)
    print("")
    time.sleep(0.1)


def shutdown():
    slow_print("SHUTTING DOWN...\n")
    time.sleep(0.4)
    quit()


def player_killed():
    time.sleep(0.6)
    slow_print("Jste mrtev.\n")
    time.sleep(0.8)
    slow_print("Chcete [z]ačít znovu, nebo [o]dejít?")
    escape_result = input()
    if escape_result == "o":
        shutdown()
    elif escape_result == "z":
        print("start")  # restarting the game
    else:
        wrong_input(0)


def base_options(*message):
    slow_print(message)
    option = input()

    if option == "quit" or option == "leave" or option == "exit" or option == "vypnout":
        shutdown()

    elif option == "save" or option == "uložit":
        option = "skip"
        if player.x == 0 and player.y == 0:
            save = ""
            print("\nVáš save je: " + save)
        else:
            slow_print("Jste v místnosti v které nejde uložit hru.\n")

    elif option == "time":
        option = "skip"
        slow_print("Jak rychle chcete aby se text vypisoval:\n"
                   "    [i]nstantně\n"
                   "    [r]ychle\n"
                   "    [p]omalu")
        while True:
            time_setting = input()
            if time_setting is "i":
                player.print_time = 0
                break
            elif time_setting is "r":
                player.print_time = 0.005
                break
            elif time_setting is "p":
                player.print_time = 0.015
                break
            else:
                wrong_input(3)

    elif option == "cman":
        player.max_health = 10000
        player.health = 10000

        option = "skip"

    elif option == "wari":
        print(player.weapon.hit_points, "player weapon hit points\n", player.helmet.hit_points, player.armor.hit_points,
              "player helmet and armor hit points\n\n")

        option = "skip"

    elif option == "tmon":
        player.test = True

        option = "skip"

    elif option == "tmof":
        player.test = False

        option = "skip"

    elif option == "hp":
        slow_print("Vaše zdraví je: " + str(player.health) + "/" + str(player.max_health) + "\n")

        option = "skip"

    elif option == "hpot":
        if player.health == player.max_health:
            slow_print("Jste úplně v pořádku a nepotřebujete léčení.\n")

        elif player.health_potions > 0:
            if player.health + 200 <= player.max_health:
                player.health += 200
            else:
                player.health = player.max_health

            player.health_potions -= 1
            slow_print("Váš život je: " + str(player.health))

            if player.health_potions == 0:
                slow_print("Už nemáte žádné léčivé lektvary.\n")
            elif player.health_potions == 1:
                slow_print("Zbývá vám poslední léčivý lektvar.\n")
            elif player.health_potions in [2, 3, 4]:
                slow_print("Zbývají vám " + str(player.health_potions) + " léčivé lektvary.\n")
            else:
                slow_print("Zbývá vám " + str(player.health_potions) + " léčivých lektvarů.\n")

        else:
            slow_print("Už nemáte žádné léčivé lektvary.\n")

        option = "skip"

    return option
