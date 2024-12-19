from time import sleep

from common.tools import draw, add, inRange

data = open("Inputs/Day15.txt").read().split("\n\n")

directions = {">":(0,1),
              "<":(0,-1),
              "^":(-1,0),
              "v":(1,0),}

doubles = {".":[".","."],
           "#":["#","#"],
           "@":["@","."],
           "O":["[","]"]}

grid = data[0]
grid = [list(row) for row in grid.split("\n")]
realGrid = []
for i in range(len(grid)):
    row = []
    for j in range(len(grid[i])):
        row.extend(doubles[grid[i][j]])
    realGrid.append(row)
        
for i in range(len(realGrid)):
    for j in range(len(realGrid[i])):
        if realGrid[i][j] == "@":
            pos = [i,j]

x = len(realGrid)
y = len(realGrid[0])
instructions = "".join(data[1].split("\n"))

for step in instructions:
    #draw(realGrid)
    if step in ["<",">"]:
        d = directions[step]
        nextPos = add(pos,d)
        if realGrid[nextPos[0]][nextPos[1]] == ".":
            realGrid[nextPos[0]][nextPos[1]] = "@"
            realGrid[pos[0]][pos[1]] = "."
            pos = [nextPos[0], nextPos[1]]
        elif realGrid[nextPos[0]][nextPos[1]] in ["[","]"]:
            freePos = [-1,-1]
            steps = 1
            freeSpace = False
            while inRange(nextPos,x,y) and not freeSpace:
                nextPos = add(nextPos,d)
                steps+=1
                if realGrid[nextPos[0]][nextPos[1]] == ".":
                    #print(f"free space found {steps} steps away!")
                    freeSpace = True
                elif realGrid[nextPos[0]][nextPos[1]] == "#":
                    break
            if freeSpace:
                #print(f"need to move @ {steps} steps in {d} direction")
                for i in range(steps):
                    temp = realGrid[nextPos[0]][nextPos[1]]
                    realGrid[nextPos[0]][nextPos[1]] = realGrid[nextPos[0] - d[0]][nextPos[1] - d[1]]
                    realGrid[nextPos[0] - d[0]][nextPos[1] - d[1]] = temp
                    nextPos = [nextPos[0] - d[0], nextPos[1] - d[1]]
                pos = add(pos,d)
    else:
        print(step)
    

    draw(realGrid)
    input()


