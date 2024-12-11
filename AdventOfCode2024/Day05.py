data = open("Inputs/Day05.txt").read().split("\n\n")

rules = data[0].split("\n")
rules = [rule.split("|") for rule in rules]
#print(rules)

pages = data[1].split("\n")
pages = [row.split(",") for row in pages]
#print(pages)

runs = {}
for rule in rules:
    before = rule[0]
    after = rule[1]
    if before not in runs.keys():
        runs[before] = []
    runs[before].append(after)

for page in pages:
    print(page)
    for i in range(len(page) - 1):
        start = page[i]
        end = page[i + 1]
        #print(start,end)
        current = ""
        toVisit = [start]
        visited = []

        found = False
        while current != end and len(toVisit) != 0:
            current = toVisit[0]
            toVisit = toVisit[1:]
            visited.append(current)
            if current in runs.keys():
                for node in runs[current]:
                    if node not in visited and node not in toVisit:
                        toVisit.append(node)

        print(current == end)