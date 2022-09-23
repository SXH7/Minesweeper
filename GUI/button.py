class button():
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