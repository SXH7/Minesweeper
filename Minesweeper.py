import random
import pygame

class game:
    def __init__(self):
        global grid
        global field
        global visited
        visited = []
        grid = ([0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0])

        field = [["x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x"],]
        self.setup()
        self.start()
        
    def setup(self):
        global mineLocations
        mines = 0
        mineLocations = []
        while(mines<=7):
            x = random.randint(0, 7)
            y = random.randint(0, 7)
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

    def reveal(self, row, col):
        if((row, col) not in visited and -1<row<5 and -1<col<5 and grid[row][col] != 1):
            mines = 0
            visited.append((row, col))
            count = 0
            xcords = [row-1, row-1, row-1, row, row, row, row+1, row+1, row+1]
            ycords = [col-1, col, col+1, col-1, col, col+1, col-1, col, col+1]
            while(count < 9):
                if(xcords[count] < 0 or ycords[count] < 0):
                    count+=1
                    continue
                try:
                    if(grid[xcords[count]][ycords[count]] == 1):
                        mines+=1
                except IndexError:
                    pass
                count+=1
            
            field[row][col] = mines
            print(mines)
            self.reveal(row-1, col)
            self.reveal(row+1, col)
            self.reveal(row, col+1)
            self.reveal(row, col-1)
            self.reveal(row+1, col+1)
            self.reveal(row-1, col-1)
        else:
            pass


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
                self.reveal(xcord, ycord)
                
game()
