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

def roomPicking(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
    while True:
        if x == 0 and y == 2:
            coordinates = roomSixSpawnTwo(x,y,last_direction)
        elif x == 1 and y == 2:
            coordinates = roomFive(x,y,last_direction)
        elif x == 2 and y == 2:
            coordinates = roomThree(x,y,last_direction)
        elif x == 2 and y == 1:
            coordinates = roomFourExit(x,y,last_direction)
        elif x == 2 and y == 0:
            slowPrint("Právě odcházíte.")
            time.sleep(2)
            quit()
        elif x == 3 and y == 2:
            coordinates = roomTwo(x,y,last_direction)
        elif x == 3 and y == 3:
            coordinates = roomOneSpawnOne(x,y,last_direction)
        
        x = coordinates[0]
        y = coordinates[1]
        last_direction = coordinates[2]

def getCoordinates(xi,yi,direction):
    x = xi
    y = yi
    if  direction == "North":
        y -= 1
    elif direction == "East":
        x += 1
    elif direction == "South":
        y += 1
    elif direction == "West":
        x -= 1
    return [x,y]

def roomTypeN(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
    if last_direction == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif last_direction == "South":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    last_direction = "North"
    coordinates = getCoordinates(x,y,last_direction)
    x = coordinates[0]
    y = coordinates[-1]
    return [x,y,last_direction]

def roomTypeE(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
    if last_direction == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif last_direction == "West":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    last_direction = "East"
    x += 1
    return [x,y,last_direction]

def roomTypeS(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
    if last_direction == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif last_direction == "North":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    last_direction = "South"
    y += 1
    return [x,y,last_direction]

def roomTypeW(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
    if last_direction == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif last_direction == "East":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    last_direction = "East"
    x -= 1
    return [x,y,last_direction]

def roomTypeNE(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
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

def roomTypeNS(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
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

def roomTypeNW(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
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

def roomTypeES(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
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

def roomTypeEW(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
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

        elif directionChoice == "r":
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

def roomTypeSW(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
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
            x -= 1

    elif last_direction == "East":
        slowPrint("Můžete jít [z]pět, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "West"
            x -= 1

        elif directionChoice == "p":
            last_direction = "South"
            y += 1

    return [x,y,last_direction]

def roomTypeNES(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
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

def roomTypeNEW(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
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

def roomTypeNSW(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
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

def roomTypeESW(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
    if last_direction == None:
        slowPrint("Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            last_direction = "East"
            x += 1
        
        elif directionChoice == "p":
            last_direction = "South"
            y += 1

        elif directionChoice == "z":
            last_direction = "West"
            x -= 1

    elif last_direction == "West":
        slowPrint("Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "East"
            x += 1

        elif directionChoice == "l":
            last_direction = "South"
            y += 1

        elif directionChoice == "r":
            last_direction = "West"
            x -= 1

    elif last_direction == "East":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            last_direction = "West"
            x -= 1

        elif directionChoice == "r":
            last_direction = "East"
            x += 1

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

def roomTypeNESW(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction
    pass
    
    coordinates = getCoordinates(last_direction)
    x = coordinates[0]
    y = coordinates[-1]

    return [x,y,last_direction]

def roomOneSpawnOne(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction

    coordinates = roomTypeN(x,y,last_direction)
    x = coordinates[0]
    y = coordinates[1]
    last_direction = coordinates[2]
    return [x,y,last_direction]

def roomTwo(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction

    coordinates = roomTypeSW(x,y,last_direction)
    x = coordinates[0]
    y = coordinates[1]
    last_direction = coordinates[2]
    return [x,y,last_direction]

def roomThree(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction

    coordinates = roomTypeNEW(x,y,last_direction)
    x = coordinates[0]
    y = coordinates[1]
    last_direction = coordinates[2]
    return [x,y,last_direction]

def roomFourExit(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction

    coordinates = roomTypeNS(x,y,last_direction)
    x = coordinates[0]
    y = coordinates[1]
    last_direction = coordinates[2]
    return [x,y,last_direction]

def roomFive(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction

    coordinates = roomTypeEW(x,y,last_direction)
    x = coordinates[0]
    y = coordinates[1]
    last_direction = coordinates[2]
    return [x,y,last_direction]

def roomSixSpawnTwo(xi,yi,last_direction):
    x = xi
    y = yi
    last_direction = last_direction

    coordinates = roomTypeE(x,y,last_direction)
    x = coordinates[0]
    y = coordinates[1]
    last_direction = coordinates[2]
    return [x,y,last_direction]

while True:
    last_direction = None
    spawnChoice = input("Vyber místnost 1, nebo 2\n")
    if spawnChoice == "1":
        x = 3
        y = 3
        break
    elif spawnChoice == "2":
        x = 0
        y = 2
        break
    else:
        print("Wrong input\n")

roomPicking(x,y,last_direction)

input("Press enter to exit.")
