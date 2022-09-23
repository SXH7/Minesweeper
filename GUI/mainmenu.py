from button import button
import pygame

playImage = pygame.image.load("GUI\Assets\Art\play.png")
quitImage = pygame.image.load("GUI\Assets\Art\quit.png")
easy = pygame.image.load("GUI\Assets\Art\easy.png")
medium = pygame.image.load("GUI\Assets\Art\medium.png")
hard = pygame.image.load("GUI\Assets\Art\hard.png")

pygame.font.init()
font = pygame.font.Font("GUI\Assets\Font\VCR_OSD_MONO_1.001.ttf", 60)

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

    def difficulty(win):
        text = font.render("Choose difficulty", False, (0, 0, 0))
        win.blit(text, (60, 50))
        easyButton = button(easy, 350, 250, win)
        mediumButton = button(medium, 350, 400, win)
        hardButton = button(hard, 350, 550, win)
        easyButton.update(win)
        mediumButton.update(win)
        hardButton.update(win)
        pygame.display.update()
        while True:
            position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easyButton.checkPress(position):
                        return 8
                    if mediumButton.checkPress(position):
                        return 10
                    if hardButton.checkPress(position):
                        return 12


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