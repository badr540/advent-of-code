
def find_total_distance_between_lists(l1, l2):
    total_distance = 0;
    l2.sort()
    number_frequencies = dict();

    for i in l2:
        if(number_frequencies.get(str(i)) == None):
            number_frequencies[str(i)] = 1;
        else:
            number_frequencies[str(i)] += 1


    for i in l1:
        freq = number_frequencies.get(str(i));
        freq = 0 if freq == None else freq

        total_distance+= i * freq
    return total_distance;

def read_lists_from_file(filename):
    l1 = []
    l2 = []
    with open(filename, 'r') as file:
        for line in file:
            l1.append(int(line.strip().split(" ")[0]))
            l2.append(int(line.strip().split(" ")[3]))
        
    return l1, l2

l1,l2 = read_lists_from_file("Day1/input.txt")
print(find_total_distance_between_lists(l1,l2))