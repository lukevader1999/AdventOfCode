input = open("input.txt")
list1 = []
list2 = []
for line in input:
    numbers = line.split()
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))
input.close()
list1.sort()
list2.sort()

# Teil 1
res = 0
for i in range(0,len(list1)):
    res += abs(list1[i]-list2[i])
print(res)

# Teil 2
countDict = {}
for number in list2:
    if number not in countDict:
        countDict[number] = 1
    else:
        countDict[number] += 1

res = 0
for number in list1:
    if number in countDict:
        res += number*countDict[number]
print(res)