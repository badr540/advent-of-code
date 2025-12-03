def read_file(filename):
    IDs = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            IDs += line.strip().strip(",").split(',')
    return IDs

# part 1
def is_ID_invalid(ID):
    r = len(ID) // 2
    if(ID[:r] == ID[r:]):
        return True
    return False

def calculate_invalid_IDs(ID_ranges):
    total = 0
    for ID_range in ID_ranges:
        [s, e] = ID_range.split('-')
        s = int(s)
        e = int(e)
        for ID in range(s, e+1):
            if is_ID_invalid(str(ID)):
                total += ID

    return total

# part 2
def is_ID_invalid2(ID):
    r = len(ID) // 2
    for i in range(1,r+1):
        s = ID.split(ID[:i])
        if len(list(filter(lambda x: len(x) != 0, s))) == 0:
            return True
    return False

def calculate_invalid_IDs2(ID_ranges):
    total = 0
    for ID_range in ID_ranges:
        [s, e] = ID_range.split('-')
        s = int(s)
        e = int(e)
        for ID in range(s, e+1):
            if is_ID_invalid2(str(ID)):
                total += ID

    return total

print("part 1:", calculate_invalid_IDs(read_file("input.txt")))
print("part 1:", calculate_invalid_IDs2(read_file("input.txt")))
