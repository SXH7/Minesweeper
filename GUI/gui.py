import pygame
from mainmenu import menu

# PYGAME SETUP

pygame.init()

win = pygame.display.set_mode((700, 700))
win.fill((60, 25, 60))
pygame.display.set_caption("Minesweeper")

start = menu.makeMenu(win)
win.fill((0, 0, 0))



# MAINLOOP OF THE GAME
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
