import random
#místnost s cestou rovně
def room_s()
    input("Můžete jít jen rovně, zmáčkněte enter až budete přiraveni.")
    next_room = random.randint(2,7)
    if next_room == 2:
        room_l()
    elif next_room == 3:
        room_r
    
#místnost s cestou vlevo
def room_l()
    input("Můžete jít jen vlevo, zmáčkněte enter až budete přiraveni.")
#místnost s cestou vpravo
def room_r()
    input("Můžete jít jen vpravo, zmáčkněte enter až budete přiraveni.")
#místnost s cestou rovně a vpravo
def room_sr()
    while True:
        direction = input("Můžete jít v[p]ravo a nebo [r]ovně.")
        if direction == "p":
            break
        elif direction == "r":
            break
        else:
            print("Nesprávný vstup, zkuste to znovu.")
#místnost s cestou rovně a vlevo
def room_ls()
    while True:
        direction = input("Můžete jít v[l]evo a nebo [r]ovně.")
        if direction == "l":
            break
        elif direction == "r":
            break
        else:
            print("Nesprávný vstup, zkuste to znovu.")
#místnost s cestou vlevo a vpravo
def room_lr()
    while True:
        direction = input("Můžete jít v[l]evo a nebo v[p]ravo.")
#místnost s cestou vlevo rovně a vpravo
def room_lsr()
    while True:
        direction = input("Můžete jít v[l]evo v[p]ravo a nebo [r]ovně.")
