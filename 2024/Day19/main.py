import os
import time
from PIL import Image
import numpy as np
cache = {}
def is_design_possible(design,colors):
    if design in cache:
        return cache[design]
    if design == "":
        return 1
    total  = 0
    for i in range(0,len(design)+1):
        if design[:i] in colors:
            total += is_design_possible(design[i:],colors) 
    cache[design] = total
    return total


colors = []
designs = []
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        if ',' in line:
            colors += line.strip('\n').split(',')
            
        elif line != '\n':
            designs.append(line.strip('\n'))
            
colors = list(map(lambda x : x.strip(' '),colors))

total = 0
start = time.time()
for d in designs:
    total += is_design_possible(d,colors)
print(total)
end = time.time()
print(end - start)