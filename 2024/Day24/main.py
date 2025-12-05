import os
import time
from PIL import Image
import numpy as np

def reformat_keys_and_locks(keys,locks):
    formatted_keys = []
    formatted_locks = []
    for key in keys:
        formatted_key = []
        for col in range(len(key[0])):
            for row in range(len(key)):
                if key[row][col] == '#':
                    formatted_key.append(6-row)
                    break
        
        formatted_keys.append(formatted_key)

    for lock in locks:
        formatted_lock = []
        for col in range(len(lock[0])):
            for row in reversed(range(len(lock))):
                if lock[row][col] == '#':
                    formatted_lock.append(row)
                    break
        
        formatted_locks.append(formatted_lock)
        
    return formatted_keys,formatted_locks

def number_of_fitting_keys(keys, locks):
    result = 0
    for key in keys:
        for lock in locks:
            result += 1
            for i in range(len(key)):
                if (key[i] + lock[i]) > 5:
                    result -= 1
                    break
    
    return result
keys = []
locks = []

filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    item = []
    for line in file:
        
        if line != '\n':
            item.append(line.strip('\n'))
        else: 
            if item[0][0] == '#':
                locks.append(item)
            else:
                keys.append(item)

            item = []
                
if item != [] and item[0][0] == '#':
    locks.append(item)
elif item != []:
    keys.append(item)
    
start = time.time()

keys,locks = reformat_keys_and_locks(keys,locks)
print(number_of_fitting_keys(keys,locks))
end = time.time()
