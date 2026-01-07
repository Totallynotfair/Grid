import pygame
import sys
import random
import math
import time

pygame.display.init()
pygame.font.init()

#Too many variables
tileSize = 15
tilesX = 60
tilesY = 60
x = 0
y = 0
screenX = tileSize * tilesX
screenY = tileSize * tilesY
screen = pygame.display.set_mode((screenX, screenY))
mouseDown = False
checkingX = 0
checkingY = 0
drawingX = 0
drawingY = 0
borderThickness = 1
paintType = "sand"
emptyList = []
twoDList = []
sandColors = []
instructionOpen = True
font = pygame.font.Font(None, size=40)
instructionText = font.render("Left click to draw", False, "black")
instructionText2 = font.render("Space to exit the instructions", False, "black")
instructionText3 = font.render("You need to press different keys to change your material", False, "black")
instructionText4 = font.render("S:Sand W:Water R:Rock M:Metal B:Blank L:Lava", False, "black")
instructionText5 = font.render("Some combinations make new materials, like steam", False, "black")
paintSize = 3

#Makes them colorful
def color(colorType, X, Y):
    colors = {
        "sand": sandColors[Y][X],
        "blank": 'lightblue',
        "metal": 'black',
        "rock": 'darkgray',
        "water": 'blue',
        "lava": 'red',
        "steam": 'white',
    }
    # I used chatgpt to help me, turns out I was returning the entire dictionary
    return colors.get(colorType, 'red')

#Makes the entire grid random materials. Not used right now
def getAMat():
    material = random.randint(1,6)
    if material == 1:
        return "sand"
    elif material == 2:
        return "water"
    elif material == 3:
        return "metal"
    elif material == 4:
        return "rock"
    elif material == 5:
        return "lava"
    else:
        return "blank"

#Swaps the position of two blocks
def swapPos(X1, Y1, X2, Y2):
    item = twoDList[Y2][X2][0]
    twoDList[Y2][X2][0] = twoDList[Y1][X1][0]
    twoDList[Y1][X1][0] = item

#This is the entire movement code
def blockCheck(Y, X):
    # Asked chatgpt to help with this, because I forgot that if I pop a unit in a list, the rest of the list moves down.

            # -----SAND----- #

    if twoDList[Y][X][0] == "sand" and twoDList[Y][X][1] == 0:
        if twoDList[Y+1][X][0] == "blank":
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X][0] == "steam":
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X-1][0] == "blank" and twoDList[Y][X-1][0] == "blank":
            swapPos(X, Y, X-1, Y+1)
        elif twoDList[Y+1][X+1][0] == "blank" and twoDList[Y][X+1][0] == "blank":
            swapPos(X, Y, X+1, Y+1)
        elif twoDList[Y+1][X][0] == "water":  
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X][0] == "lava":  
            swapPos(X, Y, X, Y+1)

            # -----ROCK----- #

    elif twoDList[Y][X][0] == "rock" and twoDList[Y][X][1] == 0:
        if twoDList[Y+1][X][0] == "blank":
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X][0] == "water":
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X][0] == "steam":
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X][0] == "lava":
            swapPos(X, Y, X, Y+1)

            # -----WATER----- #

    elif twoDList[Y][X][0] == "water" and twoDList[Y][X][1] == 0:
        if twoDList[Y+1][X][0] == "blank":
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X][0] == "lava":
            twoDList[Y][X][0] = "steam"
        elif twoDList[Y+1][X][0] == "steam":
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X-1][0] == "blank" and twoDList[Y][X-1][0] == "blank":
            swapPos(X, Y, X-1, Y+1)
        elif twoDList[Y+1][X+1][0] == "blank" and twoDList[Y][X+1][0] == "blank":
            swapPos(X, Y, X+1, Y+1)
        elif twoDList[Y+1][X-1][0] == "steam" and twoDList[Y][X-1][0] == "steam":
            swapPos(X, Y, X-1, Y+1)
        elif twoDList[Y+1][X+1][0] == "steam" and twoDList[Y][X+1][0] == "steam":
            swapPos(X, Y, X+1, Y+1)
        elif twoDList[Y][X-1][0] == "blank":
            swapPos(X, Y, X-1, Y)
        elif twoDList[Y][X+1][0] == "blank":
            swapPos(X, Y, X+1, Y)
        elif twoDList[Y][X-1][0] == "steam":
            swapPos(X, Y, X-1, Y)
        elif twoDList[Y][X+1][0] == "steam":
            swapPos(X, Y, X+1, Y)

            # -----LAVA----- #

    elif twoDList[Y][X][0] == "lava" and twoDList[Y][X][1] == 0:
        if twoDList[Y+1][X][0] == "blank":
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X][0] == "water":
            twoDList[Y+1][X][0] = "rock"
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "steam":
            swapPos(X, Y, X, Y+1)
        elif twoDList[Y+1][X-1][0] == "blank" and twoDList[Y][X-1][0] == "blank":
            swapPos(X, Y, X-1, Y+1)
        elif twoDList[Y+1][X+1][0] == "blank" and twoDList[Y][X+1][0] == "blank":
            swapPos(X, Y, X+1, Y+1)
        elif twoDList[Y][X-1][0] == "blank":
            swapPos(X, Y, X-1, Y)
        elif twoDList[Y][X+1][0] == "blank":
            swapPos(X, Y, X+1, Y)

            # -----STEAM----- #

    if twoDList[Y][X][0] == "steam" and twoDList[Y][X][1] == 0:
        if twoDList[Y-1][X][0] == "blank":
            swapPos(X, Y, X, Y-1)
        elif twoDList[Y-1][X-1][0] == "blank":
            swapPos(X, Y, X-1, Y-1)
        elif twoDList[Y-1][X+1][0] == "blank":
            swapPos(X, Y, X+1, Y-1)
        elif twoDList[Y][X-1][0] == "blank":
            swapPos(X, Y, X-1, Y)
        elif twoDList[Y][X+1][0] == "blank":
            swapPos(X, Y, X+1, Y)

