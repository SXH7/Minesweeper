import random
import pygame

class game:
    def __init__(self):
        global grid
        global field
        global check
        check = []
        grid = ([0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0])

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
            try:
                if(grid[xcords[count]][ycords[count]] == 1):
                    adj+=1
            except IndexError:
                pass
            count+=1
        return adj

    def reveal(self, row, col):
        rows = [row-1, row-1, row-1, row, row, row, row+1, row+1, row+1]
        cols = [col-1, col, col+1, col-1, col, col+1, col-1, col, col+1]
        if [row, col] not in check:
            check.append([row, col])
            if(self.countMines(row, col) == 0):
                field[row][col] = "0"
                count = 0
                while(count <9):
                    if(rows[count] < 0 or cols[count] < 0):
                        count+=1
                        continue
                    try:
                        self.countMines(rows[count], cols[count])
                    except IndexError:
                        pass
                    count+=1
            else:
                field[row][col] = self.countMines(row, col)



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
                self.reveal(xcord, ycord)
                

game()