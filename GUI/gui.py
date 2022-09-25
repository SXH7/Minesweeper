import pygame
from mainmenu import menu
from grid import makeGrid
#from detectClick import click

# PYGAME SETUP

pygame.init()

win = pygame.display.set_mode((700, 700))
win.fill((60, 25, 60))
pygame.display.set_caption("Minesweeper")

start = menu.makeMenu(win)
win.fill((60, 25, 60))
difficulty = menu.difficulty(win)
win.fill((60, 25, 60))

grid, field = makeGrid.generateGrid(difficulty)
minesLocations = makeGrid.addMines(difficulty, grid)
print(grid)
print(minesLocations)

makeGrid.drawGrid(difficulty, win)

# MAINLOOP OF THE GAME
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #if event.type == pygame.MOUSEBUTTONDOWN:
            
    


    pygame.display.update()
