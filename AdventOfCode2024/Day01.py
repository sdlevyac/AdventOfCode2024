data = open("Inputs/Day01.txt","r").read().split("\n")
data = [l.split("   ") for l in data]
col01 = [int(l[0]) for l in data]
col02 = [int(l[1]) for l in data]

col01 = sorted(col01)
col02 = sorted(col02)

ans01 = 0
ans02 = 0
for i in range(len(col01)):
	ans01 += abs(col01[i] - col02[i])
	ans02 += col02.count(col01[i]) * col01[i]

print(ans01)
print(ans02)