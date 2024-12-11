data = open("Inputs/Day05.txt").read().split("\n\n")

def search_for_page(before, after):
    these_rules = [rule for rule in rules if rule[0] == before]
    for rule in these_rules:
        if rule[1] == after:
            return True
    for rule in these_rules:
        return search_for_page(rule[1], after)
    return False

def check_update(page):
    print(page)
    for i in range(len(page) - 1):
        if not search_for_page(page[i], page[i + 1]):
            return False
    return True

rules = data[0].split("\n")
rules = [rule.split("|") for rule in rules]
#print(rules)

pages = data[1].split("\n")
pages = [row.split(",") for row in pages]
#print(pages)
ans = 0
for page in pages:
    if check_update(page):
        ans += int(page[len(page) // 2])
print(ans)