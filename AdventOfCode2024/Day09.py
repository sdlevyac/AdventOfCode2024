data = open("Inputs/Day09.txt").read()

def drawFile(file):
    output = ""
    for block in file:
        output += str(block[0]) * block[1]
    return output

def part2():
    file = []
    gap = False
    num = 0
    for count in data:
        if not gap:
            file.append((num,int(count)))
            num += 1
        else:
            file.append((".", int(count)))
        gap = not gap

    print(drawFile(file))
    i = 0
    j = len(file) - 1
    while i < len(file):
        #print(i,len(file))
        if file[i][0] == ".":
            #print("empty!")
            for x in range(len(file) - 1,i,-1):
                #print(file[i], file[j])
                if file[x][0] != "." and file[x][1] <= file[i][1]:
                    file[i] = (file[i][0], file[i][1] - file[x][1])
                    #file[i][1] -= file[x][1]
                    temp = file[x]
                    file[x] = (".", temp[1])
                    file.insert(i,temp)
                    #print(drawFile(file))
                    #input()
                    break
        i += 1
    print(drawFile(file))
    #fileNums = drawFile(file)
    ans = 0
    fileNums = []
    for block in file:
        fileNums.extend([block[0] for _ in range(block[1])])
    print(fileNums)
    input()
    for i in range(len(fileNums)):
        if fileNums[i] != ".":
            ans += i * int(fileNums[i])

    print(ans)
part2()

def part1():
    file = []

    gap = False
    num = 0
    for count in data:
        print(num,count)
        if not gap:
            file.extend([str(num) for _ in range(int(count))])
            num = num + 1
        else:
            file.extend(["." for _ in range(int(count))])
        gap = not gap

    print(file,len(file))
    input()

    backwards = len(file) - 1
    for i in range(len(file)):
        print(i)
        if file[i] == ".":
            for j in range(backwards, i, -1):
                if file[j] != ".":
                    file[i] = file[j]
                    file[j] = "."
                    backwards = j
                    break

    print(file)
    fileNums = [int(bit) for bit in file if bit != "."]
    ans = 0

    for i in range(len(fileNums)):
        ans += i * fileNums[i]

    print(ans)
