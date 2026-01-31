def read_file(filename):
    shapes = []
    queries = []
    with open(filename, 'r', encoding='utf-8') as f:
        currShape = []
        for line in f.readlines():
            if "x" in line:
                size = []
                for x in line.split(":")[0].split("x"):
                    size.append(int(x))
                indexes = [int(x) for x in line.split(":")[1].strip().split(" ")]
                queries.append([size, indexes])
            if line == '\n':
                shapes.append(currShape)
                currShape = []
            if "#" in line or "." in line:
                currShape.append(line.strip())
            
    return [shapes, queries]


def solve_p1(shapes, queries):
    total = 0
    for size, indexes in queries:
        sumindexes = sum(indexes)
        if (size[0] // 3) * (size[1] // 3) >= sumindexes:
            total += 1
    return total

shapes, queries = read_file("input.txt")
print(solve_p1(shapes, queries))