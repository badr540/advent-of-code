def find_all_trailheads(map):
    trailheads = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '0':
                trailheads.append([i,j])
    
    return trailheads

def search(map,x,y, level):
    res = []
    if map[x][y] == '9':
        res.append([x,y])
        return res
    for i in [[-1,0], [1,0],[0,-1], [0,1]]:
        
        if 0 <= x + i[0] < len(map) and 0 <= y +i[1] < len(map[0]) and map[x + i[0]][y + i[1]] == str(level+1):
            vec = search(map, x +i[0], y+i[1], level+1)
            
            if len(vec) == 0 :
                continue
        
            if isinstance(vec[0], list):
                res += vec
            else:
                res.append(vec)
                
    return res
            
            
def score_trailhead(map, trailhead):
    x = trailhead[0]
    y = trailhead[1]
    trailends = search(map, x,y, 0)
    
    return len(trailends)
    
    
map = []
filename = "Day10/input.txt"
with open(filename, 'r') as file:
    for line in file:
        map.append(line.rstrip("\n"))

trailheads = find_all_trailheads(map)

total = 0
for t in trailheads:
    total += score_trailhead(map, t)

print(total)