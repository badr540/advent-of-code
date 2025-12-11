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

def get_green_squares(points):
    pointsY = {}
    pointsX = {}
    
    edges = [[] for i in range(len(points))]

    green_squares = []
    for i in range(len(points)):
        pa = points[i]
        pb = points[i+1 % len(points)]
        if pa[0] not in pointsX:
            pointsX[pa[0]] = []
        if pa[1] not in pointsX:
            pointsX[pa[1]] = [] 
        
        edges[i].append(pb)
        edges[i+1 % len(points)].append(pa)
        





print(get_largest_area(read_file("input.txt")))