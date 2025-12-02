input = open("input.txt")
reports = []
for line in input:
    report = [int(x) for x in line.split()]
    reports.append(report)
input.close()

def isSafe(report):
    if len(report) == 1:
        return True
    direction = report[1] - report[0]
    for i in range(1,len(report)):
        diff = report[i]-report[i-1]
        if direction < 0 and diff > 0:
            return False
        if direction > 0 and diff < 0:
            return False
        if not( 1 <= abs(diff) <= 3):
            return False
    return True

def removePosFromList(list, i):
    res = []
    for j in range(len(list)):
        if j != i:
            res.append(list[j])
    return res 

def tryProblemDampenerOld(report, i):
    report1 = removePosFromList(report, i)
    report2 = removePosFromList(report, i-1)
    if isSafe(report1) or isSafe(report2):
        return True
    else:
        return False

def tryProblemDampener(report, i):
    for i in range(len(report)):
        if isSafe(removePosFromList(report, i)):
            return True
    return False
    
def isSafeWithDampener(report):
    if len(report) == 1:
        return True
    direction = report[1] - report[0]
    for i in range(1,len(report)):
        diff = report[i]-report[i-1]
        if direction < 0 and diff > 0:
            return tryProblemDampener(report, i)
        if direction > 0 and diff < 0:
            return tryProblemDampener(report, i)
        if not( 1 <= abs(diff) <= 3):
            return tryProblemDampener(report, i)
    return True

def isSafeWithDampenerOld(report):
    if len(report) == 1:
        return True
    direction = report[1] - report[0]
    for i in range(1,len(report)):
        diff = report[i]-report[i-1]
        if direction < 0 and diff > 0:
            return tryProblemDampenerOld(report, i)
        if direction > 0 and diff < 0:
            return tryProblemDampenerOld(report, i)
        if not( 1 <= abs(diff) <= 3):
            return tryProblemDampenerOld(report, i)
    return True

count = 0

testLists = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

for report in testLists:
    print(f"Report {report} is {isSafeWithDampener(report)}")

for report in reports:
    if isSafeWithDampener(report):
        count += 1
        if not isSafeWithDampenerOld(report):
            print(report)
# Ich hab nicht ganz zu Ende gedacht, dass das Problem (wenn es ganz am Anfang auftaucht) auch zwei Zahlen hinter dem Index wo das Problem auftaucht gelöst werden kann.

print(count)