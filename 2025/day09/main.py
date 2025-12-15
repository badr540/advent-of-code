import math

def read_file(filename):
    points = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            vec = tuple(map(lambda x: int(x), line.strip().split(',')))
            points.append(vec)
    
    return points

def get_largest_area(points):
    maxarea = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            w = abs(points[i][0] - points[j][0]) + 1
            h = abs(points[i][1] - points[j][1]) + 1
            maxarea = max(maxarea, w*h)
    return maxarea

# part 2

def outer_floodfill(grid, fillval):
    grid = [[0] * (len(grid[0]) + 2)] + [[0] + row + [0] for row in grid] + [[0] * (len(grid[0]) + 2)]

    queue = [[0,0]]

    while(len(queue) > 0):
        x,y = queue.pop(0)
        for tx, ty in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
            if tx < 0 or ty < 0 or tx >= len(grid) or ty >= len(grid[0]): continue
            if grid[tx][ty] == grid[x][y] and [tx,ty] not in queue:
                queue.append([tx,ty])
        
        grid[x][y] = fillval

    return [row[1:-1] for row in grid[1:-1]]


def bbox_contains_val(grid, x1, y1, x2, y2, val):
    for x in range(x1, x2+1):
        for y in range(y1,y2+1):
            if grid[x][y] == val: return True

    return False

    

def get_largest_area_inside_loop(points):
    xs = sorted({x for x, _ in points})
    ys = sorted({y for _, y in points})

    x_sizes = {}
    y_sizes = {}
    for i, (x1, x2) in enumerate(zip(xs, xs[1:])):
        x_sizes[i * 2 + 1] = x2 - x1 - 1 

    for i, (y1, y2) in enumerate(zip(ys, ys[1:])):
        y_sizes[i * 2 + 1] = y2 - y1 - 1     
    
    grid = [[0] * (len(ys) * 2 - 1) for i in range(len(xs) * 2 -1)]


    for (x1, y1), (x2,y2) in zip(points, points[1:] + points[:1]):
        cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
        cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
        for cx in range(cx1,cx2 + 1):
            for cy in range(cy1, cy2+1):
                grid[cx][cy] = 1

    grid = outer_floodfill(grid,-1)

    maxarea = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):            
            p1 = points[i]
            p2 = points[j]
            w = abs(p1[0] - p2[0]) + 1
            h = abs(p1[1] - p2[1]) + 1
            currarea = w*h
            x1, x2 = sorted([xs.index(p1[0]) * 2, xs.index(p2[0]) * 2])
            y1, y2 = sorted([ys.index(p1[1]) * 2, ys.index(p2[1]) * 2])

            if currarea > maxarea and not bbox_contains_val(grid, x1, y1, x2, y2, -1):
                maxarea = currarea
    return maxarea

print("part 1", get_largest_area(read_file("input.txt")))
print("part 1", get_largest_area_inside_loop(read_file("input.txt")))
