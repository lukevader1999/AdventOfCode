#Read sampleInput.txt file
#input_path = '2025/Day_7/sampleInput.txt'
input_path = '2025/Day_7/input.txt'
with open(input_path, 'r') as file:
    input = file.read().splitlines()

#Convert input to a grid (list of lists)
grid = [list(line) for line in input]

#Now we want to know the number of possible paths through the graph. We can use recursion to do this.
#Everytime a beam splits, it creates two new beams. When a beam hits the end it returns 1 to its parent beam.
#The parent beam adds up all the paths from its children and returns that to its parent until we reach the start point.
#If the possible paths from a splitter have already been calculated, we can store that value and return it instead of recalculating it.
#Otherwise, the number of paths can grow exponentially and take a loooooong time to calculate.

EMPTY_SPACE = '.'
START_POINT = 'S'
BEAM = '|'
SPLITTER = '^'
GRID_WIDTH = len(grid[0])
GRID_HEIGHT = len(grid)
POSSIBLE_PATHS_FROM_SPLITTER = dict()

def print_grid_state():
    for line in grid:
        print(''.join(line))
    print()

def count_paths(x, y):
    #print_grid_state()
    #count_paths assume the position currently is on a beam or start point
    if y >= GRID_HEIGHT-1:
        return 1  # Reached the end of the grid successfully
    if grid[y+1][x] in [EMPTY_SPACE, BEAM]:
        grid[y+1][x] = BEAM
        return count_paths(x, y+1)
    elif grid[y+1][x] == SPLITTER:
        #Check if we have already calculated the possible paths from this splitter
        if (x, y+1) in POSSIBLE_PATHS_FROM_SPLITTER:
            return POSSIBLE_PATHS_FROM_SPLITTER[(x, y+1)]
        
        #Split the beam into two new beams and count paths from both
        grid[y+1][x-1] = BEAM
        left_path_count = count_paths(x-1, y+1)
        grid[y+1][x+1] = BEAM
        right_path_count = count_paths(x+1, y+1)
        POSSIBLE_PATHS_FROM_SPLITTER[(x, y+1)] = left_path_count + right_path_count
        return left_path_count + right_path_count

def find_start():
    y = 0
    for x in range(GRID_WIDTH):
        if grid[y][x] == START_POINT:
            return x, y

start_x, start_y = find_start()
total_paths = count_paths(start_x, start_y)
print("Grid after path counting:")
print_grid_state()
print("Total number of possible paths:", total_paths)