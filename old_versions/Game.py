import random
import time

#úvod
print("Vítejte!")
input("Až budete chtít začít zmáčkněte klávesu enter\n")
print("Vyberte prosím obtížnost: \n")

#výběr obtížnosti
while True:
    obtiznost = input("[e]asy - možnost ukládání\n[h]ard - bez ukládání\n")
    if obtiznost == "h":
        print("Vybrali jste si obtížnost hard.")
        break

    elif obtiznost == "e":
        print("Obtížnost easy ještě není implementována a tudíž vám byla vybrána obtížnost hard.\n")
        break

    else:
        print("Zadali jste špatný znak, zkuste to znovu:\n")

#výběr postavy
while True:
    vyber_postavy = input("Vyberte si postavu: \n   [t]rpaslík\n  č[l]ověk\n   [e]lf\n")

    if vyber_postavy=="t":
        print("Jste trpaslík, jste velmi silný a vydržíte toho hodně, ale nejste moc mrštný.\n")
        last_zivot = 24
        zivot = 24
        sila = 2
        zakl_mrstn = 8
        mrstnost = 8
        zisk_mrstnosti = 1.5
        break

    elif vyber_postavy=="l":
        print("Jste člověk")
        zivot = 20
        sila = 1
        zakl_mrstn = 10
        mrstnost = 10
        zisk_mrstnosti = 2
        break

    elif vyber_postavy=="e":
        print("Jste elf")
        zivot = 16
        sila = 0.5
        zakl_mrstn = 12
        mrstnost = 12
        zisk_mrstnosti = 2.5
        break

    else:
        print("Nekompatibilní vstup, zkuste to znovu.\n")


