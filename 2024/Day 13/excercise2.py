import re

class Button:

    def __init__(self, buttonString: str):
        match = re.search(r'Button (\w): X\+(\d+), Y\+(\d+)', buttonString)
        if match:
            button_name = match.group(1)   # Der Name des Buttons (A oder B)
            self.xDir = int(match.group(2))        # Erste gefundene Zahl
            self.yDir = int(match.group(3))        # Zweite gefundene Zahl

            if button_name == "A":
                self.costs = 3
            elif button_name == "B":
                self.costs = 1

class Machine:

    def __init__(self, listWithStrings):
        self.buttonA = Button(listWithStrings[0])
        self.buttonB = Button(listWithStrings[1])

        match = re.search(r'Prize: X=(\d+), Y=(\d+)' ,listWithStrings[2])
        if match:
            self.prizeLocX = int(match.group(1)) + 10000000000000
            self.prizeLocY = int(match.group(2)) + 10000000000000
        
        self.findSolution()

    def printSolution(self, aPressNumber,bPressNumber):
        print(aPressNumber, bPressNumber)
        print(self.prizeLocX, self.prizeLocY)

    def findSolution(self):
        zaehlerB = self.prizeLocY * self.buttonA.xDir - self.prizeLocX * self.buttonA.yDir
        nennerB = self.buttonB.yDir * self.buttonA.xDir - self.buttonB.xDir * self.buttonA.yDir

        if zaehlerB % nennerB != 0:
            self.solution = 0
            return
        bPressNumber = zaehlerB//nennerB

        aPressNumber = (self.prizeLocX - self.buttonB.xDir * bPressNumber ) // ( self.buttonA.xDir )

        if aPressNumber*self.buttonA.xDir + bPressNumber*self.buttonB.xDir != self.prizeLocX:
            self.solution = 0
            return
        if aPressNumber*self.buttonA.yDir + bPressNumber*self.buttonB.yDir != self.prizeLocY:
            self.solution = 0
            return
        self.solution = self.solutionCosts(aPressNumber, bPressNumber)

        self.printSolution(aPressNumber,bPressNumber)
    
    def solutionValid(self, aPress, bPress):
        if aPress*self.buttonA.xDir + bPress*self.buttonB.xDir != self.prizeLocX:
            return False
        if aPress*self.buttonA.yDir + bPress*self.buttonB.yDir != self.prizeLocY:
            return False
        return True

    def solutionCosts(self, aPress, bPress):
        return aPress*self.buttonA.costs + bPress*self.buttonB.costs
    
class PuzzleSolver:

    def __init__(self):
        openObject = open("Day 13/input.txt")
        contents = openObject.read()
        openObject.close()
        contents = contents.split("\n\n")
        contents = [ content.split("\n") for content in contents]

        self.machines: list[Machine] = []
        for content in contents:
            self.machines.append(Machine(content))
        
        self.allTokenCosts()
    
    def allTokenCosts(self):
        res = 0
        anzahl = len(self.machines)
        counter = 1
        for machine in self.machines:
            print(f"Solving machine {counter} from {anzahl}")
            counter += 1
            res += machine.solution
        print(res)



PuzzleSolver()