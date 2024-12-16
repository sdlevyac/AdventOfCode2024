data = open("Inputs/Day12.txt").read().split("\n")
data = [list(row) for row in data]

def draw(grid):
    for row in grid:
        print("".join([_ if _ == "#" else "." for _ in row ]))

def floodFill(grid, i, j):
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
                

    draw(grid)
    input()


data.append(["0" for _ in range(len(data[0]))])
data.insert(0, ["0" for _ in range(len(data[0]))])
for i in range(len(data)):
    data[i].insert(0,"0")
    data[i].append("0")

filled = set()

for i in range(len(data)):
    for j in range(len(data[i])):
        current = (i,j)
        if data[i][j] != "0" and current not in filled:
            buffer = [[_ for _ in row] for row in data]
            floodFill(buffer,i,j)


draw(data)