import pygame
import sys
import random
import math

pygame.init()
tileSize = 25
tilesX = 30
tilesY = 30
x = 0
y = 0
screenX = tileSize * tilesX
screenY = tileSize * tilesY
screen = pygame.display.set_mode((screenX, screenY))
mouseDown = False
placeHolder = 0
placeHolder2 = 0
emptyList = []
twoDList = []

def color(colorType):
    colors = {
        "sand": 'yellow',
        "blank": 'white',
        "metal": 'black',
        "rock": "darkgrey",
        "water": "water"
    }
    # I used chatgpt to help me, turns out I was returning the entire dictionary
    return colors.get(colorType, 'red')

def getAMat():
    material = random.randint(1,5)
    if material == 1:
        return "sand"
    elif material == 2:
        return "water"
    elif material == 3:
        return "metal"
    elif material == 4:
        return "rock"
    else:
        return "blank"

for i2 in range(tilesY):
    rowList = []
    for i in range(tilesX):
        rowList.append("blank")
    twoDList.append(rowList)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEMOTION:
        x, y = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouseDown = True
    
    if mouseDown:
        if x > 0 and x < screenX and y > 0 and y < screenY:
            twoDList[math.floor(y/tileSize)].pop(math.floor(x/tileSize))
            twoDList[math.floor(y/tileSize)].insert(math.floor(x/tileSize), "metal")        

    if event.type == pygame.MOUSEBUTTONUP:
        mouseDown = False

    screen.fill('lightblue')
    for placeHolder2 in range(0, screenY // tileSize):
        for placeHolder in range(0, screenX // tileSize):
            # Inner
            pygame.draw.rect(screen, color(twoDList[placeHolder2][placeHolder]), (placeHolder * tileSize, placeHolder2 * tileSize, tileSize, tileSize))
            # Boarder
            pygame.draw.rect(screen, "black", (placeHolder * tileSize, placeHolder2 * tileSize, tileSize, tileSize), tileSize//10)

    pygame.display.update()