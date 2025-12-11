import math

def read_file(filename):
    points = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            vec = tuple(map(lambda x: int(x), line.strip().split(',')))
            points.append(vec)
    
    return points

def get_dist(p, q):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p, q)))

def root(x, parents):
    if parents[x] == x:
        return x
    
    parents[x] = root(parents[x], parents)
    return parents[x]

def merge(a, b, parents):
    parents[root(a, parents)] = root(b, parents)

def is_one_group(parents):
    g = root(0, parents)
    for p in parents:
        if root(p, parents) != g:
            return False
    return True


def build_circuts(points, n_con):
    edges = []
    parents = [i for i in range(len(points))]

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if i == j: continue
            edges.append([i, j])
    
    edges = sorted(edges, key=lambda x: get_dist(points[x[0]], points[x[1]]))
    for a, b in edges[:n_con]:
        merge(a,b, parents)
    
    sizes = [0 for i in range(len(points))]
    for i in range(len(points)):
        sizes[root(i, parents)] += 1
    sizes = sorted(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]


def get_cable_size(points):
    edges = []
    parents = [i for i in range(len(points))]

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if i == j: continue
            edges.append([i, j])
    
    edges = sorted(edges, key=lambda x: get_dist(points[x[0]], points[x[1]]))
    for a, b in edges:
        merge(a,b, parents)

        if is_one_group(parents):
            return points[a][0] * points[b][0]


print("part 1:", build_circuts(read_file("input.txt"),1000))


print("part 2:", get_cable_size(read_file("input.txt")))


