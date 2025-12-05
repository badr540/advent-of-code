import os
import time
from PIL import Image
import numpy as np

def find_worker(warehouse):
    for x in range(len(warehouse)):
        for y in range(len(warehouse[x])):
            if warehouse[x][y] == '@':
                return [x,y]

    return[-1,-1]

def simulate_movement(warehouse,w_pos,moves):
    for m in moves:

        x,y = w_pos
        x += m[0]
        y += m[1]
        if x >= 0 or x < len(warehouse) and y >= 0 or y < len(warehouse[x]):
            if warehouse[x][y] == '#':
                continue
            elif warehouse[x][y] == 'O':
                boxes = []
                xs,ys = x,y
                while(warehouse[xs][ys] == 'O'):
                    boxes.append([xs,ys])
                    xs += m[0]
                    ys += m[1]
                if warehouse[xs][ys] != '#':
                    for b in boxes:
                        xs,ys = b
                        xs += m[0]
                        ys += m[1]
                        warehouse[xs][ys] = 'O'
                    warehouse[w_pos[0]][w_pos[1]] = '.'
                    w_pos = [x,y]
                    warehouse[w_pos[0]][w_pos[1]] = '@'
                    
            else:
                warehouse[w_pos[0]][w_pos[1]] = '.'
                w_pos = [x,y]
                warehouse[w_pos[0]][w_pos[1]] = '@'
    return warehouse


def move_boxes(w,x,y, m):
    boxes = []
    boxchars = []
    xs,ys = x,y
        
    next_row = []
    next_row.append([xs,ys])
    if w[xs][ys] == ']':
        boxes.append([xs,ys])
        boxchars.append(w[xs][ys])
        next_row.append([xs,ys])
        boxes.append([xs,ys-1])
        boxchars.append(w[xs][ys-1])
        next_row.append([xs,ys-1])
    elif w[xs][ys] == '[':
        boxes.append([xs,ys])
        boxchars.append(w[xs][ys])
        next_row.append([xs,ys])
        boxes.append([xs,ys+1])
        boxchars.append(w[xs][ys+1])
        next_row.append([xs,ys+1])
        
    while(len(next_row)!= 0):
        row = next_row.copy()
        next_row = []
        for b in row:
            xs,ys = b
            xs += m[0]
            ys += m[1]
            if w[xs][ys] == ']':
                boxes.append([xs,ys])
                boxchars.append(w[xs][ys])
                next_row.append([xs,ys])
                boxes.append([xs,ys-1])
                boxchars.append(w[xs][ys-1])
                next_row.append([xs,ys-1])
            elif w[xs][ys] == '[':
                boxes.append([xs,ys])
                boxchars.append(w[xs][ys])
                next_row.append([xs,ys])
                boxes.append([xs,ys+1])
                boxchars.append(w[xs][ys+1])
                next_row.append([xs,ys+1])
            elif w[xs][ys] == '#':
                return False
    for b in boxes:
        xs,ys = b
        w[xs][ys] = '.'
    for b,c in zip(boxes,boxchars):
        xs,ys = b
        xs += m[0]
        ys += m[1]
        w[xs][ys] = c

    return True

def simulate_movement_p2(warehouse,w_pos,moves):
    for m in moves:
        for l in warehouse:
            print("".join(l))
        x,y = w_pos
        x += m[0]
        y += m[1]
        if x >= 0 or x < len(warehouse) and y >= 0 or y < len(warehouse[x]):
            if warehouse[x][y] == '#':
                continue
            elif warehouse[x][y] == '[' or warehouse[x][y] == ']':
                if m == [-1,0] or m == [1,0]:
                    if move_boxes(warehouse,x,y,m):
                            warehouse[w_pos[0]][w_pos[1]] = '.'
                            w_pos = [x,y]
                            warehouse[w_pos[0]][w_pos[1]] = '@'
                else:
                    boxes = []
                    boxchars = []
                    xs,ys = x,y
                    while(warehouse[xs][ys] == '[' or warehouse[xs][ys] == ']'):
                        boxes.append([xs,ys])
                        boxchars.append(warehouse[xs][ys])
                        xs += m[0]
                        ys += m[1]
                    if warehouse[xs][ys] != '#':
                        for b,c in zip(boxes,boxchars):
                            xs,ys = b
                            xs += m[0]
                            ys += m[1]
                            warehouse[xs][ys] = c
                        warehouse[w_pos[0]][w_pos[1]] = '.'
                        w_pos = [x,y]
                        warehouse[w_pos[0]][w_pos[1]] = '@'

            else:
                warehouse[w_pos[0]][w_pos[1]] = '.'
                w_pos = [x,y]
                warehouse[w_pos[0]][w_pos[1]] = '@'
    return warehouse

def calculate_GPS_total(warehouse):
    total = 0
    for x in range(len(warehouse)):
        for y in range(len(warehouse[x])):
            if warehouse[x][y] == 'O':
                total += x *100 + y
                
    return total


def calculate_GPS_total_p2(warehouse):
    total = 0
    for x in range(len(warehouse)):
        for y in range(len(warehouse[x])):
            if warehouse[x][y] == '[':
                total += x *100 + y
                
    return total

warehouse = []
moves = []

def arrows_to_vecs(a):
    move_arrows = ['^','>','v','<']
    move_vecs = [[-1,0],[0,1],[1,0],[0,-1]]
    return move_vecs[move_arrows.index(a)]
def widen_warehouse_map(warehouse):
    wider_warehouse = []
    for x in range(len(warehouse)):
        wider_warehouse.append([])
        for y in range(len(warehouse[x])):
            if warehouse[x][y] == '#':
                wider_warehouse[x].append('#') 
                wider_warehouse[x].append('#')
            if warehouse[x][y] == 'O':
                wider_warehouse[x].append('[') 
                wider_warehouse[x].append(']')
            if warehouse[x][y] == '.':
                wider_warehouse[x].append('.') 
                wider_warehouse[x].append('.')
            if warehouse[x][y] == '@':
                wider_warehouse[x].append('@') 
                wider_warehouse[x].append('.')
                
    return wider_warehouse
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        if '#' in line:
            warehouse.append(list(line.rstrip('\n')))
        elif line != "\n":
            m = list(line.rstrip('\n'))
            moves += list(map(arrows_to_vecs, m))
        



    
start = time.time()
w_warehouse = widen_warehouse_map(warehouse)

w_pos = find_worker(w_warehouse)
w_warehouse = simulate_movement_p2(w_warehouse,w_pos,moves)
for l in w_warehouse:
    print("".join(l))
print(calculate_GPS_total_p2(w_warehouse))


end = time.time()
print(end - start)
