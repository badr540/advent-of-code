import os
import time
from PIL import Image
import numpy as np

def find_start_and_end(maze):
    start = []
    end = []
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == 'E':
                end = [x,y]
            if maze[x][y] == 'S':
                start = [x,y]
    
    return start,end


def find_the_shortest_path(maze,start,end):
    mazescores = [[float('inf') for y in range(len(maze[0]))] for x in range(len(maze))]
    mazescores[start[0]][start[1]] = 0
    dirs =  [[-1,0],[0,1],[1,0],[0,-1]]
    orient = ['^','>','v','<']
    cdir = [0,1]
    queue = [start]
    queuedirs = [cdir]
    
    while(len(queue)!=0):
        x,y = queue.pop(0)
        cdir = queuedirs.pop(0)
        maze[x][y] = orient[dirs.index(cdir)]
        for dir in dirs:
            nextstep = 1001 if dir != cdir else 1
            if mazescores[x+dir[0]][y+dir[1]] > mazescores[x][y] + nextstep and maze[x+dir[0]][y+dir[1]] != '#':
                mazescores[x+dir[0]][y+dir[1]] = mazescores[x][y] + nextstep
                if [x+dir[0],y+dir[1]] in queue:
                    queuedirs[queue.index([x+dir[0],y+dir[1]])] = dir
                else:
                    queue.append([x+dir[0],y+dir[1]])
                    queuedirs.append(dir)
    return mazescores

def total_tiles_in_the_best_path(mazescores,maze,end):
    total = 0
    tiles = []
    queue = [end]
    flagqueue = []
    flagqueue.append(True)
    changed = []
    dirs =  [[-1,0],[0,1],[1,0],[0,-1]]
    mazecpy =  [row[:] for row in maze]
    while(len(queue) != 0):
        x,y = queue.pop(0)
        is_turn = flagqueue.pop(0)
        mazecpy[x][y] = 'O'
        if [x,y] in tiles:
            continue
        tiles.append([x,y])
        
        if mazescores[x][y] == 70364:
            print("test")
        for dir in dirs:
            if  [x+dir[0],y+dir[1]] not in tiles:

                if mazescores[x+dir[0]][y+dir[1]]+1 == mazescores[x][y] and (is_turn or maze[x][y] == maze[x+dir[0]][y+dir[1]]):
                    queue.append([x+dir[0],y+dir[1]])
                    flagqueue.append(False)
                    continue
                if mazescores[x+dir[0]][y+dir[1]]+1001 == mazescores[x][y]:
                    queue.append([x+dir[0],y+dir[1]])
                    flagqueue.append(True)
                    
                    
                mirrordir = dirs[(dirs.index(dir)+2)%4]
                if maze[x+dir[0]][y+dir[1]] != '#' and maze[x+mirrordir[0]][y+mirrordir[1]] != '#' :
                    if mazescores[x+dir[0]][y+dir[1]] <= mazescores[x+mirrordir[0]][y+mirrordir[1]] - 2  and maze[x+dir[0]][y+dir[1]] == maze[x+mirrordir[0]][y+mirrordir[1]]:
                        queue.append([x+dir[0],y+dir[1]])
                        flagqueue.append(False)
                        
        
    tiles = []
    queue = [end]
    flagqueue = []
    flagqueue.append(True)
    while(len(queue) != 0):
        x,y = queue.pop(0)
        is_turn = flagqueue.pop(0)
        mazecpy[x][y] = 'O'
        if [x,y] in tiles:
            continue
        tiles.append([x,y])
        
        if mazescores[x][y] == 70364:
            print("test")
        for dir in dirs:
            if  [x+dir[0],y+dir[1]] not in tiles:

                if mazescores[x+dir[0]][y+dir[1]]+1 == mazescores[x][y] and (is_turn or maze[x][y] == maze[x+dir[0]][y+dir[1]]):
                    queue.append([x+dir[0],y+dir[1]])
                    flagqueue.append(False)
                    continue
                elif mazescores[x+dir[0]][y+dir[1]]+1001 == mazescores[x][y]:
                    queue.append([x+dir[0],y+dir[1]])
                    flagqueue.append(True)
                    continue
                elif is_turn and mazescores[x+dir[0]][y+dir[1]]+1 == mazescores[x][y]+1000 and mazecpy[x+dir[0]][y+dir[1]] == 'O':
                    queue.append([x+dir[0],y+dir[1]])
                    flagqueue.append(False)

    
    for l,l2 in zip(mazecpy,mazescores):
        for c1,c2 in zip(l,l2):
            print(c1+"-" +str(c2).ljust(6), end='')
        print('')
    for l in mazecpy:
        print("".join(l))

    return len(tiles)
maze = []
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        maze.append(list(line.rstrip('\n')))
        
s = [len(maze)-2,1]
e = [1,len(maze[0])-2]


start = time.time()
mazescores = find_the_shortest_path(maze,s,e)
print(mazescores[e[0]][e[1]])
print(total_tiles_in_the_best_path(mazescores,maze,e))

    

end = time.time()
print(end - start)

#561 too high 
#489 lowest