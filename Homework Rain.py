import pygame, sys
from pygame.locals import*

import random

pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640,480))

screenWidth, screenHeight = pygame.display.get_surface().get_size()
screenColour = (255,255,255)

rain = []

class Raindrop:
    def __init__(self):
        self.raindropColour =(7,117+random.randint(0,20),119+random.randint(0,20))
        self.raindropPosX = random.randint(0,screenWidth)
        self.raindropPosY = 0
        self.raindropSpeed = (random.random()+0.1)*2

    def move(self):
        self.raindropPosY += self.raindropSpeed

    def draw (self):
        pygame.draw.circle(screen,(self.raindropColour),(int(self.raindropPosX),int(self.raindropPosY)),2,0)

    def delete (self, drops):
        if (self.raindropPosY > screenHeight):
            rain.remove(drops)



circlePosX = 100
circlePosY = 200
circleColour = (255,0,0)


while 1:

    pressedKey=pygame.key.get_pressed()
    
    if pressedKey[K_RIGHT]:
        circlePosX = min(circlePosX+0.2,screenWidth)
    if pressedKey[K_LEFT]:
        circlePosX = max(circlePosX-0.2,0)
    if pressedKey[K_UP]:
        circlePosY = max(circlePosY-0.2,0)
    if pressedKey[K_DOWN]:
        circlePosY = min(circlePosY+0.2,screenHeight)

    if pressedKey[K_1]:
        circleColour = (255,0,0)
    if pressedKey[K_2]:
        circleColour = (0,255,0)
    if pressedKey[K_3]:
        circleColour = (0,0,255)


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()



    screen.fill(screenColour)

    pygame.draw.circle(screen,(circleColour),(int(circlePosX),int(circlePosY)),20,0)

    raindrop = Raindrop()
    rain.append(raindrop)
    
    for drops in rain:
        drops.move()
        drops.delete(drops)
        drops.draw()

    pygame.display.update()
