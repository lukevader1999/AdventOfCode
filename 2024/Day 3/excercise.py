import re

#mulRegEx = "mul\([0-9]{1,3},[0,9]{1,3}\) | do\(\) | don't\(\)"

input = open("Day 3/input.txt")
instructions = []
for line in input:
    instructions += re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line)
input.close()

def getInstructionResult(instruction):
    instruction = instruction[4:len(instruction)-1]
    numbers = instruction.split(',')
    res = int(numbers[0])*int(numbers[1])
    return res

res = 0
instructionsEnabled = True
for instruction in instructions:
    if len(instruction)==4:
        instructionsEnabled = True
    elif instruction[0] == 'd':
        instructionsEnabled = False
    elif instructionsEnabled:
        res += getInstructionResult(instruction)

print(res)