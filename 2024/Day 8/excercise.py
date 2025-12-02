# Grid Point Class
class GridPoint:


    def __init__(self,pos1,pos2,antenna=None):
        self.pos1 = pos1
        self.pos2 = pos2
        if antenna == '.':
            self.hasAntenna = False
        else:
            self.hasAntenna = True
            self.antenna = antenna
        self.hasAntinode = False


    def antinodeLocations(self,point):
        #Distanzen um von point zu self zu gehen
        dPos1 = self.pos1 - point.pos1
        dPos2 = self.pos2 - point.pos2

        #Von self weiter in die berechnete Richtung geht
        a1Pos1 = self.pos1 + dPos1
        a1Pos2 = self.pos2 + dPos2

        #Von point weiter in die negative Richtung der berechneten Richtung gehen
        a2Pos1 = point.pos1 - dPos1
        a2Pos2 = point.pos2 - dPos2
        return [[a1Pos1,a1Pos2],[a2Pos1,a2Pos2]]

    def print(self):
        print(self.pos1, self.pos2)


class Grid:
    def __init__(self):
        input = open("Day 8/input.txt")
        self.pointsWithSameAntenna = {}
        grid = []
        counter1 = 0
        for line in input:
            line = line.strip("\n")
            counter2 = 0
            gridLine = []
            for point in line:
                newPoint = GridPoint(counter1,counter2,point)
                if newPoint.hasAntenna:
                    if newPoint.antenna in self.pointsWithSameAntenna:
                        self.pointsWithSameAntenna[newPoint.antenna].append(newPoint)
                    else:
                        self.pointsWithSameAntenna[newPoint.antenna] = [newPoint]
                gridLine.append(newPoint)
                counter2 += 1
            grid.append(gridLine)
            counter1 += 1

        input.close()
        self.grid = grid
        self.pos1Len = len(grid)
        self.pos2Len = len(grid[0])
    
    def locationIsOnTheGrid(self,pos1,pos2):
        if pos1<0 or pos2<0:
            return False
        try:
            self.grid[pos1][pos2]
            return True
        except:
            return False
    
    def printGrid(self):
        for i in range(0,len(self.grid)):
            print("\n")
            for j in range(0,len(self.grid[i])):
                point = self.grid[i][j]
                if point.hasAntinode:
                    print("#", end="")
                elif point.hasAntenna:
                    print(point.antenna, end="")
                else:
                    print(".", end="")
    
    def setAntinodes(self):
        for antennaName in self.pointsWithSameAntenna:
            ls = self.pointsWithSameAntenna[antennaName]
            # ls enthält beim Beispiel-Input die richtigen Antennen pro Antennenname
            # print(antennaName)
            #for point in ls:
            #    print(point.pos1, point.pos2)
            if len(ls) <= 1:
                continue
            for i in range(0,len(ls)):
                for j in range(i+1,len(ls)):
                    point1 = ls[i]
                    point2 = ls[j]
                    locations = point1.antinodeLocations(point2)
                    for location in locations:
                        ii = location[0]
                        jj = location[1]
                        if self.locationIsOnTheGrid(ii,jj):
                            self.grid[ii][jj].hasAntinode = True
    
    def countAntinodes(self):
        counter = 0
        for i in range(0,len(self.grid)):
            for j in range(0,len(self.grid[i])):
                if self.grid[i][j].hasAntinode:
                    counter += 1
        print(counter)

myGrid = Grid()
myGrid.setAntinodes()
myGrid.countAntinodes()