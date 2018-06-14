import random
import time
import sys

#funkce
def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    print("")

def shutdown():
    time.sleep(2)
    slow_print("Jste mrtev.\n")
    time.sleep(4)
    slow_print("SHUTTING DOWN...\n")
    time.sleep(2)
    quit()

def rolling_dice():
    dice_roll = random.randint(1,6)
    slow_print(str(dice_roll))
        
    if dice_roll == 6:
        return 1

    elif dice_roll >= 1 and dice_roll <=5:
        slow_print("\"Smůla, teď zemřeš.\" Vytáhne nůž a podřízne vám hrdlo.\n")
        shutdown()

def fight():
    slow_print("Potkali jste nepřítele, musíte se mu postavit.\n")
    zivot_s = random.randint(10,20)
    max_zivot_s = zivot_s
    sila_s = random.randint(3,6)
    mrstnost_s = random.randint(6,12)
    zakl_mrstn_s = mrstnost_s
    zist_mrstnosti_s = random.randint(1,2)
    mrstnost = zakl_mrstn
    zivot = last_zivot
    max_zivot = zivot
    while True:
        
        #obeznámení uživatele s aktuálním stavem
        slow_print("Váš život: " + str(zivot) + "/" + str(max_zivot))
        slow_print("Vaše energie: " + str(zakl_mrstn) + "/" + str(mrstnost) + "\n")
        slow_print("Soupeřův život: " + str(max_zivot_s) + "/" + str(zivot_s))
        slow_print("Soupeřova energie: " + str(zakl_mrstn_s) + "/" + str(mrstnost_s) + "\n")
        
        #nabídka akcí útok a obrana = dostatek energie
        while mrstnost >= 4:
                slow_print("Chcete ú[t]očit, nebo se [b]ránit?\n")
                nab_akc = input()
                
                #útok
                if nab_akc == "t":
                    mrstnost -= 4
                    s_obrana = random.randint(1,3)
                    while True:
                        slow_print("Chcete útočit na [b]řicho, [h]lavu, nebo na b[o]k\n")
                        utok = input()
                        
                        #utok na břicho
                        if utok == "b":
                            if s_obrana == 1:
                                slow_print("Soupeři se povedlo úspěšně zablokovat váš útok a odseknout.\n")
                                if mrstnost_s>=1:
                                    mrstnost_s -= 1
                                    zivot -= (sila_s//2)
                                else:
                                    zivot_s -= 1
                            else:
                                if mrstnost_s>=3:
                                    mrstnost_s -= 3
                                    zivot_s -= (int(sila//2))
                                    slow_print("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                                else:
                                    zivot_s -= sila
                                    slow_print("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")  
                            break
                        
                        #útok na hlavu
                        elif utok == "h":
                            if s_obrana == 2:
                                slow_print("Soupeři se povedlo úspěšně zablokovat váš útok a odseknout.\n")
                                if mrstnost_s >=1:
                                    mrstnost_s -= 1
                                    zivot -= (sila_s//2)
                                else:
                                    zivot_s -= 1
                            else:
                                if mrstnost_s>=3:
                                    mrstnost_s -= 3
                                    zivot_s -= (int(sila//2))
                                    slow_print("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                                else:
                                    zivot_s -= sila
                                    slow_print("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")
                            break    
                        
                        #útok na bok
                        elif utok == "o":
                            if s_obrana == 3:
                                slow_print("Soupeři se povedlo úspěšně zablokovat váš útok a odseknout.\n")
                                if mrstnost_s >=1:
                                    mrstnost_s -= 1
                                    zivot -= (sila_s//2)
                                else:
                                    zivot_s -= 1
                            else:
                                if mrstnost_s>=3:
                                    mrstnost_s -= 3
                                    zivot_s -= (int(sila//2))
                                    slow_print("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                                else:
                                    zivot_s -= sila
                                    slow_print("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")
                            break
                        
                        #wrong input
                        else:
                            slow_print("Neplatná možnost.\n")
                    break
                
                #obrana
                elif nab_akc == "b":
                    s_utok = random.randint(1,3)
                    while True:
                        slow_print("Myslíte, že soupeř zaútočí na [b]řicho, [h]lavu, nebo na b[o]k?\n")
                        obrana = input()
                        
                        #obrana břicha
                        if obrana == "b":
                            if s_utok == 1:
                                if mrstnost >= 1:
                                    slow_print("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                                    mrstnost -= 1
                                    zivot_s -= (sila//2)
                                else:
                                    slow_print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                                    zivot -= 1
                            else:
                                if mrstnost >= 3:
                                    slow_print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                                    mrstnost -= 3
                                    zivot -= (int(sila_s//2))
                                else:
                                    slow_print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                                    zivot -= sila
                            break
                        
                        #obrana hlavy
                        elif obrana == "h":
                            if s_utok == 2:
                                if mrstnost >= 1:
                                    slow_print("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                                    mrstnost -= 1
                                    zivot_s -= (sila//2)
                                else:
                                    slow_print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                                    zivot -= 1
                            else:
                                if mrstnost >= 3:
                                    slow_print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                                    mrstnost -= 3
                                    zivot -= (int(sila_s//2))
                                else:
                                    slow_print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                                    zivot -= sila
                            break
                        
                        #obrana boku
                        elif obrana == "o":
                            if s_utok == 3:
                                if mrstnost >= 1:
                                    slow_print("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                                    mrstnost -= 1
                                    zivot_s -= (sila//2)
                                else:
                                    slow_print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                                    zivot -= 1
                            else:
                                if mrstnost >= 3:
                                    slow_print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                                    mrstnost -= 3
                                    zivot -= (int(sila_s//2))
                                else:
                                    slow_print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                                    zivot -= sila
                            break
                        else:
                            slow_print("Špatný vstup, zkuste to znovu.\n")
                    break
                
                #wrong input
                else:
                    slow_print("Neplatná volba, zkuste to znovu.\n")
        
        #nucená obrana = není dost energie na útok
        if mrstnost < 4 and mrstnost_s >= 4:
            slow_print("Nemáte dost energie na útok, musíte se bránit.\n")
            s_utok = random.randint(1,3)
            mrstnost_s -= 4
            while True:
                slow_print("Myslíte, že soupeř zaútočí na [b]řicho, [h]lavu, nebo na b[o]k?\n")
                obrana = input()
                #obrana břicha
                if obrana == "b":
                    if s_utok == 1:
                        if mrstnost >= 1:
                            slow_print("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                            mrstnost -= 1
                            zivot_s -= (sila//2)
                        else:
                            slow_print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                            zivot -= 1
                    else:
                        if mrstnost >= 3:
                            slow_print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                            mrstnost -= 3
                            zivot -= (int(sila_s//2))
                        else:
                            slow_print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                            zivot -= sila
                    break
                
                #obrana hlavy
                elif obrana == "h":
                    if s_utok == 2:
                        if mrstnost >= 1:
                            slow_print("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                            mrstnost -= 1
                            zivot_s -= (sila//2)
                        else:
                            slow_print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                            zivot -= 1
                    else:
                        if mrstnost >= 3:
                            slow_print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                            mrstnost -= 3
                            zivot -= (int(sila_s//2))
                        else:
                            slow_print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                            zivot -= sila
                    break
                
                #obrana boku
                elif obrana == "o":
                    if s_utok == 3:
                        if mrstnost >= 1:
                            slow_print("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                            mrstnost -= 1
                            zivot_s -= (sila//2)
                        else:
                            slow_print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                            zivot -= 1
                    else:
                        if mrstnost >= 3:
                            slow_print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                            mrstnost -= 3
                            zivot -= (int(sila_s//2))
                        else:
                            slow_print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                            zivot -= sila
                    break
                else:
                    slow_print("Špatný vstup, zkuste to znovu.\n")
        
        else:
            slow_print("Oba chvíli stojíte a čerpáte energii, protože ani jeden nemáte sílu na útok.")
            
        #doplňování energie hráče
        if (mrstnost + int(zisk_mrstnosti)) < zakl_mrstn:
            mrstnost += zisk_mrstnosti
        
        #doplňování energie soupeře
        if (mrstnost_s + zist_mrstnosti_s) < zakl_mrstn_s:
            mrstnost_s += zist_mrstnosti_s
        
        zivot = last_zivot
        
        if zivot_s <= 0:
            slow_print("Podařilo se vám porazit soupeře.")
            return
        
        elif zivot <= 0:
            shutdown()


#úvod
time.sleep(1)
slow_print("Vítejte!")
time.sleep(1.5)
slow_print("Až budete chtít začít zmáčkněte klávesu enter\n")
input()
slow_print("Vyberte prosím obtížnost: \n")

#výběr obtížnosti
while True:
    obtiznost = input("[e]asy - možnost ukládání\n[h]ard - bez ukládání\n")
    if obtiznost == "h":
        slow_print("Vybrali jste si obtížnost hard.")
        break
    elif obtiznost == "e":
        slow_print("Obtížnost easy ještě není implementována a tudíž vám byla vybrána obtížnost hard.\n")
        break
    else:
        slow_print("Zadali jste špatný znak, zkuste to znovu:\n")

#výběr postavy
while True:
    slow_print("Vyberte si postavu: \n   [t]rpaslík\n  č[l]ověk\n   [e]lf\n")
    vyber_postavy = input()
    if vyber_postavy=="t":
        slow_print("Jste trpaslík, jste velmi silný a vydržíte toho hodně, ale nejste moc mrštný.\n")
        last_zivot = 24
        zivot = 24
        sila = 2
        zakl_mrstn = 8
        mrstnost = 8
        zisk_mrstnosti = 1.5
        break
    elif vyber_postavy=="l":
        slow_print("Jste člověk")
        zivot = 20
        sila = 1
        zakl_mrstn = 10
        mrstnost = 10
        zisk_mrstnosti = 2
        break
    elif vyber_postavy=="e":
        slow_print("Jste elf")
        zivot = 16
        sila = 0.5
        zakl_mrstn = 12
        mrstnost = 12
        zisk_mrstnosti = 2.5
        break
    else:
        slow_print("Nekompatibilní vstup, zkuste to znovu.\n")




#příběh trpaslíka
if vyber_postavy=="t":
    slow_print("Probouzíte se v kobce spoután rezavými řetězy. Vidíte ve své cele ležet obouruční sekeru.\n")
    
    #úvod trpaslíka 1
    while True:
        slow_print("Můžete zkusit začít řvá[t] a tím někoho přivolat, nebo se pokusit zkusit sám [v]ysvobodit.\n")
        spawn_t = input()
        if spawn_t=="t":
            slow_print("Začali jste vyřvávat, ale nikdo nepřišel...\n")
        elif spawn_t=="v":
            slow_print("Povedlo se vám to, dostal jste se z řetězů.\n")
            slow_print("Ale vypadá to, že jak jste se vysvobozovali z řetězů, tak se vám povedlo vyrvat pár kamenů ze zdi a teď se místnost začíná hroutit.\n")
            break
        else:
            slow_print("Neplatná možnost, zkuste to znovu.\n")
    
    #úvod trpaslíka 2
    while True:
        slow_print("Chcete zkusit [v]zít sekyru, nebo raději rychle [u]téct?\n")
        z_spawn_t = input()
        if z_spawn_t == "v":
            slow_print("Povedlo se vám vzít sekyru a utéct z místnosti na poslední chvíli, poté co jste z ní vyběhli se celá zbortila.\n")
            slow_print("Ocitli jste se v další místnosti, před vámi jsou dveře, až budete chtít pokračovat, zmáčkněte enter.\n")
            sila=10
            input()
            break
        elif z_spawn_t =="u":
            slow_print("Utekli jste, a celá místnost za vámi se zbortila, jste v další místnosti a z ní vede jen jeden východ, až budete připraveni zmáčkněte enter.\n")
            mrstnost=14
            zisk_mrstnosti=2.5
            input()
            break
        else:
            slow_print("Špatná možnost, zkuste to znovu.\n")
    fight()


#příběh člověka
if vyber_postavy=="l":
    slow_print("Probouzíte se pod schody, vedle vás leží odhozený krátký meč.")


#příběh elfa
if vyber_postavy == "e":
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
        if roll_six == 3:
            slow_print("\"Máš štěstí,\"povídá osoba,\"nechám tě jít.\"Odemyká vám pouta a odchází.")
            slow_print("\(Jestli se sem příště chcete dostat bez hry s kostkou, zadejte \'pass\'\)\n")
            break
        
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