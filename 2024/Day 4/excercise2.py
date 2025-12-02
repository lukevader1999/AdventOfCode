grid = []
input = open("Day 4/input.txt")
for line in input:
    newLine = []
    for char in line:
            newLine.append(char)
    grid.append(line)

def isAanXMAS(i,j):
    char1 = grid[i+1][j+1]
    char2 = grid[i-1][j-1]

    char3 = grid[i+1][j-1]
    char4 = grid[i-1][j+1]

    chars = [char1, char2, char3, char4]

    for char in chars:
        if char not in ['M','S']:
              return False
    if char1 == char2:
          return False
    if char3 == char4:
          return False    
    
    return True


res = 0
for i in range(1,len(grid)-1):
    for j in range(1,len(grid[i])-1):  
          if grid[i][j] == "A":
                try: 
                     if isAanXMAS(i,j) == True:
                          res += 1
                except:
                    continue
        
print(res)