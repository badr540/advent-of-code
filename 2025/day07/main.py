def read_file(filename):
    diagram = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            diagram.append(list(line.strip()))
    return diagram


# part 1
def calculate_splits(diagram):
    splits = 0
    for i in range(1, len(diagram)):
        for j in range(len(diagram[0])):
            if diagram[i-1][j] == 'S' or diagram[i-1][j] == '|' and diagram[i][j] != '^':
                diagram[i][j] = '|'
            elif diagram[i][j] == '^' and diagram[i-1][j] == '|':
                splits+=1
                if j > 0 and diagram[i][j-1] == '.': diagram[i][j-1] = '|'
                if j < len(diagram[i])-1 and diagram[i][j+1] == '.': diagram[i][j+1] = '|'

    return splits

# part 2

def calculate_timelines(diagram):
    for i in range(len(diagram)):
        for j in range(len(diagram[0])):
            if diagram[i][j] == '.':
                diagram[i][j] = 0
            if diagram[i][j] == 'S':
                diagram[i][j] = 1

    for i in range(1, len(diagram)):
        for j in range(len(diagram[0])):

            if diagram[i][j] == '^':
                if j > 0: 
                    diagram[i][j-1] += diagram[i-1][j]
                if j < len(diagram[i])-1: 
                    diagram[i][j+1] += diagram[i-1][j]
            elif isinstance(diagram[i-1][j], int):
                diagram[i][j] += diagram[i-1][j]

    return sum(list(filter(lambda x: isinstance(x, int),diagram[-1])))


print("part 1:", calculate_splits(read_file("input.txt")))
print("part 2:", calculate_timelines(read_file("input.txt")))


