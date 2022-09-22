import pygame

pygame.init()

window = pygame.display.set_mode((700, 700))
window.fill((60,25,60))
pygame.display.set_caption("Minesweeper")

menusprites = [pygame.image.load("Assets\Art\play.png"), pygame.image.load("Assets\Art\quit.png")]

def drawmenu():
    window.blit(menusprites[0], (150, 150))
    window.blit(menusprites[1], (150, 350))
    


run = True
while run:
    drawmenu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        '''if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for s in menusprites:
                if s.rect.collidepoint(pos):
                    print('e')'''
    pygame.display.update()

pygame.quit()