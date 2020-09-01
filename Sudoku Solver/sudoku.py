import pandas as pd 
import numpy as np
import pygame

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku Solver Visualization")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)



UNASSIGNED = 0
rank = 3
grid = [[5, 3, 0    , 0, 7, 0,     0, 0, 0],
        [6, 0, 0,     1, 9, 5,     0, 0, 0],
        [0, 9, 8,     0, 0, 0,     0, 6, 0],

        [8, 0, 0,     0, 6, 0,     0, 0, 3],
        [4, 0, 0,     8, 0, 3,     0, 0, 1],
        [7, 0, 0,     0, 2, 0,     0, 0, 6],

        [0, 6, 0,    0, 0, 0,      2, 8, 0],
        [0, 0, 0,    4, 1, 9,      0, 0, 5],
        [0, 0, 0,    0, 8, 0,      0, 7, 9]]

def isValid(row, col, number):
    global grid 
    global rank

    if(number != UNASSIGNED):
        for i in range(0, rank * rank):
            if(grid[row][i] == number):
                return False

        for j in range(0, rank * rank):
            if(grid[i][col] == number):
                return False

    #Für die Kästchen
    col = (col // rank) * rank #Für die Spalte
    row = (row  // rank) * rank #Für die Zeile

    for i in range(rank):
        for j in range(rank):
            if(grid[i+row][j+col] == number):
                return False

    return True

def solveSudoku(win):
    global grid
    global rank

    for row in range(rank * rank):
        for col in range(rank * rank):
            if(grid[row][col] == UNASSIGNED):
                for number in range(1, (rank * rank) + 1):
                    if isValid(row, col, number):
                        grid[row][col] = number
                        solveSudoku(win)
                        grid[row][col] = UNASSIGNED
                return
   # draw(win)
    print(np.matrix(grid))
    input("More?")


def draw(win):
    global grid
    w = 70
    x,y = 0,0

    font = pygame.font.SysFont(None, 100)
    

    for row in range(9):
        for col in range(9):

            rect = pygame.Rect(x,y,w,w)
            pygame.draw.rect(win,BLACK,rect)
            rect2 = pygame.Rect(x+2, y+2, w-1, w-1)
            pygame.draw.rect(win,WHITE,rect2)
            
            number = str(grid[row][col])
            screen_text = font.render(number, True, BLACK)
            win.blit(screen_text, rect2)
            pygame.display.flip()
            x = x + w
        y = y + w 
        x = 0





def main(win):
    pygame.init()
    global grid
    run = True
    while(run):
        draw(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        solveSudoku(win)

    pygame.quit()
    
                        



main(WIN)