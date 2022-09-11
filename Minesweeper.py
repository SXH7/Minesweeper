import random
import pygame

class game:
    def __init__(self):
        self.start()
    
    def generateGrid(self):
        side = 0
        grid = []
        field = []
        difficulty = input('What difficulty do you want to choose: "Easy", "Medium" or "hard"?')
        difficulty = difficulty.lower()
        if(difficulty == "easy"):
            side = 8
        elif(difficulty == "medium"):
            side = 10
        elif(difficulty == "hard"):
            side = 12
        else:
            print("Your response was invalid, maybe there was a typo?")

        count = 0
        while(count < side):
            count2 = 0
            temp1 = []
            temp2 = []
            while(count2 < side):
                temp1.append(0)
                temp2.append("x")
                count2+=1
            grid.append(temp1)
            field.append(temp2)
            count+=1
        mineLocations = self.addMines(grid, side)
        return grid, field, mineLocations

    def addMines(self, grid, side):
        mines = 0
        mineLocations = []
        while(mines < side):
            x = random.randint(0, side-1)
            y = random.randint(0, side-1)
            if(grid[x][y] == 1):
                continue 
            grid[x][y] = 1
            mineLocations.append((x, y))
            mines+=1
        print(grid)                       # FOR DEVTEST ONLY
        return mineLocations

    def gameOver(self, field, mineLocations):
        for locations in mineLocations:
            field[locations[0]][locations[1]] = "O"
        print(field)

    def reveal(self, row, col, field, grid, visited):
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
            self.reveal(row-1, col, field, grid, visited)
            self.reveal(row+1, col, field, grid, visited)
            self.reveal(row, col+1, field, grid, visited)
            self.reveal(row, col-1, field, grid, visited)
            self.reveal(row+1, col+1, field, grid, visited)
            self.reveal(row-1, col-1, field, grid, visited)
        else:
            pass

    def start(self):
        grid, field, mineLocations = self.generateGrid()
        visited = []
        win = True
        while win:
            print(field)
            xcord = int(input("Choose X coordinate"))
            ycord = int(input("Choose Y coordinate")) 
            if(grid[xcord][ycord] == 1):
                print("You lose :(")
                self.gameOver(field, mineLocations)
                break
            else:
                self.reveal(xcord, ycord, field, grid, visited)
                
game()
