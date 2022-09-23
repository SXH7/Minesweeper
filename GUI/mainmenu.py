from button import button
import pygame

playImage = pygame.image.load("GUI\Assets\Art\play.png")
quitImage = pygame.image.load("GUI\Assets\Art\quit.png")

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
    
    '''def makeButton(self, image, x, y, win):
        return button(image, x, y, win)'''

    def makeMenu(win):

        playButton = button(playImage, 350, 300, win)
        quitButton = button(quitImage, 350, 500, win)

        while True:
            position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.checkPress(position):
                        return True
                        break
                    if quitButton.checkPress(position):
                        pygame.quit()

            playButton.update(win)
            quitButton.update(win)
            pygame.display.update()