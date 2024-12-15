data = open("Inputs/Day08.txt").read().split("\n")
data = [list(line) for line in data]

def draw():
	for row in data:
		print("".join(row))

	print()

	for row in antinodes:
		print("".join(row))

antinodes = [["." for col in row] for row in data]

antennae = {}
coords = []

for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] != ".":
			antennae[(i,j)] = data[i][j]
			coords.append((i,j))

for i in range(len(coords)):
	for j in range(len(coords)):
		if i != j:
			if antennae[coords[i]] == antennae[coords[j]]:
				print(f"pair of '{antennae[coords[i]]}'s at {coords[i]} and {coords[j]}")
				diff = (coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])
				antinode = (coords[i][0] + diff[0], coords[i][1] + diff[1])
				if antinode[0] >= 0 and antinode[0] < len(data) and antinode[1] >= 0 and antinode[1] < len(data[0]):
					antinodes[antinode[0]][antinode[1]] = "#"
					print(antinode)



print(sum([row.count("#") for row in antinodes]))

antinodes = [["." for col in row] for row in data]
for i in range(len(coords)):
	for x in range(len(data)):
		for y in range(len(data[0])):
			if x == coords[i][0] or y == coords[i][1] or abs(coords[i][0] - x) == abs(coords[i][1] - y):
				if antinodes[x][y] == ".":
					antinodes[x][y] = antennae[coords[i]]
				elif antinodes[x][y] == antennae[coords[i]]:
					antinodes[x][y] = "#"
	draw()
	input()

