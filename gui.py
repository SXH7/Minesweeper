import pygame

pygame.init()

window = pygame.display.set_mode((700, 700))
window.fill((60,25,60))
pygame.display.set_caption("Minesweeper")

def drawmenu():
    play = pygame.image.load("Assets\Art\play.png")
    quit = pygame.image.load("Assets\Art\quit.png")
    window.blit(play, (150, 150))
    window.blit(quit, (150, 350))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
    drawmenu()
    pygame.display.update()

pygame.quit()