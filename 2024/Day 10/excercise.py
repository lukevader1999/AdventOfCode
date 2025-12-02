class gridNode():
    def __init__(self, height):
        self.height = height
        self.ninesReachable = []
        self.alreadyVisited = False

class grid():

    def __init__(self):
        self.grid = []
        input = open("Day 10/input.txt")
        for line in input:
            gridLine = []
            for point in line:
                if point == "\n":
                    continue
                gridLine.append(gridNode(int(point)))
            self.grid.append(gridLine)

        self.trailheads = []
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y].height == 0:
                    self.trailheads.append([x,y])
        
        self.neighbourCoords = [[-1,0], [1,0], [0,-1], [0,1]]
    
    def printGrid(self):
        for line in self.grid:
            for point in line:
                print(point.height, end = " ")
            print(" ")
    
    def coordsInRange(self,x,y):
        if x<0 or y<0:
            return False
        if x > len(self.grid)-1:
            return False
        if y > len(self.grid[x])-1:
            return False
        return True

    def visitNeighbours(self, x,y):
        point = self.grid[x][y]
        allReachables = []

        if point.height == 9:
            point.ninesReachable.append([x,y])
            point.alreadyVisited = True
            return

        for coords in self.neighbourCoords:

            i = x + coords[0]
            j = y + coords[1]

            if self.coordsInRange(i,j):
                neighbour = self.grid[i][j]
            else:
                continue

            if neighbour.height != point.height + 1:
                continue

            if neighbour.alreadyVisited:
                allReachables = allReachables + neighbour.ninesReachable
                continue

            self.visitNeighbours(i,j)
            allReachables = allReachables + neighbour.ninesReachable
        
        point.ninesReachable = allReachables
        point.alreadyVisited = True

        return
                
    def trailheadSum(self):
        res = 0
        for head in self.trailheads:
            x = head[0]
            y = head[1]
            self.visitNeighbours(x,y)
            nines = []
            for point in self.grid[x][y].ninesReachable:
                if not point in nines:
                    nines.append(point)
            res += len(nines) 
        print(res)

grid = grid()
grid.trailheadSum()