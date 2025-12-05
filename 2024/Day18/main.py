import os
import time
from PIL import Image
import numpy as np


def find_the_shortest_path(maze,start,end):
    mazescores = [[float('inf') for y in range(len(maze[0]))] for x in range(len(maze))]
    mazescores[start[0]][start[1]] = 0
    dirs =  [[-1,0],[0,1],[1,0],[0,-1]]
    queue = [start]
    
    while(len(queue)!=0):
        x,y = queue.pop(0)
        for dir in dirs:
            if  0 > x+dir[0] or x+dir[0] >= len(maze) or 0 > y+dir[1] or y+dir[1] >= len(maze[x]):
                continue
            
            if mazescores[x+dir[0]][y+dir[1]] > mazescores[x][y] + 1 and maze[x+dir[0]][y+dir[1]] != '#':
                mazescores[x+dir[0]][y+dir[1]] = mazescores[x][y] + 1
                queue.append([x+dir[0],y+dir[1]])
                
    return mazescores  

def find_uncorrupted_path(w,h,nbytes,bytes):
    memory = [['.' for x in range(w)] for y in range(h)]
    for i in range(nbytes):
        x,y = bytes[i]
        memory[y][x] = '#'
    
    memscore = find_the_shortest_path(memory,[0,0], [w-1,h-1])
    
    return memscore[h-1][w-1]

filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
bytes = []

with open(filename, 'r') as file:
    for line in file:
        bytes.append(list(map(int,line.strip('\n').split(','))))
        


start = time.time()

nbytes = 12
output = 0
while output != float('inf'):
    nbytes += 1
    output = find_uncorrupted_path(71,71,nbytes,bytes)

print(bytes[nbytes-1])

end = time.time()
print(end - start)



#0,3, A = A/2^3
#5,4, print A%8
#3,0 jump to 0