import re

data = open("Inputs/Day03.txt","r").read()

ans = 0
muls = re.findall("mul\([0-9]+\,[0-9]+\)", data)
for mul in muls:
    mul = mul.replace("mul(","")
    mul = mul.replace(")","")
    mul = [int(n) for n in mul.split(",")]
    ans += mul[0] * mul[1]
print(ans)

ans = 0
muls = re.findall("mul\([0-9]+\,[0-9]+\)|do\(\)|don't\(\)", data)
do_mul = True
for mul in muls:
    if mul == "do()":
        do_mul = True
    elif mul == "don't()":
        do_mul = False
    elif do_mul:
        mul = mul.replace("mul(","")
        mul = mul.replace(")","")
        mul = [int(n) for n in mul.split(",")]
        ans += mul[0] * mul[1]
print(ans)