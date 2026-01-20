def read_file(filename):
    conns = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            key = line.split(":")[0]
            vals = line.split(":")[1].strip().split(" " )
            conns[key] = vals            
    return conns

def calculate_paths_p1(conns):
    visited = {}
    visited["out"] = 1
    def search(curr):
        nonlocal visited, conns
        if curr == "out":
            return 1
        
        currval = 0
        for con in conns[curr]:
            if con not in visited:
                currval += search(con)
            else:
                currval += visited[con]

        visited[curr] = currval
        return visited[curr]
    
        
    return search("you")


def calculate_paths_p2(conns):
    visited = {}

    def search(curr, dst):
        nonlocal conns, visited

        if curr == dst:
            return 1
        if curr not in conns: 
            return 0

        currval = 0
        for con in conns[curr]:
            if (con, dst) not in visited:
                currval += search(con, dst)
            else:
                currval += visited[(con, dst)]

        visited[(curr, dst)] = currval

        return visited[(curr, dst)]

    return (
        search("svr", "fft") * search("fft", "dac") * search("dac", "out")
        + search("svr", "dac") * search("dac", "fft") * search("fft", "out")
    )


#print("part 1: ", calculate_paths_p1(read_file("input.txt")))

print("part 2: ", calculate_paths_p2(read_file("input.txt")))