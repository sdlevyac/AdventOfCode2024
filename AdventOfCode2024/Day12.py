data = open("Inputs/Day12.txt").read().split("\n")
data = [list(row) for row in data]

def draw(grid):
    for row in grid:
        print("".join([_ if _ in ["#","@","%"] else "." for _ in row ]))

def walk(grid,start):
    grid = [[_ if _ in ["#","@","%"] else "." for _ in row] for row in grid]
    start = (start[0] - 1, start[1])
    print(f"starting at {start}")
    current = [start[0], start[1]]
    steps = 0
    sides = 0
    direction = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    walking = True
    while walking:
        #need to be able to handle turning anticlockwise!
        #lfr = (left, forward)
        #if lf = (#,_) go forward
        #if lf = (_,_) go left
        #if lf = (#,#) go right
        print(f"stepping from {current} in direction {directions[direction]}")
        grid[current[0]][current[1]] = "%"
        toCheck = directions[(direction + 1) % 4]
        toCheck = (toCheck[0] + current[0], toCheck[1] + current[1])
        left = directions[(direction + 1) % 4]
        forward = directions[direction]
        lf = (grid[current[0] + left[0]][current[1] + left[1]],grid[current[0] + forward[0]][current[1] + forward[1]])
        print(f"checking {toCheck}")
        print(lf)
        draw(grid)
        input()
        if lf == ("#","."):
            print("go forward")
            steps += 1
            current = [current[0] + directions[direction][0], current[1] + directions[direction][1]]
        elif lf == (".","."):
            print("turn left")
            direction = (direction + 1) % 4
            sides += 1
            steps += 1
            current = [current[0] + directions[direction][0], current[1] + directions[direction][1]]
        elif lf == ("#","#"):
            print("turn right")
            direction = (direction - 1) % 4
            sides += 1
            steps += 1
            current = [current[0] + directions[direction][0], current[1] + directions[direction][1]]
        elif lf == (".","#"):
            current = [current[0] - directions[direction][0], current[1] - directions[direction][1]]
            direction = (direction - 1) % 4
        elif "%" in lf:
            walking = False

        # if grid[toCheck[0]][toCheck[1]] == "#":
        #     steps += 1
        #     current = [current[0] + directions[direction][0], current[1] + directions[direction][1]]
            
        # else:
        #     direction = (direction + 1) % 4
        #     sides += 1
        #     steps += 1
        #     current = [current[0] + directions[direction][0], current[1] + directions[direction][1]]
    return sides

def fence(grid, visited, day2):
    perimeter = 0
    for v in visited:
        for d in [(1,0),(0,1),(0,-1),(-1,0)]:
            f = (v[0] + d[0], v[1] + d[1])
            if grid[f[0]][f[1]] != "#":
                grid[f[0]][f[1]] = "@"
                perimeter += 1

    draw(grid)
    if day2:
        return sum([row.count("@") for row in grid])
    else:
        return perimeter

def floodFill(grid, i, j, day2):
    print(f"flood filling {grid[i][j]}s from ({i},{j})")
    toVisit = [(i,j)]
    visited = set()
    while len(toVisit) != 0:
        current = toVisit[0]
        toVisit.pop(0)
        visited.add(current)
        filled.add(current)
        grid[current[0]][current[1]] = "#"
        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            step = (current[0] + d[0], current[1] + d[1])
            if data[current[0]][current[1]] == grid[step[0]][step[1]] and step not in visited and step not in toVisit:
                toVisit.append(step)
                
    area = sum([row.count("#") for row in grid])
    #draw(grid)
    gridBuffer = [[_ for _ in row] for row in grid]
    #perimeter = fence(gridBuffer, visited, day2)
    perimeter = walk(gridBuffer, (i,j))
    price = area * perimeter
    print(f"{area} * {perimeter} = {price}")
    input()
    return price


data.append(["0" for _ in range(len(data[0]))])
data.append(["0" for _ in range(len(data[0]))])
data.insert(0, ["0" for _ in range(len(data[0]))])
data.insert(0, ["0" for _ in range(len(data[0]))])
for i in range(len(data)):
    data[i].insert(0,"0")
    data[i].append("0")
    data[i].insert(0,"0")
    data[i].append("0")

filled = set()

ans = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        current = (i,j)
        if data[i][j] != "0" and current not in filled:
            buffer = [[_ for _ in row] for row in data]
            ans += floodFill(buffer,i,j,True)

print(ans)


