data = open("Inputs/Day14.txt").read().split("\n")

data = [line.split(" ") for line in data]
data = [[coord[2:] for coord in line] for line in data]
print(data)