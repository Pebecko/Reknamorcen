def roomTypeN():
    if last_direction == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif last_direction == "South":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    last_direction = "North"
    y -= 1
    return [x,y,last_direction]

def roomTypeE():
    if last_direction == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif last_direction == "West":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    last_direction = "East"
    x += 1
    return [x,y,last_direction]    

def roomTypeS():
    if last_direction == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif last_direction == "North":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    last_direction = "South"
    y += 1
    return [x,y,last_direction]

def roomTypeW():
    if last_direction == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif last_direction == "East":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    last_direction = "East"
    x -= 1
    return [x,y,last_direction]

def roomTypeNE():
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "North"
            y -= 1
        
        elif directionChoice == "p":
            last_direction = "East"
            x += 1

    elif last_direction == "South":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "North"
            y -= 1

        elif directionChoice == "l":
            last_direction = "East"
            x += 1

    elif last_direction == "West":
        slowPrint("Můžete jít [z]pět, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "East"
            x += 1

        elif directionChoice == "p":
            last_direction = "North"
            y -= 1

    return [x,y,last_direction]

def roomTypeNS():
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "North"
            y -= 1
        
        elif directionChoice == "z":
            last_direction = "South"
            y += 1

    elif last_direction == "South":
        slowPrint("Můžete jít [z]pět, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "North"
            y -= 1

        elif directionChoice == "r":
            last_direction = "South"
            y += 1

    elif last_direction == "North":
        slowPrint("Můžete jít [z]pět, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "South"
            y += 1

        elif directionChoice == "r":
            last_direction = "North"
            y -= 1

    return [x,y,last_direction]

def roomTypeNW():
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "North"
            y -= 1
        
        elif directionChoice == "l":
            last_direction = "West"
            x -= 1

    elif last_direction == "South":
        slowPrint("Můžete jít [z]pět, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "North"
            y -= 1

        elif directionChoice == "p":
            last_direction = "West"
            x -= 1

    elif last_direction == "East":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "West"
            x -= 1

        elif directionChoice == "l":
            last_direction = "North"
            y -= 1

    return [x,y,last_direction]

def roomTypeES():
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "East"
            x += 1
        
        elif directionChoice == "p":
            last_direction = "South"
            y += 1

    elif last_direction == "North":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "South"
            y += 1

        elif directionChoice == "l":
            last_direction = "East"
            x += 1

    elif last_direction == "West":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "East"
            x += 1

        elif directionChoice == "l":
            last_direction = "South"
            y += 1

    return [x,y,last_direction]

def roomTypeEW():
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "East"
            x += 1
        
        elif directionChoice == "z":
            last_direction = "West"
            x -= 1

    elif last_direction == "East":
        slowPrint("Můžete jít [z]pět, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "West"
            x -= 1

        elif directionChoice == "l":
            last_direction = "East"
            x += 1

    elif last_direction == "West":
        slowPrint("Můžete jít [z]pět, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "East"
            x += 1

        elif directionChoice == "r":
            last_direction = "West"
            x -= 1

    return [x,y,last_direction]

def roomTypeSW():
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "South"
            y += 1
        
        elif directionChoice == "p":
            last_direction = "West"
            x -= 1

    elif last_direction == "North":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "South"
            y += 1

        elif directionChoice == "l":
            last_direction = "West"
            x += 1

    elif last_direction == "East":
        slowPrint("Můžete jít [z]pět, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "West"
            x += 1

        elif directionChoice == "p":
            last_direction = "South"
            y += 1

    return [x,y,last_direction]

def roomTypeNES():
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "North"
            y -= 1
        
        elif directionChoice == "p":
            last_direction = "East"
            x += 1

        elif directionChoice == "z":
            last_direction = "South"
            y += 1

    elif last_direction == "South":
        slowPrint("Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "North"
            y -= 1

        elif directionChoice == "l":
            last_direction = "East"
            x += 1

        elif directionChoice == "r":
            last_direction = "South"
            y += 1

    elif last_direction == "West":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "East"
            x += 1

        elif directionChoice == "p":
            last_direction = "North"
            y -= 1

        elif directionChoice == "l":
            last_direction = "South"
            y += 1

    elif last_direction == "North":
        slowPrint("Můžete jít [z]pět, [r]ovně, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "South"
            y += 1

        elif directionChoice == "r":
            last_direction = "North"
            y -= 1

        elif directionChoice == "p":
            last_direction = "East"
            x += 1

    return [x,y,last_direction]

def roomTypeNEW():
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, v[p]ravo, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "North"
            y -= 1
        
        elif directionChoice == "p":
            last_direction = "East"
            x += 1

        elif directionChoice == "l":
            last_direction = "West"
            x -= 1

    elif last_direction == "South":
        slowPrint("Můžete jít [z]pět, v[l]evo, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "North"
            y -= 1

        elif directionChoice == "l":
            last_direction = "East"
            x += 1

        elif directionChoice == "p":
            last_direction = "West"
            x -= 1

    elif last_direction == "West":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "East"
            x += 1

        elif directionChoice == "p":
            last_direction = "North"
            y -= 1

        elif directionChoice == "r":
            last_direction = "West"
            x -= 1

    elif last_direction == "East":
        slowPrint("Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "West"
            x -= 1

        elif directionChoice == "r":
            last_direction = "East"
            x += 1

        elif directionChoice == "l":
            last_direction = "North"
            y -= 1

    return [x,y,last_direction]

def roomTypeNSW():
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, v[l]evo, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "North"
            y -= 1
        
        elif directionChoice == "l":
            last_direction = "West"
            x -= 1

        elif directionChoice == "z":
            last_direction = "South"
            y += 1

    elif last_direction == "South":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "North"
            y -= 1

        elif directionChoice == "p":
            last_direction = "West"
            x -= 1

        elif directionChoice == "r":
            last_direction = "South"
            y += 1

    elif last_direction == "East":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "West"
            x -= 1

        elif directionChoice == "l":
            last_direction = "North"
            y -= 1

        elif directionChoice == "p":
            last_direction = "South"
            y += 1

    elif last_direction == "North":
        slowPrint("Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "South"
            y += 1

        elif directionChoice == "r":
            last_direction = "North"
            y -= 1

        elif directionChoice == "l":
            last_direction = "West"
            x -= 1

    return [x,y,last_direction]

def roomTypeESW():#dodělat
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, v[l]evo, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "North"
            y -= 1
        
        elif directionChoice == "l":
            last_direction = "West"
            x -= 1

        elif directionChoice == "z":
            last_direction = "South"
            y += 1

    elif last_direction == "South":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "North"
            y -= 1

        elif directionChoice == "p":
            last_direction = "West"
            x -= 1

        elif directionChoice == "r":
            last_direction = "South"
            y += 1

    elif last_direction == "East":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "West"
            x -= 1

        elif directionChoice == "l":
            last_direction = "North"
            y -= 1

        elif directionChoice == "p":
            last_direction = "South"
            y += 1

    elif last_direction == "North":
        slowPrint("Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "South"
            y += 1

        elif directionChoice == "r":
            last_direction = "North"
            y -= 1

        elif directionChoice == "l":
            last_direction = "West"
            x -= 1

    return [x,y,last_direction]

def roomTypeNESW():

def roomOneSpawnOne():
    global lastRoom
    global room
    if lastRoom == 2:
        while True:
            directionChoice = input("Chcete jít [z]pět?\n")
            if directionChoice == "z":
                room = 2
                break
            else:
                print("Wrong input.\n")

    elif lastRoom == 0:
        while True:
            directionChoice = input("Chcete jít [r]ovně?\n")
            if directionChoice == "r":
                room = 2
                break
            else:
                print("Wrong input.\n")

    lastRoom = 1        
    return [room,lastRoom]

def roomTwo():
    global lastRoom
    global room
    if lastRoom == 1:
        while True:
            directionChoice = input("Chcete jít [z]pět, nebo v[l]evo?\n")
            if directionChoice == "z":
                room = 1
                break
            elif directionChoice == "l":
                room = 3
                break
            else:
                print("Wrong input.\n")

    elif lastRoom == 3:
        while True:
            directionChoice = input("Chcete jít [z]pět, nebo v[p]ravo?\n")
            if directionChoice == "z":
                room = 3
                break
            elif directionChoice =="p":
                room = 1
                break
            else:
                print("Wrong input.\n")

    lastRoom = 2
    return [room,lastRoom]

def roomThree():
    lastRoom = 3
    return [room,lastRoom]

def roomFourExit():
    lastRoom = 4
    return [room,lastRoom]

def roomFive():
    lastRoom = 5
    return [room,lastRoom]

def roomSixSpawnTwo():
    lastRoom = 6
    return [room,lastRoom]

lastRoom = 0
while True:
    spawnChoice = input("Vyber místnost 1, nebo 2\n")
    if spawnChoice == "1":
        room = 1 
        break
    elif spawnChoice == "2":
        room = 6
        break
    else:
        print("Wrong input\n")


while True:
    if room == 1:
        roomOneSpawnOne()
    
    elif room == 2:
        roomTwo()
    
    elif room == 3:
        roomThree()
    
    elif room == 4:
        roomFourExit
    
    elif room == 5:
        roomFive
    
    elif room == 6:
        roomSixSpawnTwo
    
    elif room == 7:
        break
input("Press enter to exit.")