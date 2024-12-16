data = open("Inputs/Day12.txt").read().split("\n")
data = [list(row) for row in data]
data = ["#".join(row) for row in data]
print(data)

data.append([])


# draw(data)