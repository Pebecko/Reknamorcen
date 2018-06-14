import random
import time
import sys

def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    print("")

def shutdown():
    time.sleep(2)
    slow_print("Jste mrtev.\n")
    time.sleep(1)
    slow_print("SHUTTING DOWN...\n")
    time.sleep(2)
    quit()

def rolling_dice():
    dice_roll = random.randint(1,6)
    slow_print(str(dice_roll))
        
    for dice_roll !=6:
        if dice_roll == 6:
            return 1

        elif dice_roll >= 1 and dice_roll <=5:
            slow_print("\"Smůla, teď zemřeš.\" ")#Vytáhne nůž a podřízne vám hrdlo.\n")

slow_print("Jste v temné místnosti a můžete hýbat jen pravou rukou, před vámi sedí osoba s nataženou rukou podávající vám hrací kostku a říkající: \"Hoď si, když ti padne 1 až 5, tak zemřeš.\"\n")
roll_six = 0
elf_new_dialogue = 0

while True:
    slow_print("Můžete se osoby [z]eptat, co se stane pokud padne 6, [h]odit kostkou, nebo č[e]kat, co se stane.\n")
    elf_dice_game = input()
    
    if elf_dice_game == "z":
        slow_print("Když ti padne šestka, tak házíš znovu.\n")
        elf_new_dialogue = 1
        break
    
    elif elf_dice_game == "h":
        roll_six += rolling_dice()
        elf_new_dialogue = 1
        break

    elif elf_dice_game == "e":
        time.sleep(3)
        slow_print("\"Tohle už mě nebaví.\" Osoba před vámi vytáhne nůž a probodne vás.\n")
        shutdown()
    
    elif elf_dice_game == "pass":
        slow_print("Přeskakování hry s kostkou...")
        time.sleep(2)
        break

    else:
        slow_print("Vyberte jednu z možností.\n")

while elf_new_dialogue == 1:
    if roll_six == 2:
        slow_print("\"Máš štěstí,\"povídá osoba,\"nechám tě jít.\"Odemyká vám pouta a odchází.")
        time.sleep(0.5)
        slow_print("(Jestli se sem příště chcete dostat bez hry s kostkou, zadejte \'pass\')\n")
        break
#        slow_print("\"Házíš znovu.\n\"")
    slow_print("Můžete [h]odit kostkou, nebo č[e]kat.")
    elf_dice_game_2 = input()
    if elf_dice_game_2 == "h":
        roll_six += rolling_dice()
    
    elif elf_dice_game_2 == "e":
        time.sleep(3)
        slow_print("\"Tohle už mě nebaví.\" Osoba před vámi vytáhne nůž a probodne vás.\n")
        shutdown()

    elif elf_dice_game_2 == "pass":
        slow_print("Přeskakování hry s kostkou...")
        time.sleep(2)
        break

    else:
        slow_print("Vyberte jednu z možností.")

slow_print("Pro odchod ze hry zmáčkněte enter.")
input()
