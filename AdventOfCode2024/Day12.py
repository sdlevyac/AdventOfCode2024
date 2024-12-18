data = open("Inputs/Day12.txt").read().split("\n")
data = [list(row) for row in data]

def draw(grid):
    print("~"*len(grid[0]))
    for row in grid:
        print("".join([_ if _ in ["#","@","%"] else "." for _ in row ]))

def find_corners(grid,visited):
    min_i = min([v[0] for v in visited]) - 1
    max_i = max([v[0] for v in visited]) + 1
    min_j = min([v[1] for v in visited]) - 1
    max_j = max([v[1] for v in visited]) + 1

    grid = [[_ if _ in ["#"] else "." for _ in row] for row in grid]
    corners = ["###.","##.#","#.##",".###", "...#","..#.",".#..","#..."]
    c = 0
    for i in range(min_i, max_i):
        for j in range(min_j,max_j):
            zone = grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
            if zone in corners:
                c += 1
            elif zone in ["#..#",".##."]:
               c += 2
    return c

def fence(grid, visited, day2):
    perimeter = 0
    for v in visited:
        for d in [(1,0),(0,1),(0,-1),(-1,0)]:
            f = (v[0] + d[0], v[1] + d[1])
            if grid[f[0]][f[1]] != "#":
                grid[f[0]][f[1]] = "@"
                perimeter += 1
    if day2:
        return sum([row.count("@") for row in grid])
    else:
        return perimeter

def floodFill(grid, i, j, day2):
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
    gridBuffer = [[_ for _ in row] for row in grid]
    perimeter = fence(gridBuffer, visited, day2)
    corners = find_corners(gridBuffer, visited)
    price1 = area * perimeter
    price2 = area * corners
    return price1, price2


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

ans1 = 0
ans2 = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        current = (i,j)
        if data[i][j] != "0" and current not in filled:
            buffer = [[_ for _ in row] for row in data]
            price1, price2 = floodFill(buffer,i,j,True)
            ans1 += price1
            ans2 += price2

print(ans1,ans2)


