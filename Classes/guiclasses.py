import pygame
pygame.init()
pygame.font.init()

font = pygame.font.Font("Assets\Font\VCR_OSD_MONO_1.001.ttf", 60)

class buttons():
    def __init__(self, image, x, y, win):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center =(self.x, self.y))
        self.win = win

    def update(self, win):
        win.blit(self.image, self.rect)

    def checkPress(self, position):
        if(position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)):
            return True
        else:
            return False

class gui():

    def menu(win):

        dif = 1

        play = pygame.image.load("Assets/Art/play.png")
        left = pygame.image.load("Assets\Art\left.png")
        right = pygame.image.load("Assets\Art\\right.png")
        easy = pygame.image.load("Assets\Art\\easy.png")
        medium = pygame.image.load("Assets\Art\medium.png")
        hard = pygame.image.load("Assets\Art\hard.png")

        playButton = buttons(play, 350, 275, win)
        leftButton = buttons(left, 180, 475, win)
        rightButton = buttons(right, 525, 475, win)


        playButton.update(win)
        leftButton.update(win)
        rightButton.update(win)

        win.blit(easy, (153 , 400))

        pygame.display.update()
        start = False
        while True:    
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                if(event.type == pygame.MOUSEBUTTONDOWN):        
                    pos = pygame.mouse.get_pos()
                    if(playButton.checkPress(pos)):
                        start = True
                    if(leftButton.checkPress(pos)):
                        dif = dif-1 if dif > 1 else 1
                        win.blit(easy, (153 , 400)) if dif == 1 else (win.blit(medium, (153 , 400)) if dif == 2 else win.blit(hard, (153 , 400)))
                        print(dif)
                    if(rightButton.checkPress(pos)):
                        dif = dif+1 if dif < 3 else 3
                        win.blit(easy, (153 , 400)) if dif == 1 else (win.blit(medium, (153 , 400)) if dif == 2 else win.blit(hard, (153 , 400)))
                        print(dif)
            
            pygame.display.update()
                    
            if start:
                break
        return dif

