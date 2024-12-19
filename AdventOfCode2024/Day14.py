data = open("Inputs/Day14.txt").read().split("\n")

def draw(grid):
    print()
    for row in grid:
        print("".join([str(_) for _ in row]))


dim = (101,103)

data = [line.split(" ") for line in data]
data = [[coord[2:] for coord in line] for line in data]
data = [[coord.split(",") for coord in line] for line in data]
data = [[[int(coord) for coord in coords] for coords in line] for line in data]


i = 0
while i <= 10000:
#for i in range(101):

    print(f"after {i+1} seconds:")
    grid = [[0 for _ in range(dim[0])] for __ in range(dim[1])]
    for robot in data:
        pos = robot[0]
        vel = robot[1]
        newPos = [0,0]
        for d in range(2):
            newPos[d] = (pos[d] + (i * vel[d])) % dim[d]
        grid[newPos[1]][newPos[0]] += 1
    #draw(grid)
    with open("Notes/Day14Output.txt","a") as f:
        f.write(f"after {i+1} seconds:")
        for row in grid:
            f.write("".join(["#" if _ > 0 else " " for _ in row]) + "\n")

    
    #input()
    i+=1
print(data)