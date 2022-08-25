
#import statements
#import pygame
import random
import numpy

'''#initialization and variables
pygame.init()
WINDOW = pygame.display.set_mode((500, 500))
SIDE = 10
CELL = pygame.image.load()


run = True

while run:
    '''


grid = numpy.array([[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])

mines = 0
while(mines<=4):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    if(grid[x, y] == 1):
        continue 
    grid[x, y] = 1
    mines+=1


