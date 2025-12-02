import re

#Mathematically the robot can move on an infinte grid every step and only add the end the positions are calculatet with modulo the grid sizes

class Robot:

    def __init__(self, position: tuple[int,int], velocity: tuple[int, int]):
        self.position = position
        self.velocity = velocity

    def moveOneStep(self):
        self.position = tuple(map(lambda x,y: x+y, self.position, self.velocity ))

    def printRobotConfig(self):
        print(f"p={self.position[0]},{self.position[1]} v={self.velocity[0]},{self.velocity[1]}")

class Grid:

    def __init__(self, gridSizeX, gridSizeY):
        self.robots: set[Robot] = set()
        self.gridSizeX = gridSizeX
        self.gridSizeY = gridSizeY

        input = open("Day 14/input.txt")
        regex = "[+-]?[0-9]+"
        for line in input:
            numbers = re.findall(regex, line)
            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])
            self.robots.add(Robot((numbers[0],numbers[1]), (numbers[2],numbers[3])))
        input.close

        self.initQuadrants()

        #self.printConfig()

    def printConfig(self):
        self.printCountDic()
        for robot in self.robots:
            robot.printRobotConfig()

    def iterate(self, stepNumber):
        for i in range(0,stepNumber):
            for robot in self.robots:
                robot.moveOneStep()
    
    def mapRobotsOnMap(self):
        for robot in self.robots:
            robot.position = (robot.position[0] % self.gridSizeX, robot.position[1] % self.gridSizeY)

    def makeCountDic(self):
        self.mapRobotsOnMap()
        robotCountDict = dict()
        for robot in self.robots:
            pos1, pos2 = robot.position
            if (pos1,pos2) not in robotCountDict:
                robotCountDict[(pos1,pos2)] = 1
            else:
                robotCountDict[(pos1,pos2)] = robotCountDict[(pos1,pos2)] + 1
        self.robotCountDict = robotCountDict
    
    def printCountDic(self):
        self.makeCountDic()
        for y in range(0,self.gridSizeY):
            for x in range(0, self.gridSizeX):
                if (x,y) in self.robotCountDict:
                    print(self.robotCountDict[(x,y)], end="")
                else:
                    print(".", end="")
            print("\n")

    def solve(self):
        self.iterate(100)
        self.makeCountDic()
        res = 1
        for Quadrant in self.Quadrants:
            res = res * Quadrant.countRobots(self.robotCountDict)
        print(res)

    def initQuadrants(self):
        self.Quadrants = set()
        xmid = self.gridSizeX//2
        ymid = self.gridSizeY//2

        self.Quadrants.add(Quadrant(0,xmid - 1,0,ymid - 1))
        self.Quadrants.add(Quadrant(xmid+1,self.gridSizeX-1,0,ymid-1))
        self.Quadrants.add(Quadrant(xmid+1,self.gridSizeX-1,ymid+1,self.gridSizeY-1))
        self.Quadrants.add(Quadrant(0,xmid-1,ymid+1,self.gridSizeY-1))



class Quadrant:

    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
    
    def countRobots(self, countDic: dict):
        res = 0
        for x in range(self.xmin, self.xmax + 1):
            for y in range(self.ymin, self.ymax+1):
                if (x,y) in countDic:
                    res += countDic[(x,y)]
        return res



Grid = Grid(gridSizeX = 101,gridSizeY = 103)
Grid.solve()