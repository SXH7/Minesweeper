import pygame

# PYGAME SETUP

pygame.init()

win = pygame.display.set_mode((700, 700))
win.fill((60, 25, 60))
pygame.display.set_caption("Minesweeper")



# MAINLOOP OF THE GAME
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    

    pygame.display.update()
