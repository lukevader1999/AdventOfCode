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
            self.prizeLocX = int(match.group(1))
            self.prizeLocY = int(match.group(2))
        
        self.trySolutions()

    def findSolution(self):
        # Die Formeln liefer ein korrektes Ergbenis bis auf Float-Ungenauigkeiten. Sie liefern aber keine ganzen Zahlen! Sind die Ergebnisse nicht eindeutig?
        bPressNumber = (self.prizeLocY - self.buttonA.yDir * self.prizeLocX / self.buttonA.xDir)/(self.buttonB.yDir - self.buttonB.xDir/self.buttonA.xDir)
        aPressNumber = (self.prizeLocX - self.buttonB.xDir * bPressNumber ) / ( self.buttonA.xDir )
        print(aPressNumber)
        print(bPressNumber)
        print(aPressNumber*self.buttonA.xDir + bPressNumber*self.buttonB.xDir)
        print(self.prizeLocX)
    
    def trySolutions(self):
        lowestSolutionCosts = 0
        lowestSolution = []
        for i in range(0,101):
            for j in range(0,101):
                if self.solutionValid(i,j):
                    costs = self.solutionCosts(i,j)
                    if lowestSolutionCosts == 0 or costs < lowestSolutionCosts:
                        lowestSolution = [i,j]
                        lowestSolutionCosts = costs
        return lowestSolutionCosts

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
        for machine in self.machines:
            res += machine.trySolutions()
        print(res)



PuzzleSolver()