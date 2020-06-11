import numpy as np
# Notation:
# 0 = empty
# 1 = tent
# 2 = tree
# 3 = grass

grid = [
[2, 0, 0, 0, 0, 0, 0],
[0, 2, 0, 0, 2, 0, 2],
[0, 0, 0, 0, 0, 0, 0],
[0, 2, 0, 0, 0, 0, 2],
[0, 0, 0, 0, 0, 0, 0],
[0, 2, 0, 0, 2, 0, 2],
[0, 0, 0, 0, 0, 0, 0]
]

grid_col = [1,2,1,1,1,1,2]
grid_row = [1,2,2,0,1,2,1]

def isValid(i, j): #Checks if more tents are needed in col and row
    if grid[i].count(1) >= grid_row[i]:
        return False
    tents = 0
    for x in range(len(grid_row)):
        if grid[x][j] == 1:
            tents += 1
    if tents >= grid_col[j]:
        return False
    return True

def isGrass(x,y): #Checks if it can only be grass
    if x-1 >= 0 and grid[x-1][y] == 2:
        return False
    if x+1 < len(grid_row) and grid[x+1][y] == 2:
        return False
    if y+1 < len(grid_row) and grid[x][y+1] == 2:
        return False
    if y-1 >= 0 and grid[x][y-1] == 2:
        return False
    return True

def setGrass(): #Sets square if it can only be grass
    for i in range(len(grid_col)):
        for j in range(len(grid_col)):
            if grid[i][j] == 0 and isGrass(i,j):
                grid[i][j] = 3

def fillGrass(): #Fills all 0 with grass to complete puzzle
    for i in range(len(grid_col)):
        for j in range(len(grid_col)):
            if grid[i][j] == 0:
                grid[i][j] = 3

def noTentNeighbor(i, j): #Checks if tent has neighbor tents
    for x in range(-1,2):
        for y in range(-1,2):
            if(x+i >= len(grid_col)):
                continue
            if(y+j >= len(grid_col)):
                continue
            if(grid[x+i][y+j] == 1):
                    return False
    return True

def checkIfSolved(): #Checks if all tent conditions are met
    for x in range(len(grid_col)):
        if grid[x].count(1) != grid_row[x]:
            return False
    for y in range(len(grid_col)):
        tents = 0
        for x in range(len(grid_col)):
            if grid[x][y] == 1:
                tents += 1
        if tents != grid_col[y]:
            return False
    return True

def placeTents(): #Places tents Backtracking
    if checkIfSolved():
        return True
    for x in range(len(grid_col)):
        for y in range(len(grid_col)):
            if grid[x][y] == 0 and noTentNeighbor(x,y) and isValid(x,y) :
                grid[x][y] = 1
                if placeTents():
                    return True
                grid[x][y] = 0

def solve():
    setGrass()
    print(grid)
    placeTents()
    fillGrass()
    print(np.array(grid))

if __name__ == '__main__':
    solve()
