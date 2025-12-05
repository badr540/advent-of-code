dirs = [[-1,0], [0,1],[1,0], [0,-1]]
oreintations = ['^', '>', 'v', '<']
obsticles = []

def find_guard(map_list):
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] in oreintations:
                return i, j
    return None

def predict_guard_movement(x,y, map_list):
    steps = 1 
    dir_idx = oreintations.index(map_list[x][y])
    next_step = [x+dirs[dir_idx][0], y+dirs[dir_idx][1]]
    while(next_step[0] < len(map_list) and next_step[0] >= 0 and next_step[1] < len(map_list[0]) and next_step[1] >= 0):
        
        
        if (map_list[next_step[0]][next_step[1]] == '#'):
            dir_idx = (dir_idx+1)%len(dirs)
            map_list[x][y] = '+'
        else:
            x += dirs[dir_idx][0]
            y += dirs[dir_idx][1]
            steps+=1
            map_list[x][y] = 'X'

            
        
        next_step = [x+dirs[dir_idx][0], y+dirs[dir_idx][1]]

            
    return steps

def find_loops_in_path(x,y, map_list):
    loops = 0 
    dir_idx = oreintations.index(map_list[x][y])
    map_list[x][y] = '.'
    next_step = [x+dirs[dir_idx][0], y+dirs[dir_idx][1]]
    steps = 0
    while(next_step[0] < len(map_list) and next_step[0] >= 0 and next_step[1] < len(map_list[0]) and next_step[1] >= 0):
        if map_list[ x + dirs[dir_idx][0]][y + dirs[dir_idx][1]] == '.':
            map_list[ x + dirs[dir_idx][0]][y + dirs[dir_idx][1]] = '#'
            
            if is_loop(x, y, map_list, dir_idx):
                loops+=1
                
            map_list[ x + dirs[dir_idx][0]][y + dirs[dir_idx][1]] = '.'
        
        if (map_list[next_step[0]][next_step[1]] == '#'):
            dir_idx = (dir_idx+1)%len(dirs)
        else:
            x += dirs[dir_idx][0]
            y += dirs[dir_idx][1]
            steps +=1
            map_list[x][y] = oreintations[dir_idx]
        
        
        #adj_obsticle = None
        #for i in range(len(obsticles)):
        #    if dir_idx == 0:
        #        if obsticles[i][1] == y and obsticles[i][0] < x:
        #            if adj_obsticle != None and abs(adj_obsticle[0]-x) > abs(obsticles[0]-x) or abs(adj_obsticle[1]-y) > abs(obsticles[1]-y):
        #                adj_obsticle = obsticles[i]
        #    elif dir_idx == 1:
        #        if obsticles[i][1] > y and obsticles[i][0] == x:
        #            if adj_obsticle != None and abs(adj_obsticle[0]-x) > abs(obsticles[0]-x) or abs(adj_obsticle[1]-y) > abs(obsticles[1]-y):
        #                adj_obsticle = obsticles[i]
        #    elif dir_idx == 2:
        #        if obsticles[i][1] == y and obsticles[i][0] > x:
        #            if adj_obsticle != None and abs(adj_obsticle[0]-x) > abs(obsticles[0]-x) or abs(adj_obsticle[1]-y) > abs(obsticles[1]-y):
        #                adj_obsticle = obsticles[i]
        #    elif dir_idx == 3:
        #        if obsticles[i][1] < y and obsticles[i][0] == x:
        #            if adj_obsticle != None and abs(adj_obsticle[0]-x) > abs(obsticles[0]-x) or abs(adj_obsticle[1]-y) > abs(obsticles[1]-y):
        #                adj_obsticle = obsticles[i]
        #
        #if adj_obsticle != None and is_loop(x, y, map_list, (dir+1)%4, adj_obsticle):
        #    loops+=1
            
        next_step = [x+dirs[dir_idx][0], y+dirs[dir_idx][1]]

    print("steps: {}".format(steps))
    return loops

def find_all_obsticles(map_list):
    for x in range(len(map_list)):
        for y in range(len(map_list[x])):
            if map_list[x][y] == '#':
                obsticles.append([x,y])

