data = open("Inputs/Day02.txt","r").read().split("\n")
data = [l.split(" ") for l in data]
data = [[int(n) for n in l] for l in data]

ans01 = 0
for i in range(len(data)):
	line = data[i]
	safe = True
	asc = line[0] < line[1]
	for j in range(len(line) - 1):
		if (line[j] < line[j+1]) != asc:
			safe = False
			print("UNSAFE")
			break
		gap = abs(line[j + 1] - line[j])
		print(line[j], line[j+1], gap)
		if gap > 3 or gap < 1:
			safe = False
			print("UNSAFE")
			break
	if safe:
		print("SAFE")
		ans01 += 1
	else:
		variants = []
		for i in range(len(line)):
			variants.append([line[j] for j in range(len(line)) if j != i])
		print(line, variants)
		input()
	#input()

print(ans)