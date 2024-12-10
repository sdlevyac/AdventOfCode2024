data = open("Inputs/Day04.txt").read().split("\n")

def part01():
    lines = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i + 4 <= len(data):
                line = "".join([data[i + n][j] for n in range(4)])
                lines.append(line)
                lines.append(line[::-1])
            if j + 4 <= len(data[i]):
                line = data[i][j:j+4]
                lines.append(line)
                lines.append(line[::-1])
            if i + 4 <= len(data) and j + 4 <= len(data[i]):
                line = "".join([data[i+n][j+n] for n in range(4)])
                lines.append(line)
                lines.append(line[::-1])
            if i + 4 <= len(data) and j - 4 >= -1:
                line = "".join([data[i+n][j-n] for n in range(4)])
                lines.append(line)
                lines.append(line[::-1])
    print(lines.count("XMAS"))

def check_cross(block):
    print(block)
    x = "".join(block[1])
    y = "".join(block[n][1] for n in range(3))
    print(x,y)
    xyPos = "".join([block[n][n] for n in range(3)])
    xyNeg = "".join([block[n][2-n] for n in range(3)])
    print(xyPos,xyNeg)
    #two cross shapes to check:
    #   .?.     ?.?
    #   ?A?     .A.
    #   .?.     ?.?

for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] == "A":
            print("checking...")
            if i - 1 >= 0 and j - 1 >= 0 and i + 1 < len(data) and j + 1 < len(data):
                block = []
                for x in [-1,0,1]:
                    print(data[i+x][j-1:j+2])
                    block.append(list(data[i+x][j-1:j+2]))
                check_cross(block)
            print()
