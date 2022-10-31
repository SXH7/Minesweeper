import pygame
pygame.init()
pygame.font.init()
from random import randint

class gridgen():
    def make(cell, win, side):
        sidew = 70 if side == 8 else 50
        for row in range(side):
            for col in range (side):
                constr = row*sidew
                constc = col*sidew
                win.blit(cell, (60+constr, 75+constc))

    def generate(side):
        grid = []
        field = []
        for count in range(side):
            count2 = 0
            temp1 = []
            temp2 = []
            for count2 in range(side):
                temp1.append(0)
                temp2.append("X")
            grid.append(temp1)
            field.append(temp2)

        return field, grid

    def insert(grid, xc, yc, side):
        mines = 0
        minelocations = []
        while(mines < side):
            x = randint(0, side-1)
            y = randint(0, side-1)
            if(x == xc and y == yc):
                continue
            if(grid[x][y]):
                continue
            if((x == xc-1 and y == yc-1) or (x == xc-1 and y == yc) or (x == xc-1 and y == yc+1) or
               (x == xc and y == yc-1) or (x == xc and y == yc+1) or
               (x == xc+1 and y == yc-1) or (xc == xc+1 and y == yc) or (x == xc+1 and y == xc+1)):
               continue
            grid[x][y] = 1
            minelocations.append((x, y))
            mines+=1
        return minelocations

    def check(pos, grid):
        x = pos[0]-65
        y = pos[1]-75
        xnum = int(x/70)
        ynum = int(y/70)
        return ynum, xnum

    def update(field, grid, win, cell, revealed, font, side):
        for x in range(side):
            for y in range(side):
                xcord = 60+(y*70)
                ycord = 75+(x*70)
                if(field[x][y] == "X"):
                    win.blit(cell, (xcord, ycord))
                elif(grid[x][y] == 1):
                    win.blit(revealed, (xcord, ycord))
                    text = font.render("M", False, (0, 0, 0))
                    win.blit(text, (xcord+10, ycord))
                elif(field[x][y] > 0):
                    win.blit(revealed, (xcord, ycord))
                    num = field[x][y]
                    text = font.render(f"{num}", False, (0, 0, 0))
                    win.blit(text, (xcord+10, ycord))
                else:
                    win.blit(revealed, (xcord, ycord))

    def checkRemaining(field, grid, side, win, font):
        unrevealed = 0
        for x in range(0, side):
            for y in range(0, side):
                if(field[y][x] == "X" and grid[y][x] == 0):
                    unrevealed +=1
        if(unrevealed == 0):
            win.fill((60, 25, 60))
            text = font.render("You Win!", False, (0, 0, 0))
            win.blit(text, (225, 300))
