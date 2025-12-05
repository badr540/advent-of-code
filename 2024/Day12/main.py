import os
import time
def find_garden_area_and_perimeter(map,visited,x,y):
    area = 0
    perimeter = 0
    #part 2
    usides = []
    dsides = []
    lsides = []
    rsides = []
    queue = [[x,y]]
    x,y = 0,0
    while(len(queue) > 0):
        x,y = queue.pop(0)
        if visited[x][y] == True:
            print("error")
        visited[x][y] = True
        area += 1
        for offset in [[-1,0], [1,0], [0,-1], [0,1]]:
            xs = x + offset[0]
            ys = y + offset[1]
            if xs < 0 or xs >= len(map) or  ys < 0 or ys >= len(map[x]) or map[xs][ys] != map[x][y]:
                
                    if offset[0] == -1:
                        usides.append([xs,ys])
                        if [xs,ys+1] not in usides and [xs,ys-1] not in usides:
                            perimeter += 1
                    if offset[0] == 1:
                        dsides.append([xs,ys])
                        if [xs,ys+1] not in dsides and [xs,ys-1] not in dsides:
                            perimeter += 1
                    if offset[1] == -1:
                        lsides.append([xs,ys])
                        if [xs+1,ys] not in lsides and [xs-1,ys] not in lsides:
                            perimeter += 1
                    if offset[1] == 1:
                        rsides.append([xs,ys])
                        if [xs+1,ys] not in rsides and [xs-1,ys] not in rsides:
                            perimeter += 1

            elif not visited[xs][ys] and [xs,ys] not in queue:
                queue.append([xs,ys])

    #for i in reversed(range(len(sides))):
    #    
    #    side = sides[i]
    #    for offset in [[-1,0], [1,0], [0,-1], [0,1]]:
    #        s = side
    #        while [s[0] + offset[0], s[1] + offset[1]] in sides :
    #            s = sides.pop(sides.index([s[0] + offset[0], s[1] + offset[1]]))
    #    perimeter += 1
        
    return [area,perimeter]

def calculate_fencing_prices(map):
    gardens = dict() 
    visited = [[False for i in map[0]] for i in map]
    total = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if not visited[x][y]:
                area,perimeter = find_garden_area_and_perimeter(map,visited,x,y)
                total += area*perimeter 

    return total

            
map = []
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        map.append(line.rstrip('\n'))

start = time.time()

print(calculate_fencing_prices(map))
end = time.time()
print(end - start)
