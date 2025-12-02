import copy

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

def takeStep(grid,direction,i,j):
    ii, jj = positionsAfterStep(direction,i,j)
    if not inRange(grid,ii,jj):
        return(direction,ii,jj)
    if grid[ii][jj] == '#':
        newDirection = (direction + 1)%4
        return(newDirection,i,j)
    else:
        return(direction,ii,jj)

# Problem: Wenn man sich immer nur die letzte Direction merkt mit der man schon da war, bleibt man in einer Endlos-Schleife hängen,
# Wenn der Loop jedes seiner Felder in einem Durchlauf mehrmals in der selben Richtung besucht (weiß gerade nicht, ob das möglich ist, aber irgendwo her muss meine Endlos-Schleife kommen)
def hasLoop(grid,i,j):
    visitedPositions = {}
    direction = 0
    while inRange(grid,i,j):
        #Aktuelle Position mit Richtung merken
        if (i,j) not in visitedPositions:
            visitedPositions[(i,j)] = [direction]
        else:
            visitedPositions[(i,j)].append(direction)

        #Einen Schritt/eine Richtungsänderung machen
        direction, i, j = takeStep(grid,direction,i,j)

        #Prüfen, ob wir uns auf einem Loop befinden
        try:
            if direction in visitedPositions[(i,j)]:
                return True
        except:
            continue
    
    #Wenn der while-loop endet, ohne das returned wurde, enthält das Feld keinen Loop
    return False

#Die Funktion braucht schon ein bisschen zum laufen, aber das Ergebnis ist richtig :D Hauptsache durch sag ich immer
def findNumberOfLoops(grid):
    res = 0
    counter = 0
    possibleOptions = len(grid)*len(grid[0])
    numberRows = len(grid)
    i,j = findPosition(grid)
    for x in range(0,len(grid)):
        print(f"Testing row {x} from {numberRows}")
        for y in range(0,len(grid[x])):
            counter += 1
            if grid[x][y] == '.':
                newGrid = copy.deepcopy(grid)
                newGrid[x][y] = "#"
                #print(f"Testing option {counter} from {possibleOptions}")
                if hasLoop(newGrid,i,j):
                    res += 1
    print(res)

findNumberOfLoops(grid)