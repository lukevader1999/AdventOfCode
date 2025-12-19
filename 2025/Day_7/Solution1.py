#Read sampleInput.txt file
#input_path = '2025/Day_7/sampleInput.txt'
input_path = '2025/Day_7/input.txt'
with open(input_path, 'r') as file:
    input = file.read().splitlines()

#Convert input to a grid (list of lists)
grid = [list(line) for line in input]

#Following a beam and counting how often it gets split has the problem that overlapping beams get counted multiple times.
#Instead we can mark points that split at least one beam and count them after processing all beams.

EMPTY_SPACE = '.'
START_POINT = 'S'
BEAM = '|'
SPLITTER = '^'
USED_SPLITTER_COORDINATES = set()
GRID_WIDTH = len(grid[0])
GRID_HEIGHT = len(grid)

def process_first_line():
    lineIndex = 0
    for index, char in enumerate(grid[lineIndex]):
        if char == 'S':
            grid[lineIndex+1][index] = BEAM

def process_line(lineIndex):
    for index, char in enumerate(grid[lineIndex]):
        if char == BEAM:
            if grid[lineIndex+1][index] == SPLITTER:
                if (index+1 < GRID_WIDTH):
                    grid[lineIndex+1][index+1] = BEAM
                if (index-1 >= 0):
                    grid[lineIndex+1][index-1] = BEAM
                USED_SPLITTER_COORDINATES.add((lineIndex+1, index))
            else:
                grid[lineIndex+1][index] = BEAM

for lineIndex in range(GRID_HEIGHT - 1):
    if lineIndex == 0:
        process_first_line()
    else:
        process_line(lineIndex)

print("Number of used splitters:", len(USED_SPLITTER_COORDINATES))
print("Processed Grid:")
for line in grid:
    print(''.join(line))