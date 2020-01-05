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
    time.sleep(0.8)
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
        print("no implemented")  # restarting the game
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

    elif option == "pinfo":
        while True:
            slow_print("Co byste chtěli vědět:\n"
                       "    kolik máte [ž]ivotů\n"
                       "    co máte za [p]ostavu\n"
                       "    jakou máte [z]braň\n"
                       "    jakou máte [h]elmu\n"
                       "    jaké máte [b]rnění\n"
                       "    kolik máte [l]éčivých lektvarů\n")
            info_option = input()

            if info_option == "ž":
                slow_print("Vaše zdraví je: " + str(player.health) + "/" + str(player.max_health) + "\n")
                break
            elif info_option == "p":
                slow_print("Vaše postava je {}, {}.".format(player.name, player.info))
                break
            elif info_option == "z":
                if player.weapon.weapon_class != "unarmed":
                    slow_print("Vaše zbraň je {}, {}.\n".format(player.weapon.name, player.weapon.info))
                else:
                    slow_print("Nemáte u sebe žádnou zbraň\n")
                break
            elif info_option == "h":
                if player.helmet.name != "":
                    slow_print("Vaše helma je {}, {}.\n".format(player.helmet.name, player.helmet.info))
                else:
                    slow_print("Nemáte žádnou helmu.\n")
                break
            elif info_option == "b":
                if player.armor.name != "":
                    slow_print("Vaše brnění je {}, {}.\n".format(player.armor.name, player.armor.info))
                else:
                    slow_print("Nemáte žádné brnění.\n")
                break
            elif info_option == "l":
                if player.health_potions == 0:
                    slow_print("Nemáte žádné léčivé lektvary.\n")
                elif player.health_potions == 1:
                    slow_print("Máte slední léčivý lektvar.\n")
                elif player.health_potions in [2, 3, 4]:
                    slow_print("Máte " + str(player.health_potions) + " léčivé lektvary.\n")
                else:
                    slow_print("Máte " + str(player.health_potions) + " léčivých lektvarů.\n")
                break
            else:
                wrong_input(0)

        option = "skip"

    elif option == "cinfo":
        slow_print("Užitečné příkazy:\n"
                   "    [time] - nastavení rychlosti vypisování\n"
                   "    [quit] - vypne hru\n"
                   "    [save] - uloží hru (není dostupné)\n"
                   "    [pinfo] - informace o hráči\n"
                   "    [oinfo] - informace o všech zbraních, helmách a brněních\n"
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
                wrong_input(0)

        option = "skip"

    elif option == "hpot":
        if player.health == player.max_health:
            slow_print("Jste úplně v pořádku a nepotřebujete léčení.\n")

        elif player.health_potions > 0:
            if player.health + 260 <= player.max_health:
                player.health += 260
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
