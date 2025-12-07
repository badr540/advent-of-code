def read_file(filename):
    diagram = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            diagram.append(list(line.strip()))
    return diagram

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


def calculate_timelines(diagram):
    timelines = 1
    for i in range(1, len(diagram)):
        for j in range(len(diagram[0])):
            if diagram[i-1][j] == 'S' or diagram[i-1][j] == '|' and diagram[i][j] != '^':
                diagram[i][j] = '|'
            elif diagram[i][j] == '^' and diagram[i-1][j] == '|':
                if j > 0 and diagram[i][j-1] == '.': 
                    diagram[i][j-1] = '|'
                    timelines += 1
                if j < len(diagram[i])-1 and diagram[i][j+1] == '.': 
                    diagram[i][j+1] = '|'
                    timelines += 1

    return timelines

print("part 1:", calculate_splits(read_file("input.txt")))
print("part 2:", calculate_timelines(read_file("input.txt")))