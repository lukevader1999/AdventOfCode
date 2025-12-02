input = open('Day 5/input.txt')

# Die Regeln werden in einem Dictionary gespeichert. Der Value zu einem key enthält die Liste aller Zahlen, die NACH dem Key gedruckt werden müssen
rules = {}
updates = []

inputPartOne=True

for line in input:
    if line == "\n":
        inputPartOne = False
        continue
    if inputPartOne:
        numbers = [int(x) for x in line.split('|')]
        key = numbers[0]
        value = numbers[1]
        if key not in rules:
            rules[key] = [value]
        else:
            rules[key].append(value)
    else:
        updates.append([int(x) for x in line.split(',')])
input.close()

def rulesOk(update, rules):
    for i in range(1, len(update)):
        if update[i] in rules:
            mustBePrintedAfter = rules[update[i]]
        else:
            continue
        for j in range(0,i):
            if update[j] in mustBePrintedAfter:
                return False
    return True

falseUpdates = []

res = 0
for update in updates:
    if rulesOk(update,rules):
        res += update[len(update)//2]
    else:
        falseUpdates.append(update)

# Wie erstellt man ein richtig geordnetes Update? These: In einem Update muss es immer eine Zahl geben, die in keinem der Dictionary-Werte der anderen Zahlen im Update vorkommt.
# Denn würde es solch eine Zahl nicht geben, kann keine Zahl des Updates die erste Zahl sein und es existiert keine richtige Reihenfolge. Ein funktionierender Algorithmus ist also,
# aus allen Zahlen die Zahl mit der Eigenschaft zu finden, an den Anfang des Updates zu tun und mit den restlichen Zahlen als Teilupdate dieses Vorgehen zu iterieren.

def findFirstNumber(update, rules):
    for number in update:
        numberViable = True
        for otherNumber in update:
            if otherNumber in rules:
                if number in rules[otherNumber]:
                    numberViable = False
        if numberViable:
            return number
    return -1

def orderUpdate(update,rules):
    newUpdate = []
    while len(update) > 0:
        firstNumber = findFirstNumber(update,rules)
        newUpdate.append(firstNumber)
        update.remove(firstNumber)
    return newUpdate

res = 0
for update in falseUpdates:
    update = orderUpdate(update, rules)
    print(update)
    res += update[len(update)//2]
print(res)