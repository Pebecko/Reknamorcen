import random
import time
import sys

#funkce
def slowPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    print("")
    time.sleep(0.02)

def attack():
    opponent_defence = random.randint(1,3)
    while True:
        slowPrint("Chcete útočit na [b]řicho, [h]lavu, nebo na b[o]k\n")
        attack = input("\n")
        if ((attack == "b") and (opponent_defence == 1)) or ((attack == "h") and (opponent_defence == 2)) or ((attack == "o") and (opponent_defence == 3)):
            return 1
        elif ((attack == "b") and (opponent_defence != 1)) or ((attack == "h") and (opponent_defence != 2)) or ((attack == "o") and (opponent_defence != 3)):
            return 2
        else:
            slowPrint("Neplatná možnost.\n")

def defence():
    opponent_attack = random.randint(1,3)
    while True:
        slowPrint("Myslíte, že soupeř zaútočí na [b]řicho, [h]lavu, nebo na b[o]k?\n")
        defence = input("\n")
        if ((defence == "b") and (opponent_attack == 1)) or ((defence == "h") and (opponent_attack == 2)) or ((defence == "o") and (opponent_attack == 3)):
            return 1
        elif ((defence == "b") and (opponent_attack != 1)) or ((defence == "h") and (opponent_attack != 2)) or ((defence == "o") and (opponent_attack != 3)):
            return 2
        else:
            slowPrint("Neplatná možnost.\n")

def shutdown():
    time.sleep(1)
    slowPrint("Jste mrtev.\n")
    time.sleep(2)
    slowPrint("SHUTTING DOWN...\n")
    time.sleep(1)
    quit()

def rolling_dice():
    dice_roll = random.randint(1,6)
    slowPrint(str(dice_roll))
        
    if dice_roll == 6:
        return 1

    elif dice_roll >= 1 and dice_roll <=5:
        slowPrint("\"Smůla, teď zemřeš.\" Vytáhne nůž a podřízne vám hrdlo.\n")
        shutdown()

