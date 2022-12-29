import random

class game:
    def __init__(self):
        self.start()
    
    def generateGrid(self, x, y, difficulty):
        side = 0
        grid = []
        field = []
        difficulty = difficulty.lower()
        if(difficulty == "easy"):
            side = 8
        elif(difficulty == "medium"):
            side = 10
        elif(difficulty == "hard"):
            side = 12
        else:
            print("Your response was invalid, maybe there was a typo?")

        for count in range(side):
            count2 = 0
            temp1 = []
            temp2 = []
            for count2 in range(side):
                temp1.append(0)
                temp2.append("x")
            grid.append(temp1)
            field.append(temp2)
            count+=1
        mineLocations = self.addMines(grid, side, x, y)
        return grid, field, mineLocations, side

    def addMines(self, grid, side, xc, yc):
        mines = 0
        mineLocations = []
        while(mines < side):
            x = random.randint(0, side-1)
            y = random.randint(0, side-1)
            if(grid[x][y]):
                continue 
            if((x == xc and y == yc) or (x == xc and y == yc-1) or (x == xc and y == yc+1) 
               or (x == xc+1 and y == yc) or (x == xc+1 and y == yc+1) or (x == xc+1 and y == yc-1)
               or (x == xc-1 and y == yc) or (x == xc-1 and y == yc+1) or (x == xc-1 and yc == yc-1)):
                continue
            grid[x][y] = 1
            mineLocations.append((x, y))
            mines+=1
        return mineLocations

    def gameOver(self, field, mineLocations):
        for locations in mineLocations:
            field[locations[0]][locations[1]] = "O"
        print(field)

    def reveal(self, row, col, field, grid, visited, side, mines):
        if((row, col) not in visited and -1<row< side and -1<col< side and mines == 0):
            #mines = 0
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
            self.reveal(row-1, col, field, grid, visited, side, mines)
            self.reveal(row+1, col, field, grid, visited, side, mines)
            self.reveal(row, col+1, field, grid, visited, side, mines)
            self.reveal(row, col-1, field, grid, visited, side, mines)
            self.reveal(row+1, col+1, field, grid, visited, side, mines)
            self.reveal(row-1, col-1, field, grid, visited, side, mines)

    def checkRemaining(self, field, grid, side):
        unrevealed = 0
        for x in range(0, side):
            for y in range(0, side):
                if(field[x][y] == "x" and grid[x][y] == 0):
                    unrevealed += 1
        if(unrevealed == 0):
            print("You Win!")
            return 1

    def start(self):
        firstTurn = True
        run = True
        difficulty = input('What difficulty do you want to choose: "Easy", "Medium" or "hard"? ')
        visited = []
        while run:
            xcord = int(input("Choose X coordinate"))
            ycord = int(input("Choose Y coordinate")) 
            if(firstTurn):
                grid, field, mineLocations, side = self.generateGrid(xcord, ycord, difficulty)
                self.reveal(xcord, ycord, field, grid, visited, side, 0)
                if(self.checkRemaining(field, grid, side) == 1):
                    break
                firstTurn = False
            if(grid[xcord][ycord] == 1):
                print("You lose :(")
                self.gameOver(field, mineLocations)
                break
            else:
                self.reveal(xcord, ycord, field, grid, visited, side, 0)
                print(field)
                if(self.checkRemaining(field, grid, side) == 1):
                    break

game()
