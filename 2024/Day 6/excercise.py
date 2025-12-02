input = open('Day 6/Input.txt')

grid = []

for line in input:
    temp = []
    for char in line:
        if char != '\n':
            temp.append(char)
    grid.append(temp)

input.close()

def findPosition(grid):
    for i in range(0,len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '^':
                return i,j

def inRange(grid,i,j):
    if i < 0 or j < 0:
        return False
    try:
        grid[i][j]
        return True
    except:
        return False

def positionsAfterStep(direction,i,j):
    """
    direction -- 0,1,2,3 = N,O,S,W für Richtungen des Steps (Direction ändert sich pro Drehen immer mit +1 modulo 4)
    i,j -- Die Indices mit denen auf grid[i][j] zugegriffen wird. D.h. i größer zu machen ist Süden (analog negativ Norden) und
           j größer machen Osten (analog negativ Westen)
    """
    if direction == 0:
        return i-1,j
    if direction == 1:
        return i,j+1
    if direction == 2:
        return i+1,j
    if direction == 3:
        return i,j-1

i,j = findPosition(grid)
direction = 0

def visitedTiles(grid):
    res = 0
    for line in grid:
        for char in line:
            if char == "X":
                res += 1
    print(res)

def takeStep(grid,direction,i,j):
    ii, jj = positionsAfterStep(direction,i,j)
    if not inRange(grid,ii,jj):
        return(direction,ii,jj)
    if grid[ii][jj] == '#':
        newDirection = (direction + 1)%4
        return(newDirection,i,j)
    else:
        return(direction,ii,jj)

while inRange(grid,i,j):
    grid[i][j] = "X"
    print(i,j,grid[i][j])
    direction, i, j = takeStep(grid,direction,i,j)

visitedTiles(grid)