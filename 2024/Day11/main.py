import os
import time
blinks = 25
DP = dict()

def solve(stones, blinks):   
    if not isinstance(stones,list):
        stones = [stones]
    levels = []
    for i in range(blinks):
        for j in reversed(range(len(stones))):
            if int(stones[j]) == 0:
                stones[j] = str(1)
            elif len(stones[j]) % 2 == 0:
                left = stones[j][:int(len(stones[j])/2)]
                right = stones[j][int(len(stones[j])/2):].lstrip('0')
                if right == '':
                    right = '0'
                stones[j] = right
                stones.insert(j,left)
            else:
                stones[j] = str(int(stones[j]) * 2024)
        levels.append(stones)
        
    return levels

def solveP2(stones, blinks):   
    if not isinstance(stones,list):
        stones = [stones]
    levels = []
    for j in reversed(range(len(stones))):
        
        if int(stones[j]) == 0:
            stones[j] = str(1)
        elif len(stones[j]) % 2 == 0:
            left = stones[j][:int(len(stones[j])/2)]
            right = stones[j][int(len(stones[j])/2):].lstrip('0')
            if right == '':
                right = '0'
            stones[j] = right
            stones.insert(j,left)
        else:
            stones[j] = str(int(stones[j]) * 2024)
    
    return stones


def solve_DP(stone,blinks,DP):
    if stone in DP.keys():
        b = len(DP[stone]) - blinks
        if b < 0:
            level = []
            for i in range(abs(b)):
                DP[stone].append([])
            for s in DP[stone][-2]:
                for i in range(abs(b)):
                    DP[stone][blinks-abs(b)+i] += DP[s][i]
        else:
            return DP[stone][blinks-1]
    else:
        DP[stone] = solveP2(stone,blinks)
        return DP[stone][blinks-1]
            
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        stones = line.rstrip('\n').split(' ')

start = time.time()
l = []
for s in stones:
    l += solve_DP(s,blinks,DP)

print(len(l))

end = time.time()
print(end - start)

start = time.time()
levels = solve(stones,blinks)
print(len(levels[blinks-1]))
end = time.time()
print(end - start)


#194482
#2.3786797523498535


#2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
