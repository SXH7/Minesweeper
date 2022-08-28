import random
import pygame

class game:
    def __init__(self):
        global grid
        global field 
        grid = [[0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

        field = [["x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x"]]
        self.setup()
        self.start()
        
    def setup(self):
        global mineLocations
        mines = 0
        mineLocations = []
        while(mines<=4):
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if(grid[x][y] == 1):
                continue 
            grid[x][y] = 1
            mineLocations.append((x, y))
            mines+=1
        print(grid)

    def gameOver(self):
        for locations in mineLocations:
            field[locations[0]][locations[1]] = "O"
        print(field)
        

    def start(self):
        win = True
        while win:
            print(field)
            xcord = int(input("Choose X coordinate"))
            ycord = int(input("Choose Y coordinate")) 
            if(grid[xcord][ycord] == 1):
                print("You lose :(")
                self.gameOver()
                break
                

game()