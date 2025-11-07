import pygame
import sys
import random

pygame.init()
tileSize = 50
tilesX = 20
tilesY = 20
screenX = tileSize * tilesX
screenY = tileSize * tilesY
screen = pygame.display.set_mode((screenX, screenY))
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
        "water": "blue"
    }
    # I used chatgpt to help me, turns out I was returning the entire dictionary
    return colors.get(colorType, 'red')

def getAMat():
    material = random.randint(1,5)
    if material == 1:
        return "sand"
    elif material == 2:
        return "blank"
    elif material == 3:
        return "metal"
    elif material == 4:
        return "rock"
    elif material == 5:
        return "water"

for i2 in range(tilesY):
    rowList = []
    for i in range(tilesX):
        rowList.append(getAMat())
    twoDList.append(rowList)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('lightblue')
    for placeHolder2 in range(0, screenY // tileSize):
        for placeHolder in range(0, screenX // tileSize):
            # Inner
            pygame.draw.rect(screen, color(twoDList[placeHolder2][placeHolder]), (placeHolder * tileSize, placeHolder2 * tileSize, tileSize, tileSize))
            # Boarder
            pygame.draw.rect(screen, "black", (placeHolder * tileSize, placeHolder2 * tileSize, tileSize, tileSize), 5)

    pygame.display.update()