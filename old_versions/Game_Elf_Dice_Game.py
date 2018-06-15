import random
import time
import sys

def slowPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    print("")
    time.sleep(0.02)

def shutdown():
    time.sleep(1)
    slowPrint("Jste mrtev.\n")
    time.sleep(2)
    slowPrint("SHUTTING DOWN...\n")
    time.sleep(1)
    quit()

def rolling_dice():
    dice_roll = random.randint(1,7)
        
    if dice_roll >= 6:
        slowPrint("Padla 6")
#        slowPrint("\"Ty máš ale štěstí!\"\n")
        return 1

    elif dice_roll >= 1 and dice_roll <=5:
        slowPrint("Padla " + str(dice_roll))
        slowPrint("\"Smůla, házíš znovu.\"\n")
        return 0

slowPrint("Jste v temné místnosti a můžete hýbat jen pravou rukou, před vámi sedí osoba s nataženou rukou podávající vám hrací kostku a říkající: \"Hoď si, když ti nepadne třikrát z 12 hodů 6, tak zemřeš.\"\n")
roll_six = 0
diceRolled = 0


while True:
    if roll_six == 3:
        slowPrint("\"Máš štěstí,\"povídá osoba,\"nechám tě jít.\"Odemyká vám pouta a odchází.")
        time.sleep(0.5)
        slowPrint("(Jestli se sem příště chcete dostat bez hry s kostkou, zadejte \'pass\')\n")
        break

    if diceRolled == 12:
        slowPrint("\"To by stačilo,\" osoba před vámi vytáhne nůž a probodne vás.\n")
        shutdown()
    
    slowPrint("Můžete [h]odit kostkou, nebo č[e]kat.")
    elf_dice_game = input()
    
    if elf_dice_game == "h":
        roll_six += rolling_dice()
        diceRolled +=1

    elif elf_dice_game == "e":
        time.sleep(2.5)
        slowPrint("\"Tohle už mě nebaví.\" Osoba před vámi vytáhne nůž a probodne vás.\n")
        shutdown()

    elif elf_dice_game == "pass":
        slowPrint("Přeskakování hry s kostkou...")
        time.sleep(1.25)
        break

    else:
        slowPrint("Vyberte jednu z možností.")

slowPrint("Pro odchod ze hry zmáčkněte enter.")
input()