data = open("Inputs/Day06.txt").read().split("\n")
data = [list(row) for row in data]
print(data)

movement = {"v":[1,0],
            ">":[0,1],
            "<":[0,-1],
            "^":[-1,0]}

pos = [-1,-1]

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] in [">","<","^","v"]:
            pos = [i,j]

here = True

while here:
    symbol = data[pos[0]][pos[1]]
    m = movement[symbol]
    n = [pos[0] + m[0], pos[1] + m[1]]
    data[pos[0]][pos[1]] = "X"
    if n[0] >= 0 and n[0] < len(data) and n[1] >= 0 and n[1] < len(data[0]):
        i