#funkce
def fight():
    print("Potkali jste nepřítele, musíte se mu postavit.\n")
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
        print("Váš život: " + str(zivot) + "/" + str(max_zivot))
        print("Vaše energie: " + str(mrstnost) + "/" + str(zakl_mrstn) + "\n")
        print("Soupeřův život: " + str(zivot_s) + "/" + str(max_zivot_s))
        print("Soupeřova energie: " + str(mrstnost_s) + "/" + str(zakl_mrstn_s) + "\n")
        
        #nabídka akcí útok a obrana = dostatek energie
        while mrstnost >= 4:
                nab_akc = input("Chcete ú[t]očit, nebo se [b]ránit?\n")
                
                #útok
                if nab_akc == "t":
                    mrstnost -= 4
                    s_obrana = random.randint(1,3)
                    while True:
                        utok = input("Chcete útočit na [b]řicho, [h]lavu, nebo na b[o]k\n")
                        
                        #utok na břicho
                        if utok == "b":
                            if s_obrana == 1:
                                print("Soupeři se povedlo úspěšně zablokovat váš útok\n")
                                if mrstnost_s>=1:
                                    mrstnost_s -= 1
                                else:
                                    zivot_s -= 1
                            else:
                                if mrstnost_s>=3:
                                    mrstnost_s -= 3
                                    zivot_s -= (int(sila//2))
                                    print("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                                else:
                                    zivot_s -= sila
                                    print("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")  
                            break
                        
                        #útok na hlavu
                        elif utok == "h":
                            if s_obrana == 2:
                                print("Soupeři se povedlo úspěšně zablokovat váš útok\n")
                                if mrstnost_s >=1:
                                    mrstnost_s -= 1
                                else:
                                    zivot_s -= 1
                            else:
                                if mrstnost_s>=3:
                                    mrstnost_s -= 3
                                    zivot_s -= (int(sila//2))
                                    print("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                                else:
                                    zivot_s -= sila
                                    print("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")
                            break    
                        
                        #útok na bok
                        elif utok == "o":
                            if s_obrana == 3:
                                print("Soupeři se povedlo úspěšně zablokovat váš útok\n")
                                if mrstnost_s >=1:
                                    mrstnost_s -= 1
                                else:
                                    zivot_s -= 1
                            else:
                                if mrstnost_s>=3:
                                    mrstnost_s -= 3
                                    zivot_s -= (int(sila//2))
                                    print("Soupeř kryl špatně, ale ještě se mu na poslední chvíli povedlo útok částečně vykrýt.\n")
                                else:
                                    zivot_s -= sila
                                    print("Soupeř kryl špatně a už neměl dost síly, aby svůj kryt rychle změnil.\n")
                            break
                        
                        #wrong input
                        else:
                            print("Neplatná možnost.\n")
                    break
                
                #obrana
                elif nab_akc == "b":
                    s_utok = random.randint(1,3)
                    while True:
                        obrana = input("Myslíte, že soupeř zaútočí na [b]řicho, [h]lavu, nebo na b[o]k?\n")
                        
                        #obrana břicha
                        if obrana == "b":
                            if s_utok == 1:
                                zivot_s -= (sila//2)
                                if mrstnost >= 1:
                                    print("Úspěšně jste zablokovali soupeřův útok.\n")
                                    mrstnost -= 1
                                else:
                                    print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                                    zivot -= 1
                            else:
                                if mrstnost >= 3:
                                    print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                                    mrstnost -= 3
                                    zivot -= (int(sila_s//2))
                                else:
                                    print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                                    zivot -= sila
                            break
                        
                        #obrana hlavy
                        elif obrana == "h":
                            if s_utok == 2:
                                zivot_s -= (sila//2)
                                if mrstnost >= 1:
                                    print("Úspěšně jste zablokovali soupeřův útok.\n")
                                    mrstnost -= 1
                                else:
                                    print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                                    zivot -= 1
                            else:
                                if mrstnost >= 3:
                                    print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                                    mrstnost -= 3
                                    zivot -= (int(sila_s//2))
                                else:
                                    print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                                    zivot -= sila
                            break
                        
                        #obrana boku
                        elif obrana == "o":
                            if s_utok == 3:
                                zivot_s -= (sila//2)
                                if mrstnost >= 1:
                                    print("Úspěšně jste zablokovali soupeřův útok.\n")
                                    mrstnost -= 1
                                else:
                                    print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                                    zivot -= 1
                            else:
                                if mrstnost >= 3:
                                    print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                                    mrstnost -= 3
                                    zivot -= (int(sila_s//2))
                                else:
                                    print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                                    zivot -= sila
                            break
                        else:
                            print("Špatný vstup, zkuste to znovu.\n")
                    break
                
                #wrong input
                else:
                    print("Neplatná volba, zkuste to znovu.\n")
        
        #nucená obrana = není dost energie na útok
        else:
            print("Nemáte dost energie na útok, musíte se bránit.\n")
            s_utok = random.randint(1,3)

            while True:
                obrana = input("Myslíte, že soupeř zaútočí na [b]řicho, [h]lavu, nebo na b[o]k?\n")
                #obrana břicha
                if obrana == "b":

                    if s_utok == 1:
                        zivot_s -= (sila//2)
                        if mrstnost >= 1:
                            print("Úspěšně jste zablokovali soupeřův útok.\n")
                            mrstnost -= 1
                        else:
                            print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                            zivot -= 1

                    else:
                        if mrstnost >= 3:
                            print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                            mrstnost -= 3
                            zivot -= (int(sila_s//2))
                        else:
                            print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                            zivot -= sila
                    break
                
                #obrana hlavy
                elif obrana == "h":

                    if s_utok == 2:
                        zivot_s -= (sila//2)
                        if mrstnost >= 1:
                            print("Úspěšně jste zablokovali soupeřův útok.\n")
                            mrstnost -= 1
                        else:
                            print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                            zivot -= 1

                    else:
                        if mrstnost >= 3:
                            print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                            mrstnost -= 3
                            zivot -= (int(sila_s//2))
                        else:
                            print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                            zivot -= sila
                    break
                
                #obrana boku
                elif obrana == "o":

                    if s_utok == 3:
                        zivot_s -= (sila//2)
                        if mrstnost >= 1:
                            print("Úspěšně jste zablokovali soupeřův útok.\n")
                            mrstnost -= 1
                            zivot_s -= (sila//2)
                        else:
                            print("Úspěšně jste zablokovali soupeřův útok, ale už jste neměli dost energie a tak vás soupeř lehce zranil.\n")
                            zivot -= 1

                    else:
                        if mrstnost >= 3:
                            print("Kryli jste špatně, ale ještě jste měli dost energie soupeřův útok částečně zablokovat.")
                            mrstnost -= 3
                            zivot -= (int(sila_s//2))
                        else:
                            print("Váš kryt byl špatný a už jste neměli dost energie ho změnit a tak vás soupeř zasáhl plnou silou. ")
                            zivot -= sila
                    break
                else:
                    print("Špatný vstup, zkuste to znovu.\n")
        
        #doplňování energie
        if (mrstnost + int(zisk_mrstnosti)) < zakl_mrstn:
            mrstnost += zisk_mrstnosti

        if (mrstnost_s + zist_mrstnosti_s) < zakl_mrstn_s:
            mrstnost_s += zist_mrstnosti_s

        zivot = last_zivot

        if zivot_s <= 0:
            print("Podařilo se vám porazit soupeře.")
            return

        elif zivot <= 0:
            input("Jste mrtev.")
            quit()


#příběh trpaslíka
if vyber_postavy=="t":
    print("Probouzíte se v kobce spoután rezavými řetězy. Vidíte ve své cele ležet obouruční sekeru.\n")
    
    #úvod trpaslíka 1
    while True:
        spawn_t = input("Můžete zkusit začít řvá[t] a tím někoho přivolat, nebo se pokusit zkusit sám [v]ysvobodit.\n")
        if spawn_t=="t":
            print("Začali jste vyřvávat, ale nikdo nepřišel...\n")
        elif spawn_t=="v":
            print("Povedlo se vám to, dostal jste se z řetězů.\n")
            print("Ale vypadá to, že jak jste se vysvobozovali z řetězů, tak se vám povedlo vyrvat pár kamenů ze zdi a teď se místnost začíná hroutit.\n")
            break
        else:
            print("Neplatná možnost, zkuste to znovu.\n")
    
    #úvod trpaslíka 2
    while True:
        z_spawn_t = input("Chcete zkusit [v]zít sekyru, nebo raději rychle [u]téct?\n")
        if z_spawn_t == "v":
            print("Povedlo se vám vzít sekyru a utéct z místnosti na poslední chvíli, poté co jste z ní vyběhli se celá zbortila.\n")
            print("Ocitli jste se v další místnosti, před vámi jsou dveře, až budete chtít pokračovat, zmáčkněte enter.\n")
            sila=10
            input()
            break
        elif z_spawn_t =="u":
            print("Utekli jste, a celá místnost za vámi se zbortila, jste v další místnosti a z ní vede jen jeden východ, až budete připraveni zmáčkněte enter.\n")
            mrstnost=14
            zisk_mrstnosti=2.5
            input()
            break
        else:
            print("Špatná možnost, zkuste to znovu.\n")
    fight()


#příběh člověka
if vyber_postavy=="l":
    print("Probouzíte se pod schody, vedle vás leží odhozený krátký meč.")


#příběh elfa
if vyber_postavy=="e":
    print("Jste v temné místnosti a můžete hýbat jen pravou rukou, před vámi sedí osoba s nataženou rukou podávající vám hrací kostku a říkající: \"Hoď si, když ti padne 1 až 5, pak zemřeš.\"")  
input()
