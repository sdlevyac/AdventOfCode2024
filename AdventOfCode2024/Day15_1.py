from time import sleep

from common.tools import draw, add, inRange

data = open("Inputs/Day15.txt").read().split("\n\n")

directions = {">":(0,1),
              "<":(0,-1),
              "^":(-1,0),
              "v":(1,0),}

grid = data[0]
grid = [list(row) for row in grid.split("\n")]
x = len(grid)
y = len(grid[0])
instructions = "".join(data[1].split("\n"))

pos = [len(grid)//2 - 1, len(grid[0])//2 - 1]
count = 0
for step in instructions:
    count += 1
    #draw(grid)
    d = directions[step]
    nextPos = add(pos,d)
    if grid[nextPos[0]][nextPos[1]] == ".":
        grid[nextPos[0]][nextPos[1]] = "@"
        grid[pos[0]][pos[1]] = "."
        pos = [nextPos[0], nextPos[1]]
    elif grid[nextPos[0]][nextPos[1]] == "O":
        freePos = [-1,-1]
        steps = 1
        freeSpace = False
        while inRange(nextPos,x,y) and not freeSpace:
            nextPos = add(nextPos,d)
            steps+=1
            if grid[nextPos[0]][nextPos[1]] == ".":
                #print(f"free space found {steps} steps away!")
                freeSpace = True
            elif grid[nextPos[0]][nextPos[1]] == "#":
                break
        if freeSpace:
            #print(f"need to move @ {steps} steps in {d} direction")
            for i in range(steps):
                temp = grid[nextPos[0]][nextPos[1]]
                grid[nextPos[0]][nextPos[1]] = grid[nextPos[0] - d[0]][nextPos[1] - d[1]]
                grid[nextPos[0] - d[0]][nextPos[1] - d[1]] = temp
                nextPos = [nextPos[0] - d[0], nextPos[1] - d[1]]
            pos = add(pos,d)

    #print(step)
    #draw(grid)
    #sleep(0.01)
    #input()
draw(grid)
ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            ans += (100 * i) + j

print(ans)


