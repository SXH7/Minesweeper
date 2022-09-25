from random import randint
import pygame

cell = pygame.image.load("GUI\Assets\Art\cell.png")

class makeGrid():
    def __init__(self, side, grid):
        self.side = side
        self.grid = grid

    def addMines(side, grid):
        mines = 0
        mineLocations = []
        while(mines < side):
            x = randint(0, side-1)
            y = randint(0, side-1)
            if(grid[x][y] == 1):
                continue 
            grid[x][y] = 1
            mineLocations.append((x, y))
            mines+=1
        return mineLocations

    def generateGrid(side):
        grid = []
        field = []
        for count in range(side):
            count2 = 0
            temp1 = []
            temp2 = []
            for count2 in range(side):
                temp1.append(0)
                temp2.append("x")
            grid.append(temp1)
            field.append(temp2)
            count+=1
        return grid, field

    def drawGrid(side, win):
        if(side == 8):
            sidewidth = 70
        for row in range (side):
            for col in range (side):
                constr = row*sidewidth
                constc = col*sidewidth
                win.blit(cell, (65+constr, 75+constc))
            
