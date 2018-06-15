import random
import time
import sys

# funkce


def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    print("")
    time.sleep(0.02)


def attack():
    opponent_defence = random.randint(1,3)
    while True:
        slow_print("Chcete útočit na [b]řicho, [h]lavu, nebo na b[o]k\n")
        attack = input("\n")
        if ((attack == "b") and (opponent_defence == 1)) or ((attack == "h") and (opponent_defence == 2)) or ((attack == "o") and (opponent_defence == 3)):
            return 1
        elif ((attack == "b") and (opponent_defence != 1)) or ((attack == "h") and (opponent_defence != 2)) or ((attack == "o") and (opponent_defence != 3)):
            return 2
        else:
            slow_print("Neplatná možnost.\n")


def defence():
    opponent_attack = random.randint(1,3)
    while True:
        slow_print("Myslíte, že soupeř zaútočí na [b]řicho, [h]lavu, nebo na b[o]k?\n")
        defence = input("\n")
        if ((defence == "b") and (opponent_attack == 1)) or ((defence == "h") and (opponent_attack == 2)) or ((defence == "o") and (opponent_attack == 3)):
            return 1
        elif ((defence == "b") and (opponent_attack != 1)) or ((defence == "h") and (opponent_attack != 2)) or ((defence == "o") and (opponent_attack != 3)):
            return 2
        else:
            slow_print("Neplatná možnost.\n")


def player_killed():
    time.sleep(0.6)
    slow_print("Jste mrtev.\n")
    time.sleep(0.8)
    slow_print("SHUTTING DOWN...\n")
    time.sleep(0.4)
    quit()


def rolling_dice():
    dice_roll = random.randint(1, 7)

    if dice_roll >= 6:
        slow_print("Padla 6")
        # slow_print("\"Ty máš ale štěstí!\"\n")
        return 1

    elif dice_roll >= 1 and dice_roll <= 5:
        slow_print("Padla " + str(dice_roll))
        slow_print("\"Smůla, házíš znovu.\"\n")
        return 0


def playerStats():
    global stab
    if weapon == "shortSword":
        damage_type = "cut"
        stab = True
        strenght = 6
        mrstnost = 8
        zisk_mrstnosti = 1.5
        if vyber_postavy == "human":
            strenght += 0.5
            mrstnost += 1
            zisk_mrstnosti += 0.5
        if 50 < short_sword_xp:
            mrstnost += 1
            if 150 <= short_sword_xp:
                zisk_mrstnosti += 0.5

    elif weapon == "twoHandedAxe":
        damage_type = "cut"
        strenght = 8
        mrstnost = 6 
        zisk_mrstnosti = 1
        if character == "dwarf":
            strenght += 2
        if 50 < two_handed_axe_xp:
            mrstnost += 1
            if 150 <= two_handed_axe_xp:
                zisk_mrstnosti += 0.5

    elif weapon == "dagger":
        damage_type = "cut"
        stab = True
        strenght = 5
        mrstnost = 9
        zisk_mrstnosti = 2
        if vyber_postavy == "elf":
            mrstnost += 2 
            zisk_mrstnosti += 0.5
        if 50 < dagger_xp:
            mrstnost += 1
            if 150 <= dagger_xp:
                zisk_mrstnosti += 0.5

    elif weapon == "fists":
        damage_type = "smash"
        if vyber_postavy == "dwarf":
            mrstnost = 14
            strenght = 3
            zisk_mrstnosti = 2.5
        elif vyber_postavy == "human":
            mrstnost = 16
            strenght = 2
            zisk_mrstnosti = 2.5
        elif vyber_postavy == "elf":
            mrstnost = 18
            strenght = 1.5
            zisk_mrstnosti = 3
        if 20 < unarmed_xp:
            mrstnost += 2
            if 50 <= unarmed_xp:
                zisk_mrstnosti += 0.5
                strenght += 1

    return [mrstnost, strenght, zisk_mrstnosti, stab, damage_type]


