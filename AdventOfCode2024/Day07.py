import itertools

data = open("Inputs/Day07.txt","r").read().split("\n")
data = [line.split(": ") for line in data]
data = [[int(line[0]), [int(num) for num in line[1].split(" ")]] for line in data]

def evaluate(operands, operators):
    result = operands[0]
    for i in range(len(operands) - 1):
        num = operands[i + 1]
        operator = operators[i]
        if operator == "+":
            result += num
        elif operator == "*":
            result *= num
        else:
            result = int(str(result) + str(num))
    #print(operands, operators, result)
    return result
def generate(operands, target):
    print(operands)
    operators = itertools.product("+*|",repeat = len(operands) - 1)
    for o in operators:
        if evaluate(operands, o) == target:
            return target
    return 0
    
count = 0
ans = 0
for line in data:
    count += 1
    print(count/len(data))
    results = generate(line[1], line[0])
    ans += results

print(ans)