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
				step = 0
				while True:				
					antinode = (coords[i][0] + diff[0] * step, coords[i][1] + diff[1] * step)
					if antinode[0] >= 0 and antinode[0] < len(data) and antinode[1] >= 0 and antinode[1] < len(data[0]):
						antinodes[antinode[0]][antinode[1]] = "#"
						#print(antinode)
						step += 1
					else:
						break


draw()
print(sum([row.count("#") for row in antinodes]))