#Makes the grid as a 3d list
for i2 in range(tilesY + (borderThickness * 2)):
    rowList = []
    for i in range(tilesX + (borderThickness * 2)):
        if i2 == 0 or i2 == tilesY + (borderThickness):
            rowList.append(["metal", 0])
        elif i == 0 or i == tilesX + (borderThickness):
            rowList.append(["metal", 0])
        else:
            rowList.append(["blank", 0])
    twoDList.append(rowList)
    rowList = []
    for i in range(tilesX + (borderThickness * 2)):
        rowList.append((random.randint(205,215),random.randint(175,185),random.randint(135,145)))
    sandColors.append(rowList)

#Game loop
while True:
    
    #Menu
    while instructionOpen == True:
        screen.fill('lightblue')
        screen.blit(instructionText, (screenX/8, screenY/2-80))
        screen.blit(instructionText2, (screenX/8, screenY/2+130))
        screen.blit(instructionText3, (screenX/8, screenY/2-30))
        screen.blit(instructionText4, (screenX/8, screenY/2+30))
        screen.blit(instructionText5, (screenX/8, screenY/2+80))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    instructionOpen = False
        pygame.display.flip()

    #Closing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Checks the entire grid
    for checkingY in range(0, screenY // tileSize):
        for checkingX in range(0, screenX // tileSize):
            # Checks from bottom right to top left
            blockCheck((tilesY - checkingY), (tilesX - checkingX))          

    #Finds the mouse position
    if event.type == pygame.MOUSEMOTION:
        x, y = pygame.mouse.get_pos()

    #Changes the material
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        paintType = "sand"
    elif keys[pygame.K_w]:
        paintType = "water"
    elif keys[pygame.K_r]:
        paintType = "rock"
    elif keys[pygame.K_m]:
        paintType = "metal"
    elif keys[pygame.K_b]:
        paintType = "blank"
    elif keys[pygame.K_l]:
        paintType = "lava"

    #Bigger paint of materials
    if mouseDown:
        if x > 0 and x < screenX and y > 0 and y < screenY:
            for i in range(paintSize):
                for i2 in range(paintSize):
                    twoDList[math.floor(y/tileSize)+(i-paintSize//2)][math.floor(x/tileSize)+(i2-paintSize//2)].pop(0)
                    twoDList[math.floor(y/tileSize)+(i-paintSize//2)][math.floor(x/tileSize)+(i2-paintSize//2)].insert(0, paintType)


    #Paints the materials
    # if mouseDown:
    #     if x > 0 and x < screenX and y > 0 and y < screenY:
    #         twoDList[math.floor(y/tileSize)+1][math.floor(x/tileSize)+1].pop(0)
    #         twoDList[math.floor(y/tileSize)+1][math.floor(x/tileSize)+1].insert(0, paintType)
    buttons = pygame.mouse.get_pressed()
    if not any(buttons):
        mouseDown = False
    else:
        mouseDown = True

    #Prints the entire screen
    screen.fill('lightblue')
    for drawingY in range(0, screenY // tileSize):
        for drawingX in range(0, screenX // tileSize):
            # Inner
            pygame.draw.rect(screen, color(twoDList[drawingY+borderThickness][drawingX+borderThickness][0], drawingX, drawingY), (drawingX * tileSize, drawingY * tileSize, tileSize, tileSize))
            # Boarder
            #pygame.draw.rect(screen, "black", (drawingX * tileSize, drawingY * tileSize, tileSize, tileSize), tileSize // 10)
    
    #Delay if we wanted
    #time.sleep(0.05)

    pygame.display.update()