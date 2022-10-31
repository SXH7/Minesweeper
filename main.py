import pygame
from Classes.makegrid import gridgen
from Classes.guiclasses import gui  

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((700, 700))
win.fill((60, 25, 60))
pygame.display.set_caption("Minesweeper")
font = pygame.font.Font("Assets\Font\VCR_OSD_MONO_1.001.ttf", 60)

cell = pygame.image.load("Assets\Art\cell.png")
revealed = pygame.image.load("Assets\Art\cellreveal.png")

def reveal(row, col, field, grid, visited, side, mines):
    if((row, col) not in visited and -1<row< side and -1<col< side and mines == 0):
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
        reveal(row-1, col, field, grid, visited, side, mines)
        reveal(row+1, col, field, grid, visited, side, mines)
        reveal(row, col+1, field, grid, visited, side, mines)
        reveal(row, col-1, field, grid, visited, side, mines)
        reveal(row+1, col+1, field, grid, visited, side, mines)
        reveal(row-1, col-1, field, grid, visited, side, mines)

def main():
    difficulty = gui.menu(win)
    sides = 8 if difficulty == 1 else (10 if difficulty == 2 else 12)
    win.fill((60, 25, 60))

    cell = pygame.image.load("Assets\Art\cell.png") 
    first = True
    field, grid = gridgen.generate(sides)
    visited = []
    gridgen.make(cell, win, sides)
    
    while True:
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:                    
                if(first):
                    pos = pygame.mouse.get_pos()
                    x, y = gridgen.check(pos, grid)
                    minelocations = gridgen.insert(grid, x, y, sides)
                    print(x, y)
                    print(grid)
                    print(minelocations)
                    reveal(x, y, field, grid, visited, sides, 0)
                    gridgen.update(field, grid, win, cell, revealed, font, sides)
                    first = False
                    continue

                x, y = gridgen.check(pos, grid)
                print(x, y)
                reveal(x, y, field, grid, visited, sides, 0)
                gridgen.update(field, grid, win, cell, revealed, font, sides)
                gridgen.checkRemaining(field, grid, sides, win, font)

        pygame.display.update()

main()
