from sympy import Eq, solve
from sympy.abc import a,b

data = open("Inputs/Day13.txt").read().split("\n\n")

#data = data[0]

ans = 0

for block in data:
    block = [line.split(": ")[1] for line in block.split("\n")]
    block = [line.split(", ") for line in block]
    block = [[int(num[2:]) for num in line] for line in block]
    print(block)

    print(f"{block[0][0]}a + {block[1][0]}b = {block[2][0]}")
    print(f"{block[0][1]}a + {block[1][1]}b = {block[2][1]}")

    sol = solve([Eq(block[0][0]*a + block[1][0]*b, block[2][0]),
                 Eq(block[0][1]*a + block[1][1]*b, block[2][1])])

    a = sol[a]

    b = sol[b]
    if a == a // 1 and b == b // 1:
        print(a,b)
        ans += a + b

print(ans)

#solving equations
#ax + bx = X
#   and
#ay + by = Y