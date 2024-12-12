data = open("Inputs/Day07.txt","r").read().split("\n")
data = [line.split(": ") for line in data]
data = [[int(line[0]), [int(num) for num in line[1].split(" ")]] for line in data]