def fight():
    slowPrint("Potkali jste nepřítele, musíte se mu postavit.\n")
    #enemy generation
    zivot_s = random.randint(16,24)
    max_zivot_s = zivot_s
    sila_s = random.randint(4,8)
    mrstnost_s = random.randint(6,12)
    zakl_mrstn_s = mrstnost_s
    zist_mrstnosti_s = random.randint(1,2)
    mrstnost = zakl_mrstn
    zivot = last_zivot

    while True:
        #fight status
        time.sleep(0.5)
        slowPrint("    Váš život: " + str(zivot) + "/" + str(last_zivot))
        slowPrint("    Vaše energie: " + str(mrstnost) + "/" + str(zakl_mrstn) + "\n")
        time.sleep(0.5)
        slowPrint("    Soupeřův život: " + str(zivot_s) + "/" + str(max_zivot_s))
        slowPrint("    Soupeřova energie: " + str(mrstnost_s) + "/" + str(zakl_mrstn_s) + "\n")
        time.sleep(0.25)
        
        #nabídka akcí útok a obrana = dostatek energie
        if (mrstnost >= 4) and (mrstnost_s >= 4):
            while True:
                slowPrint("Chcete ú[t]očit, nebo se [b]ránit?\n")
                nab_akc = input("\n")
                
                #útok
                if nab_akc == "t":
                    mrstnost -= 4
                    attack_consequences = attack()
                    
                    if attack_consequences == 1:
                        slowPrint("Soupeři se povedlo úspěšně zablokovat váš útok a odseknout.\n")
                        if mrstnost_s>=2:
                            mrstnost_s -= 1
                            zivot -= (sila_s//2)
                        else:
                            zivot_s -= 1

                    elif attack_consequences == 2:
                        if mrstnost_s>=3:
                            mrstnost_s -= 3
                            zivot_s -= (int(sila//2))
                            slowPrint("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                        else:
                            zivot_s -= sila
                            slowPrint("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")
                    
                    last_fight_action = "attack"
                
                #obrana
                elif nab_akc == "b":
                    mrstnost_s -= 4
                    defence_consequences = defence()

                    if defence_consequences == 1:
                        if mrstnost >= 2:
                            slowPrint("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                            mrstnost -= 1
                            zivot_s -= (sila//2)
                        
                        else:
                            slowPrint("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                            zivot -= 1

                    elif defence_consequences == 2:
                        if mrstnost >= 3:
                            slowPrint("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.\n")
                            mrstnost -= 3
                            zivot -= (int(sila_s//2))
                        
                        else:
                            slowPrint("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou.\n ")
                            zivot -= sila

                    last_fight_action = "defence"

                #wrong input
                else:
                    slowPrint("Neplatná volba, zkuste to znovu.\n")
                break

        #soupeř nemá dost síly na útok ale hráč ano
        elif (mrstnost >= 4) and (mrstnost_s < 4):
            while True:
                slowPrint("Chcete ú[t]očit, nebo č[e]kat a doplňovat síly.\n")
                nab_akc = input()
                    
                #útok
                if nab_akc == "t":
                    mrstnost -= 4
                    attack_consequences = attack()
                    
                    if attack_consequences == 1:
                        slowPrint("Soupeři se povedlo úspěšně zablokovat váš útok a odseknout.\n")
                        if mrstnost_s>=2:
                            mrstnost_s -= 1
                            zivot -= (sila_s//2)
                        else:
                            zivot_s -= 1

                    elif attack_consequences == 2:
                        if mrstnost_s>=3:
                            mrstnost_s -= 3
                            zivot_s -= (int(sila//2))
                            slowPrint("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                        else:
                            zivot_s -= sila
                            slowPrint("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")
                    
                    last_fight_action = "attack"

                #vyčkávání
                elif nab_akc == "e":
                    slowPrint("Chvíli oba se soupeřem čekáte a doplňujete energii.")
                break

        #nucená obrana = není dost energie na útok        
        elif (mrstnost < 4) and (mrstnost_s >= 4):
            slowPrint("Nemáte dost energie na útok, musíte se bránit.\n")
            mrstnost_s -= 4
            defence_consequences = defence()

            if defence_consequences == 1:
                if mrstnost >= 2:
                    slowPrint("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                    mrstnost -= 1
                    zivot_s -= (sila//2)
                        
                else:
                    slowPrint("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                    zivot -= 1

            elif defence_consequences == 2:
                if mrstnost >= 3:
                    slowPrint("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.\n")
                    mrstnost -= 3
                    zivot -= (int(sila_s//2))
                        
                else:
                    slowPrint("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou.\n ")
                    zivot -= sila

            last_fight_action = "defence"

        elif (mrstnost < 4) and (mrstnost_s) < 4:
            slowPrint("Oba chvíli stojíte a čerpáte energii, protože ani jeden nemáte sílu na útok.\n")
            
        #doplňování energie hráče
        if (mrstnost + int(zisk_mrstnosti)) < zakl_mrstn:
            mrstnost += zisk_mrstnosti
        
        #doplňování energie soupeře
        if (mrstnost_s + zist_mrstnosti_s) < zakl_mrstn_s:
            mrstnost_s += zist_mrstnosti_s
        
        
        if zivot_s <= 0:
            slowPrint("Podařilo se vám porazit soupeře.\n")
            return zivot
        
        elif zivot <= 0:
            shutdown()
        

#výběr postavy
while True:
    slowPrint("Vyberte si postavu: \n   [t]rpaslík\n  č[l]ověk\n   [e]lf\n")
    vyber_postavy = input()
    if vyber_postavy=="t":
        slowPrint("Jste trpaslík, jste velmi silný a vydržíte toho hodně, ale nejste moc mrštný.\n")
        max_zivot = 24
        last_zivot = 24
        zivot = 24
        sila = 10
        zakl_mrstn = 8
        mrstnost = 8
        zisk_mrstnosti = 1.5
        break
    elif vyber_postavy=="l":
        slowPrint("Jste člověk")
        max_zivot = 20
        last_zivot = 20
        zivot = 20
        sila = 8
        zakl_mrstn = 10
        mrstnost = 10
        zisk_mrstnosti = 2
        break
    elif vyber_postavy=="e":
        slowPrint("Jste elf")
        max_zivot = 18
        last_zivot = 18
        zivot = 18
        sila = 6
        zakl_mrstn = 12
        mrstnost = 12
        zisk_mrstnosti = 2.5
        break
    else:
        slowPrint("Nekompatibilní vstup, zkuste to znovu.\n")

last_zivot = fight()
last_zivot = fight()

slowPrint("Pro odchod ze hry zmáčkněte enter.")
input()