def fight(last_health):
    global stab
    #enemy generation
    playerStatistics = playerStats()
    mrstnost = playerStatistics[0]
    strenght = playerStatistics[1]
    zisk_mrstnosti = playerStatistics[2]
    stab = playerStatistics[3]

    opp_health = random.randint(12,18)
    max_opp_health = opp_health
    opp_strenght = random.randint(4,8)
    mrstnost_s = random.randint(6,12)
    zakl_mrstn_s = mrstnost_s
    zakl_mrstn = mrstnost
    zist_mrstnosti_s = random.randint(1,2)
    health = last_health
    slow_print("Potkali jste nepřítele, musíte se mu postavit.\n")

    while True:
        #fight status
        time.sleep(0.3)
        slow_print("    Váš život: " + str(health) + "/" + str(last_health))
        slow_print("    Vaše energie: " + str(mrstnost) + "/" + str(zakl_mrstn) + "\n")
        time.sleep(0.3)
        slow_print("    Soupeřův život: " + str(opp_health) + "/" + str(max_opp_health))
        slow_print("    Soupeřova energie: " + str(mrstnost_s) + "/" + str(zakl_mrstn_s) + "\n")
        time.sleep(0.25)
        
        #nabídka akcí útok a obrana = dostatek energie
        if (mrstnost >= 4) and (mrstnost_s >= 4):
            while True:
                slow_print("Chcete ú[t]očit, nebo se [b]ránit?\n")
                nab_akc = input("\n")
                
                #útok
                if nab_akc == "t":
                    mrstnost -= 4
                    attack_consequences = attack()
                    
                    if attack_consequences == 1:
                        slow_print("Soupeři se povedlo úspěšně zablokovat váš útok a odseknout.\n")
                        if mrstnost_s>=2:
                            mrstnost_s -= 1
                            health -= (opp_strenght//2)
                        else:
                            opp_health -= 1

                    elif attack_consequences == 2:
                        if mrstnost_s>=3:
                            mrstnost_s -= 3
                            opp_health -= (int(strenght//2))
                            slow_print("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                        else:
                            opp_health -= strenght
                            slow_print("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")
                    
                    last_fight_action = "attack"
                
                #obrana
                elif nab_akc == "b":
                    mrstnost_s -= 4
                    defence_consequences = defence()

                    if defence_consequences == 1:
                        if mrstnost >= 2:
                            slow_print("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                            mrstnost -= 1
                            opp_health -= (strenght//2)
                        
                        else:
                            slow_print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                            health -= 1

                    elif defence_consequences == 2:
                        if mrstnost >= 3:
                            slow_print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.\n")
                            mrstnost -= 3
                            health -= (int(opp_strenght//2))
                        
                        else:
                            slow_print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou.\n ")
                            health -= strenght

                    last_fight_action = "defence"

                #wrong input
                else:
                    slow_print("Neplatná volba, zkuste to znovu.\n")
                break

        #soupeř nemá dost síly na útok ale hráč ano
        elif (mrstnost >= 4) and (mrstnost_s < 4):
            while True:
                slow_print("Chcete ú[t]očit, nebo č[e]kat a doplňovat síly.\n")
                nab_akc = input()
                    
                #útok
                if nab_akc == "t":
                    mrstnost -= 4
                    attack_consequences = attack()
                    
                    if attack_consequences == 1:
                        slow_print("Soupeři se povedlo úspěšně zablokovat váš útok a odseknout.\n")
                        if mrstnost_s>=2:
                            mrstnost_s -= 1
                            health -= (opp_strenght//2)
                        else:
                            opp_health -= 1

                    elif attack_consequences == 2:
                        if mrstnost_s>=3:
                            mrstnost_s -= 3
                            opp_health -= (int(strenght//2))
                            slow_print("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                        else:
                            opp_health -= strenght
                            slow_print("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")
                    
                    last_fight_action = "attack"

                #vyčkávání
                elif nab_akc == "e":
                    slow_print("Chvíli oba se soupeřem čekáte a doplňujete energii.")
                break

        #nucená obrana = není dost energie na útok        
        elif (mrstnost < 4) and (mrstnost_s >= 4):
            slow_print("Nemáte dost energie na útok, musíte se bránit.\n")
            mrstnost_s -= 4
            defence_consequences = defence()

            if defence_consequences == 1:
                if mrstnost >= 2:
                    slow_print("Úspěšně jste zablokovali soupeřův útok a odsekli.\n")
                    mrstnost -= 1
                    opp_health -= (strenght//2)
                        
                else:
                    slow_print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                    health -= 1

            elif defence_consequences == 2:
                if mrstnost >= 3:
                    slow_print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.\n")
                    mrstnost -= 3
                    health -= (int(opp_strenght//2))
                        
                else:
                    slow_print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou.\n ")
                    health -= strenght

            last_fight_action = "defence"

        elif (mrstnost < 4) and (mrstnost_s) < 4:
            slow_print("Oba chvíli stojíte a čerpáte energii, protože ani jeden nemáte sílu na útok.\n")
            
        #doplňování energie hráče
        if (mrstnost + int(zisk_mrstnosti)) < zakl_mrstn:
            mrstnost += zisk_mrstnosti
        
        #doplňování energie soupeře
        if (mrstnost_s + zist_mrstnosti_s) < zakl_mrstn_s:
            mrstnost_s += zist_mrstnosti_s
        
        
        if opp_health <= 0:
            slow_print("Podařilo se vám porazit soupeře.\n")
            return health
        
        elif health <= 0:
            player_killed()


def healingPotionUse(last_health):
    global healingPotionCount
    if (last_health < max_health) and (healingPotionCount > 0):
        while True:
            if healingPotionCount == 1:
                slow_print("Máte 1 léčící lektvar, chcete ho [p]oužít, nebo si ho [n]echat na později?\n")
            
            elif healingPotionCount > 1:
                slow_print("Máte " + str(healingPotionCount) + " léčících lektvarů, chcete jeden [p]oužít, nebo si ho [n]echat na později?\n")
            healingPotionUse = input()
            
            if healingPotionUse == "p":
                healingPotionCount -= 1
                last_health += 10
                if last_health > max_health:
                    last_health = max_health
                slow_print("Váš život: " + str(last_health))
                return [last_health , healingPotionCount]
            
            elif healingPotionUse == "n":
                slow_print("Váš život: " + str(last_health))
                return [last_health , healingPotionCount]
    
    else:
        return [last_health , healingPotionCount]


# úvod
def introduction():
    time.sleep(0.3)
    slow_print("Vítejte ve verzi Alpha 0.041")
    time.sleep(0.8)
    slow_print("Až budete chtít začít zmáčkněte klávesu enter\n")
    input()
    difficulty_selection()


# výběr obtížnosti
def difficulty_selection():
    while True:
        slow_print("Vyberte prosím obtížnost: \n")
        time.sleep(0.2)
        slow_print(" [l]ehká - možnost ukládání, málo a lehých soubojů.\n"
                   " [s]třední - možnost ukládání, hodně lehkých soubojů.\n"
                   " [t]ěžká - bez ukládání, hodně a těžkých soubojů.\n")
        obtiznost = input()
        if obtiznost == "h":
            slow_print("Vybrali jste si obtížnost hard.")
            difficulty = "hard"
            return
        elif obtiznost == "e":
            slow_print("Obtížnost easy ještě není implementována a tudíž vám byla vybrána obtížnost hard.\n")
            return
        else:
            slow_print("Zadali jste špatný znak, zkuste to znovu:\n")


# výběr postavy
def character_selection():
    while True:
        slow_print("Vyberte si postavu: \n   [t]rpaslík\n  č[l]ověk\n   [e]lf\n")
        vyber_postavy = input()
        if vyber_postavy=="t":
            slow_print("Jste trpaslík, jste velmi silný a vydržíte toho hodně, ale nejste moc mrštný.\n")
            max_health = 24
            last_health = 24
            health = 24
            shortSwordSkillLvl = 0
            break
        elif vyber_postavy=="l":
            slow_print("Jste člověk")
            max_health = 20
            last_health = 20
            health = 20
            shortSwordSkillLvl = 0
            break
        elif vyber_postavy=="e":
            slow_print("Jste elf")
            max_health = 18
            last_health = 18
            health = 18
            shortSwordSkillLvl = 0
            break
        else:
            slow_print("Nekompatibilní vstup, zkuste to znovu.\n")

#příběh trpaslíka
if vyber_postavy=="t":
    x = 3
    y = 3
    last_direction = None
    healingPotionCount += 1
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
        slow_print("Chcete raději [v]zít sekyru, [l]éčíci lektvar, nebo zkusit vzít [o]bojí?\n")
        z_spawn_t = input()
        if z_spawn_t == "v":
            slow_print("Povedlo se vám vzít sekyru a utéct z místnosti na poslední chvíli, poté co jste z ní vyběhli se celá zbortila.\n")
            weapon = "twoHandedAxe"
            slow_print("Ocitli jste se v další místnosti, před vámi jsou dveře, až budete chtít pokračovat, zmáčkněte enter.\n")
            input()
            break
        elif z_spawn_t =="l":
            slow_print("Vzali jste lektvar a utekli, celá místnost za vámi se zbortila, jste v další místnosti a z ní vede jen jeden východ, až budete připraveni zmáčkněte enter.\n")
            weapon = "fists"
            healingPotionCount += 1
            input()
            break
        elif z_spawn_t == "o":
            deathRoll = random.randint(1,3)
            if deathRoll == 3:
                weapon = "twoHandedAxe"
                healingPotionCount += 1
                slow_print("Dokázali jste to, vzali jste jak sekyru, tak lektvar. Hned jakmile jste je sebrali utekli jste a místnost se zhroutila.")
                break
            else:
                slow_print("Povedlo se vám vzít sekeru, ale když jste brali lektvar, tak se na vás zřítil strop.")
                player_killed()
        else:
            slow_print("Špatná možnost, zkuste to znovu.\n")
    
    room_picking(x,y,last_direction,last_health,healingPotionCount)

#příběh člověka
if vyber_postavy=="l":
    x = 0
    y = 2
    last_direction = None
    slow_print("Probouzíte se pod schody s ohromnou boletí hlavy, postupně se zvedáte a vidíte, že vedle vás leží odhozený krátký meč a rozežhnutá louče.")
    while True:
        slow_print("Chcete [s]ebrat meč nebo [j]ít dál?")
        humanSpawnAction = input()
        if humanSpawnAction == "s":
            slow_print("Berete tedy meč a louči.\n")
            weapon = "shortSword"
            break
        elif humanSpawnAction == "j":
            slow_print("Sebrali jste jen louči, bez meče se budete mít problém bránit, ale kdybyste ho nakonec chtěli, tak se pro něj můžete kdykoliv vrátit.\n")
            weapon = "fists"
            break
        else:
            slow_print("Nekompatibilní vstup, zkuste to znovu.\n")
    
    room_picking(x,y,last_direction,last_health,healingPotionCount)

#příběh elfa
if vyber_postavy == "e":
    slow_print("Jste v temné místnosti a můžete hýbat jen pravou rukou, před vámi sedí osoba s nataženou rukou podávající vám hrací kostku a říkající: \"Hoď si, když ti nepadne třikrát z 12 hodů 6, tak zemřeš.\"\n")
    x = 3
    y = 3
    last_direction = None
    
    roll_six = 0
    diceRolled = 0

    while True:
        if roll_six == 3:
            slow_print("\"Máš štěstí,\"povídá osoba,\"nechám tě jít.\"Odemyká vám pouta a odchází.")
            time.sleep(0.5)
            slow_print("(Jestli se sem příště chcete dostat bez hry s kostkou, zadejte \'pass\')\n")
            break

        if diceRolled == 12:
            slow_print("\"To by stačilo,\" osoba před vámi vytáhne nůž a probodne vás.\n")
            player_killed()
        
        slow_print("Můžete [h]odit kostkou, nebo č[e]kat.")
        elf_dice_game = input()
        
        if elf_dice_game == "h":
            roll_six += rolling_dice()
            diceRolled +=1
        elif elf_dice_game == "e":
            time.sleep(2.5)
            slow_print("\"Tohle už mě nebaví.\" Osoba před vámi vytáhne nůž a probodne vás.\n")
            player_killed()
        elif elf_dice_game == "pass":
            slow_print("Přeskakování hry s kostkou...")
            time.sleep(1.25)
            break
        else:
            slow_print("Vyberte jednu z možností.")
    
    while True:
        slow_print("Jak osoba odcházela nechala na stole nůž, chcete ho [v]zít, nebo jít [d]ál bez něj?")
        elf_weapon_pick = input()
        if elf_weapon_pick == "v":
            weapon = "dagger"
            break
        elif elf_weapon_pick == "d":
            weapon = "fists"
            break
        else:
            slow_print("Wrong input.")


    room_picking(x,y,last_direction,last_health,healingPotionCount)

#rozloučení
slow_print("Pro odchod ze hry zmáčkněte enter.")
input()