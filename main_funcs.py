import random
import sys
import time
import character_stats


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
    writing_time = 0.015
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


def base_options():
    option = input()

    if option is "quit" or option is "leave" or option is "exit" or option is "vypnout":
        shutdown()

    elif option is "save" or option is "uložit":
        option = "skip"
        if player.x == 0 and player.y == 0:
            save = ""
            print("\nVáš save je: " + save)
        else:
            slow_print("Jste v místnosti v které nejde uložit hru.\n")

        time.sleep(1)
        slow_print("Vyberte prosím další možnost.\n")

    return option

