data = open("Inputs/Day10.txt").read().split("\n")
data = [list(line) for line in data]


def add(a,b):
    return (a[0] + b[0], a[1] + b[1])

def inRange(coord, grid):
    return coord[0] >= 0 and coord[0] < len(data) and coord[1] >= 0 and coord[1] < len(data[0])

for row in data:
    print("".join(row))

starts = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "0":
            starts.append((i,j))

look = -1


ans = 0
totalFound = 0
count = 0
for start in starts:
    found = 0
    count += 1
    visited = []
    toVisit = [start]
    grid = [["." for _ in row] for row in data]

    while len(toVisit) != 0:
        current = toVisit[look]
        if data[current[0]][current[1]] == "9":
            grid[current[0]][current[1]] = "@"
            found += 1
        else:
            grid[current[0]][current[1]] = "#"
        toVisit.pop(look)
        #visited.append(current)
        #print(visited,toVisit,current)
        for d in [(1,0),(0,1),(0,-1),(-1,0)]:
            step = add(current,d)
            if inRange(step, data):
                if data[step[0]][step[1]] != "." and int(data[step[0]][step[1]]) == int(data[current[0]][current[1]]) + 1 and step not in toVisit and step not in visited:
                    toVisit.append(step)


    for row in grid:
        print("".join(row))
    score = sum([row.count("@") for row in grid])
    print(count, score, found)
    ans += score
    totalFound += found
    #input()

print(ans, totalFound)