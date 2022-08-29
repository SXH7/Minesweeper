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

    def countMines(self, x, y):
        adj = 0
        count = 0
        xcords = [x-1, x-1, x-1, x, x, x, x+1, x+1, x+1]
        ycords = [y-1, y, y+1, y-1, y, y+1, y-1, y, y+1]
        while(count < 9):
            if(xcords[count] < 0 or ycords[count] < 0):
                count+=1
                continue
            if(grid[xcords[count]][ycords[count]] == 1):
                adj+=1
            count+=1
        print(adj)

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
            else:
                self.countMines(xcord, ycord)
                

game()