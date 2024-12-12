data = open("Inputs/Day06.txt").read().split("\n")
data = [list(row) for row in data]
print(data)

symbols = [">","v","<","^"]


def draw_grid():
    for row in data:
        print("".join(row))

def find_pos():
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in symbols:
                return [i,j]
    return False

movement = {"v":[1,0],
            ">":[0,1],
            "<":[0,-1],
            "^":[-1,0]}

ans = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        print(i,j)
        data = open("Inputs/Day06.txt").read().split("\n")
        data = [list(row) for row in data]
        visited = [[0 for i in range(len(data))] for j in range(len(data))]
        if data[i][j] not in ["#","^"]:
            data[i][j] = "#"
            pos = [-1,-1]
            pos = find_pos()

            here = True
            loop = False
            while here:
                draw_grid()
                input()
                pos = find_pos()
                if not pos:
                    break
                for row in visited:
                    if 5 in row:
                        loop = True
                        print("LOOP")
                        ans += 1
                        break
                if loop:
                    break
                symbol = data[pos[0]][pos[1]]
                m = movement[symbol]
                n = [pos[0] + m[0], pos[1] + m[1]]
                data[pos[0]][pos[1]] = "X"
                visited[pos[0]][pos[1]] += 1
                if n[0] >= 0 and n[0] < len(data) and n[1] >= 0 and n[1] < len(data[0]):
                    if data[n[0]][n[1]] == "#":
                        nextSymbol = symbols[(symbols.index(symbol) + 1) % len(symbols)]
                        data[pos[0]][pos[1]] = nextSymbol
                        visited[pos[0]][pos[1]] -= 1
                    else:
                        data[n[0]][n[1]] = symbol
                #print(visited)

            # draw_grid()
            # input()
print(ans)