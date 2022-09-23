import pygame
from button import button

# PYGAME SETUP

pygame.init()

win = pygame.display.set_mode((700, 700))
win.fill((60, 25, 60))
pygame.display.set_caption("Minesweeper")

playImage = pygame.image.load("GUI\Assets\Art\play.png")
quitImage = pygame.image.load("GUI\Assets\Art\quit.png")

playButton = button(playImage, 350, 300, win)
quitButton = button(quitImage, 350, 500, win)

class menu():
    def __init__(play, quit, x, play_y, quit_y):
        self.play = play
        self.quit = quit
        self.x = x
        self.play_y = play_y
        self.quit_y = self.quit_y
    
    def update(self):
        win.blit(self.play)
        win.blit(self.quit)

    #def placeButtons()

while True:

    position = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playButton.checkPress(position):
                print("Play")
            if quitButton.checkPress(position):
                pygame.quit() 

    playButton.update(win)
    quitButton.update(win)
    pygame.display.update()