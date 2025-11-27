import pygame
import sys
import random
import math
import time

pygame.display.init()

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

def color(colorType, X, Y):
    colors = {
        "sand": sandColors[Y][X],
        "blank": 'lightblue',
        "metal": 'black',
        "rock": 'lightgray',
        "water": 'blue',
        "lava": 'red',
        "steam": 'white',
        "tree": 'darkgreen',
        "coal": 'darkgray',
        "oil": 'darkred',
        "fire": 'orange'
    }
    # I used chatgpt to help me, turns out I was returning the entire dictionary
    return colors.get(colorType, 'red')

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

def blockCheck(Y, X):
    # Asked chatgpt to help with this, because I forgot that if I pop a unit in a list, the rest of the list moves down.
    if twoDList[Y][X][0] == "sand":
        if twoDList[Y+1][X][0] == "blank":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "steam":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "steam"
        elif twoDList[Y+1][X-1][0] == "blank" and twoDList[Y][X-1][0] == "blank":
           twoDList[Y+1][X-1][0] = twoDList[Y][X][0]
           twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X+1][0] == "blank" and twoDList[Y][X+1][0] == "blank":
           twoDList[Y+1][X+1][0] = twoDList[Y][X][0]
           twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "water":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "water"
    elif twoDList[Y][X][0] == "rock":
        if twoDList[Y+1][X][0] == "blank":
           twoDList[Y+1][X][0] = twoDList[Y][X][0]
           twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "water":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "water"
        elif twoDList[Y+1][X][0] == "steam":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "steam" 
    elif twoDList[Y][X][0] == "water":
        if twoDList[Y+1][X][0] == "blank":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "lava":
            twoDList[Y][X][0] = "steam"
        elif twoDList[Y+1][X][0] == "steam":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "steam"
        elif twoDList[Y+1][X][0] == "oil":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "oil"
        elif twoDList[Y+1][X-1][0] == "oil" and twoDList[Y][X-1][0]:
            twoDList[Y+1][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "oil"
        elif twoDList[Y+1][X+1][0] == "oil" and twoDList[Y][X+1][0]:
            twoDList[Y+1][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "oil"
        elif twoDList[Y][X-1][0] == "oil":
            twoDList[Y][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "oil"
        elif twoDList[Y][X+1][0] == "oil":
            twoDList[Y][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "oil"
        elif twoDList[Y+1][X-1][0] == "blank" and twoDList[Y][X-1][0] == "blank":
            twoDList[Y+1][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X+1][0] == "blank" and twoDList[Y][X+1][0] == "blank":
            twoDList[Y+1][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y][X-1][0] == "blank":
            twoDList[Y][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y][X+1][0] == "blank":
            twoDList[Y][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
    elif twoDList[Y][X][0] == "lava":
        if twoDList[Y+1][X][0] == "blank":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "water":
            twoDList[Y+1][X][0] = "rock"
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "steam":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "steam"
        elif twoDList[Y+1][X-1][0] == "blank" and twoDList[Y][X-1][0] == "blank":
            twoDList[Y+1][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X+1][0] == "blank" and twoDList[Y][X+1][0] == "blank":
            twoDList[Y+1][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y][X-1][0] == "blank":
            twoDList[Y][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y][X+1][0] == "blank":
            twoDList[Y][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
    if twoDList[Y][X][0] == "steam":
        if twoDList[Y-1][X][0] == "blank":
            twoDList[Y-1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y-1][X-1][0] == "blank":
            twoDList[Y-1][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y-1][X+1][0] == "blank":
            twoDList[Y-1][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y][X-1][0] == "blank":
            twoDList[Y][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y][X+1][0] == "blank":
            twoDList[Y][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
    elif twoDList[Y][X][0] == "tree":
        if twoDList[Y+1][X][0] == "blank":
           twoDList[Y+1][X][0] = twoDList[Y][X][0]
           twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "steam":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "steam"
        elif twoDList[Y+1][X][0] == "blank":
           twoDList[Y+1][X][0] = twoDList[Y][X][0]
           twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "lava":
           twoDList[Y][X][0] = "coal"
    elif twoDList[Y][X][0] == "coal":
        if twoDList[Y+1][X][0] == "blank":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "steam":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "steam"
        elif twoDList[Y+1][X-1][0] == "blank" and twoDList[Y][X-1][0] == "blank":
           twoDList[Y+1][X-1][0] = twoDList[Y][X][0]
           twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X+1][0] == "blank" and twoDList[Y][X+1][0] == "blank":
           twoDList[Y+1][X+1][0] = twoDList[Y][X][0]
           twoDList[Y][X][0] = "blank"
    elif twoDList[Y][X][0] == "oil":
        if twoDList[Y+1][X][0] == "blank":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X][0] == "steam":
            twoDList[Y+1][X][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "steam"
        elif twoDList[Y+1][X-1][0] == "blank" and twoDList[Y][X-1][0] == "blank":
            twoDList[Y+1][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y+1][X+1][0] == "blank" and twoDList[Y][X+1][0] == "blank":
            twoDList[Y+1][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y][X-1][0] == "blank":
            twoDList[Y][X-1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"
        elif twoDList[Y][X+1][0] == "blank":
            twoDList[Y][X+1][0] = twoDList[Y][X][0]
            twoDList[Y][X][0] = "blank"

for i2 in range(tilesY + (borderThickness * 2)):
    rowList = []
    for i in range(tilesX + (borderThickness * 2)):
        if i2 == 0 or i2 == tilesY + (borderThickness):
            rowList.append(["metal"])
        elif i == 0 or i == tilesX + (borderThickness):
            rowList.append(["metal"])
        else:
            rowList.append(["blank"])
    twoDList.append(rowList)
    rowList = []
    for i in range(tilesX + (borderThickness * 2)):
        rowList.append((random.randint(205,215),random.randint(175,185),random.randint(135,145)))
    sandColors.append(rowList)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for checkingY in range(0, screenY // tileSize):
        for checkingX in range(0, screenX // tileSize):
            # Checks from bottom right to top left
            blockCheck((tilesY - checkingY), (tilesX - checkingX))

    if event.type == pygame.MOUSEMOTION:
        x, y = pygame.mouse.get_pos()

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
    elif keys[pygame.K_t]:
        paintType = "tree"
    elif keys[pygame.K_o]:
        paintType = "oil"

    if mouseDown:
        if x > 0 and x < screenX and y > 0 and y < screenY:
            twoDList[math.floor(y/tileSize)+1][math.floor(x/tileSize)+1].pop(0)
            twoDList[math.floor(y/tileSize)+1][math.floor(x/tileSize)+1].insert(0, paintType)

    buttons = pygame.mouse.get_pressed()

    if not any(buttons):
        mouseDown = False
    else:
        mouseDown = True

    screen.fill('lightblue')
    for drawingY in range(0, screenY // tileSize):
        for drawingX in range(0, screenX // tileSize):
            # Inner
            pygame.draw.rect(screen, color(twoDList[drawingY+borderThickness][drawingX+borderThickness][0], drawingX, drawingY), (drawingX * tileSize, drawingY * tileSize, tileSize, tileSize))
            # Boarder
            #pygame.draw.rect(screen, "black", (drawingX * tileSize, drawingY * tileSize, tileSize, tileSize), tileSize // 10)
    
    #time.sleep(0.05)

    pygame.display.update()