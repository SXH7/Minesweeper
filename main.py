
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
mineLocations = []
while(mines<=4):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    if(grid[x, y] == 1):
        continue 
    grid[x, y] = 1
    mineLocations.append((x, y))
    mines+=1

win = True

field = numpy.array([["x", "x", "x", "x", "x"],
                    ["x", "x", "x", "x", "x"],
                    ["x", "x", "x", "x", "x"],
                    ["x", "x", "x", "x", "x"],
                    ["x", "x", "x", "x", "x"]])

def countMines(cords):
    total = 0
    x = cords[0]
    y = cords[1]
    coords = [
        {"x": x-1,  "y": y-1},  
        {"x": x-1,  "y": y},   
        {"x": x-1,  "y": y+1}, 
        {"x": x,    "y": y-1}, 
        {"x": x,    "y": y+1}, 
        {"x": x+1,  "y": y-1}, 
        {"x": x+1,  "y": y},   
        {"x": x+1,  "y": y+1}, 
    ]
    for n in coords:
        try:
            if((grid[n["x"]][n["y"]]) == 1):
                total+=1
        except KeyError:
            pass
    return total

def showMines():
    for location in mineLocations:
        field[location] = "O"
    print(field)

def gameOver():
    print("You clicked on a mine :<")
    showMines()

while win:
    print(field)
    turn = []
    print(grid)
    for x in range(2):
        turn.append(int(input("enter coordinate:")))

    #when game over
    if((grid[turn[0]])[turn[1]]):
        gameOver()
        break

    else:
        print(grid)    #only for testing
        print(countMines(turn))
        
