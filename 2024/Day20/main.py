import os
import time
from PIL import Image
import numpy as np
obsticles = []
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


def score_path(maze,start,end):
    mazescores = [[float('inf') for y in range(len(maze[0]))] for x in range(len(maze))]
    mazescores[start[0]][start[1]] = 0
    dirs =  [[-1,0],[0,1],[1,0],[0,-1]]
    queue = [start]
    
    while(len(queue)!=0):
        x,y = queue.pop(0)
        for dir in dirs:
            if mazescores[x+dir[0]][y+dir[1]] > mazescores[x][y] + 1 and maze[x+dir[0]][y+dir[1]] != '#':
                if maze[x+dir[0]][y+dir[1]] == 'X':
                    if [x+dir[0],y+dir[1]] not in obsticles:
                        obsticles.append([x+dir[0],y+dir[1]])
                else:
                    queue.append([x+dir[0],y+dir[1]])
                    mazescores[x+dir[0]][y+dir[1]] = mazescores[x][y] + 1

    return mazescores


def find_steps_saved_with_cheats(maze,mazescores,cheats,start, cheats_scores):  
    
    dirs =  [[-1,0],[0,1],[1,0],[0,-1]]
    queue = [start]
    cheatsqueue = [cheats]
    while(len(queue)!=0):
        x,y = queue.pop(0)
        c_cheats = cheatsqueue.pop(0)
        for dir in dirs:
            if mazescores[x+dir[0]][y+dir[1]] > mazescores[x][y] + 1 and maze[x+dir[0]][y+dir[1]] != '#' and c_cheats > 0:
                
                if mazescores[x+dir[0]][y+dir[1]] != float('inf'):
                    saved = mazescores[x+dir[0]][y+dir[1]] - (mazescores[x][y] + 1)
                    key = (tuple(start), (x+dir[0], y+dir[1]))
                    cheats_scores[key] = saved
                    
                mazescores[x+dir[0]][y+dir[1]] = mazescores[x][y] + 1
                queue.append([x+dir[0],y+dir[1]])
                cheatsqueue.append(c_cheats-1)


def find_steps_saved_with_cheats(mazescores,start,cheats,cheats_scores):
    x,y = start
    startscore = mazescores[x][y]
    for i in range(-cheats,cheats+1):
        c = cheats - abs(i)
        for j in range(-c,c+1):
            if i == j == 0: continue
            if x+i >= len(mazescores) or x+i < 0 or y+j >= len(mazescores[0]) or y+j < 0: continue
            
            if mazescores[x+i][y+j] != float('inf'):
                key = (tuple(start), (x+i,y+j))

                cheats_scores[key] = mazescores[x+i][y+j] - (startscore + abs(i)+ abs(j))
            
             

maze = []
starts = []
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        maze.append(list(line.rstrip('\n')))

for x in range(1,len(maze)-1):
    for y in range(1,len(maze[x])-1):
        if maze[x][y] == '#':
            maze[x][y] = 'X'
        else:
            starts.append([x,y])

s,e = find_start_and_end(maze)


start = time.time()
mazescores = score_path(maze,s,e)
base_score = mazescores[e[0]][e[1]]
cheats_scores = {}
total = 0
find_steps_saved_with_cheats(mazescores,[1,3],20,cheats_scores)

for i in range(len(starts)):
    mazescorescpy = [row[:] for row in mazescores]
    find_steps_saved_with_cheats(mazescorescpy,starts[i],20, cheats_scores)

for val in cheats_scores.values():
    if val >= 100:
        total +=1 
print(total)

end = time.time()
print(end - start)

#884928-884928
#944910