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

    def solve(self, stepNumber, stepIncrease, startSteps):
        myFile = open("Day 14/trees.txt", "w")
        myFile.write("")
        myFile.close

        stepCounter = 0

        for i in range(0,startSteps):
            for robot in self.robots:
                robot.moveOneStep()
            stepCounter += 1
        self.writeCountDic(stepCounter)

        for j in range(0,stepNumber):
            for i in range(0,stepIncrease):
                for robot in self.robots:
                    robot.moveOneStep()
                stepCounter += 1
            self.writeCountDic(stepCounter)
    
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
    
    def writeCountDic(self, stepCount: int):
        self.makeCountDic()
        string = ""
        for y in range(0,self.gridSizeY):
            for x in range(0, self.gridSizeX):
                if (x,y) in self.robotCountDict:
                    string += str(self.robotCountDict[(x,y)])
                else:
                    string += "."
            string += "\n"
        string += "\n"
        myFile = open("Day 14/trees.txt", "a")
        string2 = "Bathroom after step " + str(stepCount) + "\n"
        myFile.write(string2)
        myFile.write(string)
        myFile.close



Grid = Grid(gridSizeX = 101,gridSizeY = 103)
Grid.solve(stepNumber=100, stepIncrease=101, startSteps=331)

#Special iterations
#290 331 432 533 599 634 937

#Christmas Tree at 3801500!!! But is this the lowest possible number?
#Upper number is wrong, there was an error in the counting method