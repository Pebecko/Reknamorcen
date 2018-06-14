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

def roomPicking(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    while True:
        if x == 0 and y == 2:
            coordinates = roomSixSpawnTwo(x,y,lastDirection)
        elif x == 1 and y == 2:
            coordinates = roomFive(x,y,lastDirection)
        elif x == 2 and y == 2:
            coordinates = roomThree(x,y,lastDirection)
        elif x == 2 and y == 1:
            coordinates = roomFourExit(x,y,lastDirection)
        elif x == 2 and y == 0:
            slowPrint("Právě odcházíte.")
            time.sleep(2)
            quit()
        elif x == 3 and y == 2:
            coordinates = roomTwo(x,y,lastDirection)
        elif x == 3 and y == 3:
            coordinates = roomOneSpawnOne(x,y,lastDirection)
        
        x = coordinates[0]
        y = coordinates[1]
        lastDirection = coordinates[2]

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

def roomTypeN(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif lastDirection == "South":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    lastDirection = "North"
    coordinates = getCoordinates(x,y,lastDirection)
    x = coordinates[0]
    y = coordinates[-1]
    return [x,y,lastDirection]

def roomTypeE(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif lastDirection == "West":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    lastDirection = "East"
    x += 1
    return [x,y,lastDirection]    

def roomTypeS(xi,yi,last_directioni):
    x = xi
    y = yi
    last_direction = last_directioni
    if last_direction == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif last_direction == "North":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    last_direction = "South"
    y += 1
    return [x,y,last_direction]

def roomTypeW(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít pouze rovně, zmáčkněte enter až budete připraveni.\n")
        input()

    elif lastDirection == "East":
        slowPrint("Můžete jít pouze zpět, zmáčkněte enter až budete připraveni.\n")
        input()

    lastDirection = "East"
    x -= 1
    return [x,y,lastDirection]

def roomTypeNE(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "North"
            y -= 1
        
        elif directionChoice == "p":
            lastDirection = "East"
            x += 1

    elif lastDirection == "South":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "l":
            lastDirection = "East"
            x += 1

    elif lastDirection == "West":
        slowPrint("Můžete jít [z]pět, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "East"
            x += 1

        elif directionChoice == "p":
            lastDirection = "North"
            y -= 1

    return [x,y,lastDirection]

def roomTypeNS(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "North"
            y -= 1
        
        elif directionChoice == "z":
            lastDirection = "South"
            y += 1

    elif lastDirection == "South":
        slowPrint("Můžete jít [z]pět, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "r":
            lastDirection = "South"
            y += 1

    elif lastDirection == "North":
        slowPrint("Můžete jít [z]pět, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "South"
            y += 1

        elif directionChoice == "r":
            lastDirection = "North"
            y -= 1

    return [x,y,lastDirection]

def roomTypeNW(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "North"
            y -= 1
        
        elif directionChoice == "l":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "South":
        slowPrint("Můžete jít [z]pět, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "p":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "East":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "West"
            x -= 1

        elif directionChoice == "l":
            lastDirection = "North"
            y -= 1

    return [x,y,lastDirection]

def roomTypeES(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "East"
            x += 1
        
        elif directionChoice == "p":
            lastDirection = "South"
            y += 1

    elif lastDirection == "North":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "South"
            y += 1

        elif directionChoice == "l":
            lastDirection = "East"
            x += 1

    elif lastDirection == "West":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "East"
            x += 1

        elif directionChoice == "l":
            lastDirection = "South"
            y += 1

    return [x,y,lastDirection]

def roomTypeEW(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "East"
            x += 1
        
        elif directionChoice == "z":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "East":
        slowPrint("Můžete jít [z]pět, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "West"
            x -= 1

        elif directionChoice == "r":
            lastDirection = "East"
            x += 1

    elif lastDirection == "West":
        slowPrint("Můžete jít [z]pět, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "East"
            x += 1

        elif directionChoice == "r":
            lastDirection = "West"
            x -= 1

    return [x,y,lastDirection]

def roomTypeSW(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "South"
            y += 1
        
        elif directionChoice == "p":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "North":
        slowPrint("Můžete jít [z]pět, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "South"
            y += 1

        elif directionChoice == "l":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "East":
        slowPrint("Můžete jít [z]pět, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "West"
            x -= 1

        elif directionChoice == "p":
            lastDirection = "South"
            y += 1

    return [x,y,lastDirection]

def roomTypeNES(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "North"
            y -= 1
        
        elif directionChoice == "p":
            lastDirection = "East"
            x += 1

        elif directionChoice == "z":
            lastDirection = "South"
            y += 1

    elif lastDirection == "South":
        slowPrint("Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "l":
            lastDirection = "East"
            x += 1

        elif directionChoice == "r":
            lastDirection = "South"
            y += 1

    elif lastDirection == "West":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "East"
            x += 1

        elif directionChoice == "p":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "l":
            lastDirection = "South"
            y += 1

    elif lastDirection == "North":
        slowPrint("Můžete jít [z]pět, [r]ovně, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "South"
            y += 1

        elif directionChoice == "r":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "p":
            lastDirection = "East"
            x += 1

    return [x,y,lastDirection]

def roomTypeNEW(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, v[p]ravo, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "North"
            y -= 1
        
        elif directionChoice == "p":
            lastDirection = "East"
            x += 1

        elif directionChoice == "l":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "South":
        slowPrint("Můžete jít [z]pět, v[l]evo, nebo v[p]ravo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "l":
            lastDirection = "East"
            x += 1

        elif directionChoice == "p":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "West":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "East"
            x += 1

        elif directionChoice == "p":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "r":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "East":
        slowPrint("Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "West"
            x -= 1

        elif directionChoice == "r":
            lastDirection = "East"
            x += 1

        elif directionChoice == "l":
            lastDirection = "North"
            y -= 1

    return [x,y,lastDirection]

def roomTypeNSW(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, v[l]evo, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "North"
            y -= 1
        
        elif directionChoice == "l":
            lastDirection = "West"
            x -= 1

        elif directionChoice == "z":
            lastDirection = "South"
            y += 1

    elif lastDirection == "South":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "p":
            lastDirection = "West"
            x -= 1

        elif directionChoice == "r":
            lastDirection = "South"
            y += 1

    elif lastDirection == "East":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "West"
            x -= 1

        elif directionChoice == "l":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "p":
            lastDirection = "South"
            y += 1

    elif lastDirection == "North":
        slowPrint("Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "South"
            y += 1

        elif directionChoice == "r":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "l":
            lastDirection = "West"
            x -= 1

    return [x,y,lastDirection]

def roomTypeESW(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    if lastDirection == None:
        slowPrint("Můžete jít [r]ovně, v[p]ravo, nebo v[z]ad.\n")
        directionChoice = input()
        if directionChoice == "r":
            lastDirection = "East"
            x += 1
        
        elif directionChoice == "p":
            lastDirection = "South"
            y += 1

        elif directionChoice == "z":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "West":
        slowPrint("Můžete jít [z]pět, v[l]evo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "East"
            x += 1

        elif directionChoice == "l":
            lastDirection = "South"
            y += 1

        elif directionChoice == "r":
            lastDirection = "West"
            x -= 1

    elif lastDirection == "East":
        slowPrint("Můžete jít [z]pět, v[p]ravo, nebo [r]ovně.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "West"
            x -= 1

        elif directionChoice == "r":
            lastDirection = "East"
            x += 1

        elif directionChoice == "p":
            lastDirection = "South"
            y += 1

    elif lastDirection == "North":
        slowPrint("Můžete jít [z]pět, [r]ovně, nebo v[l]evo.\n")
        directionChoice = input()
        if directionChoice == "z":
            lastDirection = "South"
            y += 1

        elif directionChoice == "r":
            lastDirection = "North"
            y -= 1

        elif directionChoice == "l":
            lastDirection = "West"
            x -= 1

    return [x,y,lastDirection]

def roomTypeNESW(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni
    pass
    
    coordinates = getCoordinates(lastDirection)
    x = coordinates[0]
    y = coordinates[-1]

    return [x,y,lastDirection]

def roomOneSpawnOne(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni

    coordinates = roomTypeN(x,y,lastDirection)
    x = coordinates[0]
    y = coordinates[1]
    lastDirection = coordinates[2]
    return [x,y,lastDirection]

def roomTwo(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni

    coordinates = roomTypeSW(x,y,lastDirection)
    x = coordinates[0]
    y = coordinates[1]
    lastDirection = coordinates[2]
    return [x,y,lastDirection]

def roomThree(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni

    coordinates = roomTypeNEW(x,y,lastDirection)
    x = coordinates[0]
    y = coordinates[1]
    lastDirection = coordinates[2]
    return [x,y,lastDirection]

def roomFourExit(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni

    coordinates = roomTypeNS(x,y,lastDirection)
    x = coordinates[0]
    y = coordinates[1]
    lastDirection = coordinates[2]
    return [x,y,lastDirection]

def roomFive(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni

    coordinates = roomTypeEW(x,y,lastDirection)
    x = coordinates[0]
    y = coordinates[1]
    lastDirection = coordinates[2]
    return [x,y,lastDirection]

def roomSixSpawnTwo(xi,yi,lastDirectioni):
    x = xi
    y = yi
    lastDirection = lastDirectioni

    coordinates = roomTypeE(x,y,lastDirection)
    x = coordinates[0]
    y = coordinates[1]
    lastDirection = coordinates[2]
    return [x,y,lastDirection]

while True:
    lastDirection = None
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

roomPicking(x,y,lastDirection)

while False:
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
