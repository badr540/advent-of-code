def read_file(filename):
    fresh = []
    available = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if('-' in line):
                l,r = line.strip().split('-')
                fresh.append([int(l), int(r)])
            elif line != "\n":
                available.append(int(line.strip()))
    return fresh, available

def combine_overlapping_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    combined = [ranges[0]]
    for i in range(1, len(ranges)):
        if combined[-1][1] >= ranges[i][0]:
            combined[-1] = [combined[-1][0], max(combined[-1][1], ranges[i][1])]
        else:
            combined.append(ranges[i])
    
    return combined

# part 1
def count_fresh_available_ingredients(fresh, available):
    count = 0
    for ing_ID in available:
        for fresh_range in fresh:
            if ing_ID >= fresh_range[0] and ing_ID <= fresh_range[1]:
                count+= 1
                break
    
    return count

# part 2
def count_fresh_ingredients(fresh):
    count = 0
    for fresh_range in fresh:
        count += (fresh_range[1] - fresh_range[0]) + 1
    
    return count

fresh, available = read_file("input.txt")
fresh = combine_overlapping_ranges(fresh)

print("part 1:",count_fresh_available_ingredients(fresh, available))

print("part 2:",count_fresh_ingredients(fresh))