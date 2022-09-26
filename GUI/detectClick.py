import pygame

pygame.init()

class click():
    def checkBlock(side, pos):
        if(side == 8):
            sidewidth = 70
            x = pos[0]-65
            y = pos[1]-75
        xnum = int(x/sidewidth)
        ynum = int(y/sidewidth)
        return xnum, ynum