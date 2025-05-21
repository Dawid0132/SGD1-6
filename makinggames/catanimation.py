import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
cat1Img = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'
cat1x = 10
cat1y = 10
direction1 = 'down'




while True:  # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction1 == 'right':
        cat1x += 5
        if cat1x == 280:
            direction1 = 'up'
    elif direction1 == 'down':
        cat1y += 5
        if cat1y == 220:
            direction1 = 'right'
    elif direction1 == 'left':
        cat1x -= 5
        if cat1x == 10:
            direction1 = 'down'
    elif direction1 == 'up':
        cat1y -= 5
        if cat1y == 10:
            direction1 = 'left'

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(cat1Img, (cat1x, cat1y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
