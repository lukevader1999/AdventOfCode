grid = []
input = open("Day 4/input.txt")
for line in input:
    newLine = []
    for char in line:
            newLine.append(char)
    grid.append(line)

#print(len(grid))
#print(len(grid[0]))

#for line in grid:
#    if len(line) == 141:
#        print('Yes')
#    else:
#        print(len(line))

def outOfBounds(i,j):
      if i < 0 or j < 0:
            return True
      if i >= len(grid):
            return True
      if j >= len(grid[i]):
            return True
      return False

def rightStep(i,j):
      return (i+1,j)

def leftStep(i,j):
      return (i-1,j)

def downStep(i,j):
      return (i,j+1)

def upStep(i,j):
      return (i,j-1)

def diag1Step(i,j):
      return (i+1,j+1)

def diag2Step(i,j):
      return (i+1,j-1)

def diag3Step(i,j):
      return (i-1,j+1)

def diag4Step(i,j):
      return (i-1,j-1)

stepFunctions = [rightStep, leftStep, downStep, upStep, diag1Step, diag2Step, diag3Step, diag4Step]

def isXMASinSpecificDirection(i,j,stepFunction):
    searchWord = "XMAS"
    counter = 0
    while counter < len(searchWord):
        if outOfBounds(i,j):
              return False
        if grid[i][j] != searchWord[counter]:
                return False
        i,j = stepFunction(i,j)
        counter += 1
    return True
    
res = 0
for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):  
          if grid[i][j] == "X":
                for stepFunction in stepFunctions:
                      if isXMASinSpecificDirection(i,j,stepFunction):
                            res += 1
print(res)