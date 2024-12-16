data = open("Inputs/Day10.txt").read().split("\n")
data = [list(line) for line in data]

for row in data:
    print("".join(row))

starts = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "0":
            starts.append((i,j))

print(starts)