from functools import *

data = open("Inputs/Day05.txt").read().split("\n\n")

rules = data[0].split("\n")
rules = [rule.split("|") for rule in rules]
#print(rules)

pages = data[1].split("\n")
pages = [row.split(",") for row in pages]
#print(pages)

def inOrder(page):
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            if page[i] not in orders.keys() and i + 1 != len(page):
                inOrder = False
                return False
            if page[j] not in orders[page[i]]:
                inOrder = False
                return False
    return True


def compare(a,b):
    if a in orders[b]:
        return 1
    if b in orders[a]:
        return -1
    return 0

ans = 0

bad = []

orders = {}
for rule in rules:
    before = rule[0]
    after = rule[1]
    if before not in orders.keys():
        orders[before] = set()
    if after not in orders.keys():
        orders[after] = set()
    orders[before].add(after)


for page in pages:
    if inOrder(page):
        ans += int(page[len(page) // 2])
    else:
        bad.append(page)

print(ans)
print(bad)

ans = 0

for page in bad:
    page = sorted(page, key=cmp_to_key(compare))
    ans += int(page[len(page) // 2])

print(ans)


    
