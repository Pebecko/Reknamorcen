from random import choice
from sys import stdout
from time import sleep
from os import system
from game.character_stats.player import player
from game.important_modules.settings import settings


def wrong_input():
    error_messages = ["Špatný vstup, zkuste to znovu.\n",
                      "Špatná možnost, zkuste to znovu.\n",
                      "Nekompatibilní vstup, zkuste to znovu.\n",
                      "To co jste zadali nesouhlasí s možnostmi.\n"]

    return slow_print(choice(error_messages))


def slow_print(s):
    for c in s:
        stdout.write(c)
        stdout.flush()
        sleep(settings.print_time)
    print()
    sleep(settings.print_break)


def shutdown():
    slow_print("SHUTTING DOWN...\n")
    sleep(0.8)
    quit()


def player_killed():
    sleep(0.6)
    slow_print("Jste mrtev.\n")
    sleep(0.8)

    return player_restarting_choice()


def player_restarting_choice():
    slow_print("Chcete [z]ačít znovu, nebo [o]dejít?")

    escape_result = input()

    if escape_result == "o":
        shutdown()
    elif escape_result == "z":
        print("not implemented")  # restarting the game
        quit()
    else:
        wrong_input()


# TODO - Split everything into separate functions
def base_options(*message):
    slow_print(message)
    option = input()

    if option == "quit" or option == "leave" or option == "exit" or option == "vypnout":
        shutdown()

    elif option == "save" or option == "uložit":
        option = "skip"
        saving()

    elif option == "time":
        option = "skip"
        changing_print_time()

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

    elif option == "pinfo":
        slow_print(str(player))

        option = "skip"

    elif option == "cinfo":
        slow_print("Užitečné příkazy:\n"
                   "    [time] - nastavení rychlosti vypisování\n"
                   "    [quit] - vypne hru\n"
                   "    [save] - uloží hru (není dostupné)\n"
                   "    [pinfo] - informace o hráči\n"
                   "    [oinfo] - informace o všech zbraních, helmách a brněních (není dostupné)\n"
                   "    [hpot] - použití léčivého lekvaru\n")

        option = "skip"

    elif option == "oinfo":
        while True:
            slow_print("Zajímá vás určitá [z]braň, [h]elma, nebo [b]rnění?\n")
            type_decision = input()
            if type_decision == "z":
                break
            elif type_decision == "h":
                break
            elif type_decision == "b":
                break
            else:
                wrong_input()

        option = "skip"

    elif option == "hpot":
        if player.health == player.max_health:
            slow_print("Jste úplně v pořádku a nepotřebujete léčení.\n")

        elif player.potions.health_potions > 0:
            if player.health + 260 <= player.max_health:
                player.health += 260
            else:
                player.health = player.max_health

            player.potions.health_potions -= 1
            slow_print("Váš život je: " + str(player.health))

            if player.potions.health_potions == 0:
                slow_print("Už nemáte žádné léčivé lektvary.\n")
            elif player.potions.health_potions == 1:
                slow_print("Zbývá vám poslední léčivý lektvar.\n")
            elif player.potions.health_potions in [2, 3, 4]:
                slow_print("Zbývají vám " + str(player.health_potions) + " léčivé lektvary.\n")
            else:
                slow_print("Zbývá vám " + str(player.health_potions) + " léčivých lektvarů.\n")

        else:
            slow_print("Už nemáte žádné léčivé lektvary.\n")

        option = "skip"

    return option


def saving():
    if player.x == 0 and player.y == 0:
        save = ""
        print("\nVáš save je: " + save)
    else:
        slow_print("Jste v místnosti v které nejde uložit hru.\n")


def changing_print_time():
    slow_print("Jak rychle chcete aby se text vypisoval:\n"
               "    [i]nstantně\n"
               "    [r]ychle\n"
               "    [p]omalu")
    while True:
        time_setting = input()
        if time_setting is "i":
            settings.print_time = 0
            break
        elif time_setting is "r":
            settings.print_time = 0.005
            break
        elif time_setting is "p":
            settings.print_time = 0.015
            break
        else:
            wrong_input()


def clearing_screen():
    system("cls")
