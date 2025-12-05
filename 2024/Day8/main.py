def is_point_inline_area(x1, y1, x2, y2, x, y):
    # Calculate the determinant-based area
    area = x1 * (y2 - y) + x2 * (y - y1) + x * (y1 - y2)
    return area == 0

def find_all_antenna_pairs(map):
    pairs = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            for k in range(len(map)):
                for l in range(len(map[k])):
                    if i == k and j == l:
                        continue
                    if map[i][j] != '.' and map[i][j] == map[k][l]:
                        pairs.append([(i,j), (k,l)])

    return pairs

def remove_dedundant_pairs(pairs):
    
    for i in range(int(len(pairs)/2)):
        for j in range(len(pairs)):
            if pairs[i][0] == pairs[j][1] and pairs[i][1] == pairs[j][0]:
                pairs.pop(i)
                break
    
    return pairs

def place_antinodes(pairs, map):
    total = 0
    for pair in pairs:
        P1 = pair[0]#(pair[0][0] + round((pair[0][0] - pair[1][0])), pair[0][1] + round((pair[0][1] - pair[1][1])))
        P2 = pair[1]#(pair[1][0] + round((pair[1][0] - pair[0][0])), pair[1][1] + round((pair[1][1] - pair[0][1])))

    
        x1 = P1[0]
        x2 = P2[0]
        y1 = P1[1]
        y2 = P2[1]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = -1 if x1 < x2 else 1  # Step for x direction
        sy = -1 if y1 < y2 else 1  # Step for y direction
        err = dx - dy
 
        while (x1 >= 0 and x1 < len(map) and  y1 >= 0 and y1 < len(map[x1])):
            if map[x1][y1] != '#' and is_point_inline_area(P1[0], P1[1], P2[0], P2[1], x1, y1):
                map[x1][y1] = '#'
                total +=1
                
            e2 = 2 * err
            if e2 > -dy:  # Adjust error and move in x direction
                err -= dy
                x1 += sx
            if e2 < dx:  # Adjust error and move in y direction
                err += dx
                y1 += sy

        
        x1 = P2[0]
        x2 = P1[0]
        y1 = P2[1]
        y2 = P1[1]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = -1 if x1 < x2 else 1  # Step for x direction
        sy = -1 if y1 < y2 else 1  # Step for y direction
        err = dx - dy
 
        while (x1 >= 0 and x1 < len(map) and  y1 >= 0 and y1 < len(map[x1])):
            if map[x1][y1] != '#' and is_point_inline_area(P1[0], P1[1], P2[0], P2[1], x1, y1):
                map[x1][y1] = '#'
                total +=1
                
            e2 = 2 * err
            if e2 > -dy:  # Adjust error and move in x direction
                err -= dy
                x1 += sx
            if e2 < dx:  # Adjust error and move in y direction
                err += dx
                y1 += sy
                
    return total
                
filename = "Day8/input.txt"
total = 0
map = []
with open(filename, 'r') as file:
    for line in file:
        map.append(list(line.rstrip("\n")))


print(place_antinodes(remove_dedundant_pairs(find_all_antenna_pairs(map)), map))

for m in map:
    print("".join(m))
    



# Example usage
A = (4, 4)
B = (3, 7)
P1 = (2, 10)  # Collinear point
P2 = (2, 2)  # Collinear point
P3 = (4, 5)  # Not collinear

#print(is_point_inline_area(A[0], A[1], B[0], B[1], P1[0], P1[1]))  # True

