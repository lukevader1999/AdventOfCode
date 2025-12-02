#Einzelne Input Linie verarbeiten
input = open("Day 11/input.txt")
stoneList = []
for line in input:
    stoneList = [int(x) for x in line.split()]
input.close()

# Apllies rules on one stone and returns a list with a variable number of new stones
def applyRules(x):
    if x == 0:
        return [1]
    if len(str(x))%2 == 0:
        x = str(x)
        half = len(x)//2
        x1 = x[0:half]
        x2 = x[half:]
        return [int(x1),int(x2)]
    return [x*2024]

def oneStep(ls):
    newList = []
    for stone in ls:
        newList = newList + applyRules(stone)
    return newList

def doXSteps(x, stoneList):
    for i in range(0,x):
        stoneList = oneStep(stoneList)
        print(i)
    print(len(stoneList))

doXSteps(25,stoneList)