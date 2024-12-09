data = open("Inputs/Day02.txt","r").read().split("\n")
data = [l.split(" ") for l in data]
data = [[int(n) for n in l] for l in data]

def is_safe(line, double_check = False):
	safe = True
	asc = line[0] < line[1]
	for j in range(len(line) - 1):
		if (line[j] < line[j+1]) != asc:
			safe = False
			#print("UNSAFE")
			break
		gap = abs(line[j + 1] - line[j])
		#print(line[j], line[j+1], gap)
		if gap > 3 or gap < 1:
			safe = False
			#print("UNSAFE")
			break
	if safe:
		return True
	elif double_check:
		variants = []
		for i in range(len(line)):
			variants.append([line[j] for j in range(len(line)) if j != i])
			variant = [line[j] for j in range(len(line)) if j != i]
			if is_safe(variant):
				return True
	return False

ans01 = 0
for i in range(len(data)):
	line = data[i]
	if is_safe(line, True):
	    ans01 += 1

print(ans01)