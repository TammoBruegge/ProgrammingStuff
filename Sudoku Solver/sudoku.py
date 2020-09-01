import pandas as pd 
import numpy as np 

UNASSIGNED = 0
rank = 3
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
#sudoku = np.matrix(grid)

def isValid(self,row, col, number):
    global grid 
    global rank
    print("Valid?")

    if(number != UNASSIGNED):
        for i in range(0, rank * rank, 1):
            if(grid[row][i] == number and i != col):
                return False

        for j in range(0, rank * rank, 1):
            if(grid[i][col] == number and i != row):
                return False

    #Für die Kästchen
    r = (row  // rank) * rank #Für die Zeile
    c = (col // rank) * rank #Für die Spalte

    for i in range(0,rank):
        for j in range(0,rank):
            if(grid[i+r][j+c] == number and row != i + r and col != j + c):
                return False

    return True

def solveSudoku():
    global grid
    global rank

    for row in range(rank * rank):
        for col in range(rank * rank):
            if(grid[row][col] == UNASSIGNED):
                for number in range(1, (rank * rank) + 1):
                    if isValid(row, col, number):
                        grid[row][col] = number
                        solveSudoku()
                        grid[row][col] = UNASSIGNED
                return
    print(np.matrix(grid))
    input("More?")




def solve(self,rank):
    global grid
    self.rank = rank
    
    for i in range(rank * rank):
        for j in range(rank * rank):
            field = grid[i][j]

            if(not(isValid(i,j,field))):
                print("Sudoku isnt valid!")
                exit()
    if(rank < 1):
        print("The Rank has to be min. 2")
        exit()

    solveSudoku()

solveSudoku()
# def __main__():
#     solveSudoku()
#    # solve(3)