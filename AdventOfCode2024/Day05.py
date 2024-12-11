data = open("Inputs/Day05.txt").read().split("\n\n")

rules = data[0].split("\n")
rules = [rule.split("|") for rule in rules]
print(rules)

pages = data[1].split("\n")
pages = [row.split(",") for row in pages]
#print(pages)

ordering = {}
for rule in rules:
    before = rule[0]
    after = rule[1]
    if before in ordering.keys():
        ordering[before].append(after)
    else:
        ordering[before] = [after]

