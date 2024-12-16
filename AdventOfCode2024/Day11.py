data = open("Inputs/Day11.txt").read().split(" ")
stones = [int(_) for _ in data]

def bruteforce(stones, limit):
    count = 0
    while count != limit:
        count += 1
        stonesBuffer = []
        for stone in stones:
            #print(stone)
            if stone == 0:
                stonesBuffer.append(1)
            elif len(str(stone)) % 2 == 0:
                stoneString = str(stone)
                stonesBuffer.append(int(stoneString[:len(stoneString) // 2]))
                stonesBuffer.append(int(stoneString[len(stoneString) // 2:]))
            else:
                stonesBuffer.append(int(stone) * 2024)
        #print(stonesBuffer)
        stones = [stone for stone in stonesBuffer]
        #input()
    return len(stones)

# part1 = bruteforce(stones,25)
# print(part1)

transforms = {0:[1],}

stones_ = [stone for stone in stones]
stones = {stone : stones.count(stone) for stone in stones}

count = 1
while count <= 75:
    stonesBuffer = {}
    for stone in stones.keys():
        result = []
        if stone in transforms.keys():
            result.extend(transforms[stone])
        else:
            if len(str(stone)) % 2 == 0:
                stoneString = str(stone)
                result = [int(stoneString[:len(stoneString) // 2]), int(stoneString[len(stoneString) // 2:])]
                transforms[stone] = result
            else:
                result = [stone * 2024]
                transforms[stone] = result
        for r in result:
            if r in stonesBuffer.keys():
                stonesBuffer[r] += stones[stone]
            else:
                stonesBuffer[r] = stones[stone]
    stones = {stone:stonesBuffer[stone] for stone in stonesBuffer.keys()}   
    count += 1
    #input()
print(sum([stones[stone] for stone in stones.keys()]))
#things can either -> become 1, split in half, or multiply by 2024
#all 0s become 1s, all 1s become 2024, all 2024s become 20 and 24
#   all 20s become 2 and 0, all 24s become 2 and 4
#   all 2s become 4048, all 4s become 8096
#   all 4048s become 40 and 48
#   all 8096s become 80 and 96
#   all 40s become 4 and 0, all 48s become 4 and 8
#   all 80s become 8 and 0, all 96s become 9 and 6
#   all 8s become 16192, all 9s become 18216, all 6s become 12144