def fill_adj_list(obsticles):
    obst = obsticles.copy()
    adj_list = dict()
    while(len(obst) > 0):
        idx = len(obst) - 1
        up = None
        left = None
        right = None
        down = None
        if idx in adj_list.keys():
            up = adj_list[idx][0]
            right = adj_list[idx][1]
            down = adj_list[idx][2]
            left = adj_list[idx][3]
            
        for i in range(idx):
            # check if adjectent 
            if obst[i][0] < obst[idx][0] and obst[i][1] == obst[idx][1]+1:
                if up == None or (obst[idx][0] - obst[up][0]) <  (obst[idx][0] - obst[i][0]):
                    up = i
            
            if obst[i][1] > obst[idx][1] and obst[i][0] == obst[idx][0]+1:
                if right == None or (obst[right][1] - obst[idx][1]) <  (obst[i][1] - obst[idx][1]):
                    right = i
                    
            if obst[i][0] > obst[idx][0] and obst[i][1] == obst[idx][1]-1:
                if down == None or (obst[down][0] - obst[idx][0]) <  (obst[i][0] - obst[idx][0]):
                    down = i
            
            if obst[i][1] < obst[idx][1] and obst[i][0] == obst[idx][0]-1:
                if left == None or (obst[idx][1] - obst[left][1]) <  (obst[idx][1] - obst[i][1]):
                    left = i

        adj_list[idx] = [up, right, down, left]
        
        for i in range(len(adj_list[idx])):
            key = adj_list[idx][i]
            if  key in adj_list.keys():
                adj_list[key][(i-2 % 4)] = idx
            elif key != None:
                adj_list[key] = [None, None, None, None]
                adj_list[key][(i-2 % 4)] = idx

            
        obst.pop(-1)    
    
    return adj_list 
        
                        
def is_loop(x, y, map_list, dir):
    dir_idx = dir
    next_step = [x+dirs[dir_idx][0], y+dirs[dir_idx][1]]
    turns = []
    turn_dirs = []
    while(next_step[0] < len(map_list) and next_step[0] >= 0 and next_step[1] < len(map_list[0]) and next_step[1] >= 0):
        
        #map_list[x][y] = oreintations[dir_idx]
        #print("========")
        #for i in map_list:
        #    print("".join(i))
        #map_list[x][y] = '.'
        
        if (map_list[next_step[0]][next_step[1]] == '#'):
            turn_dirs.append(dir_idx)
            turns.append([x,y])
            dir_idx = (dir_idx+1)%len(dirs)
        else:
            x += dirs[dir_idx][0]
            y += dirs[dir_idx][1]
            if [x,y] in turns and turn_dirs[turns.index([x,y])] == dir_idx:
                return True

            
        
        next_step = [x+dirs[dir_idx][0], y+dirs[dir_idx][1]]
            
    return False

def find_loops(adj_list, map_list):
    counter = 0
    for i in adj_list.keys():
        for j in range(len(adj_list[i])):
            steps = []
            last_node = i 
            dir = j
            curr_node = adj_list[i][dir]
            while (curr_node != None and curr_node not in steps):
                last_node = curr_node
                steps.append(last_node)
                dir = (dir+1) % 4
                curr_node = adj_list[last_node][dir]
            
                if dir == (j+2) % 4 and last_node != i:
                    if dir == 0:
                        if obsticles[i][0] -1 >= 0 and obsticles[last_node][1] + 1 < len(map_list):
                            point = [obsticles[i][0] -1, obsticles[last_node][1] + 1 ]
                            map_list[point[0]][point[1]] = oreintations[dir]

                    elif dir == 1:
                        if obsticles[last_node][0] +1 < len(map_list) and obsticles[i][1] + 1 < len(map_list[0]):
                            point = [obsticles[last_node][0] +1,obsticles[i][1] + 1]
                            map_list[point[0]][point[1]] = oreintations[dir]

                    elif dir == 2:
                        if obsticles[i][0] + 1 < len(map_list) and obsticles[last_node][1] -1 >= 0:
                            point = [obsticles[i][0] + 1, obsticles[last_node][1] -1]
                            map_list[point[0]][point[1]] = oreintations[dir]
                        # last.x+1 < len(map)
                        # firstpoint.y -1 >= 0
                    elif dir == 3:
                        if obsticles[i][1] - 1 >= 0 and obsticles[last_node][0] - 1 >= 0:
                            point = [obsticles[last_node][0] - 1, obsticles[i][1] - 1]
                            map_list[point[0]][point[1]] = oreintations[dir]

                        # firstpont.x -1 >= 0
                        # lastpoint.y +1 < len(map)


    return map_list
    
    

filename = "Day6/input.txt"
map_list = []
total = 0
with open(filename, 'r') as file:
    for line in file:
        map_list.append(list(line.rstrip("\n")))

x,y = find_guard(map_list)
#find_all_obsticles(map_list)
#map_list = find_loops(fill_adj_list(obsticles),map_list)
print(find_loops_in_path(x,y,map_list))


#[0,4] <- [9,6]

#[3,2] <- [9,6]

#j = 1
#dir == 2
steps = 5853
1957