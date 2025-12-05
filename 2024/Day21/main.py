import os
import time
from PIL import Image
import numpy as np
keypad = [['7','8','9'],
          ['4','5','6'],
          ['1','2','3'],
          ['X','0','A']]

dpad = [['X','^','A'],
        ['<','v','>']]

def find_key_pos(key,keypad):
    for x in range(len(keypad)):
        for y in range(len(keypad[x])):
            if keypad[x][y] == key:
                return [x,y]

def find_sequence(code,keypad, startpos):
    sequence = ''
    x = len(keypad)-1
    y = len(keypad[x])-1
    curpos = startpos
    
    for key in code:
        tgt_pos = find_key_pos(key,keypad)
        dist = [tgt_pos[0]-curpos[0], tgt_pos[1]-curpos[1]]
        
        while tgt_pos != curpos : 
            
            if dist[1] > 0:
                curpos[1] += dist[1]
                if  keypad[curpos[0]][curpos[1]] == 'X':
                    curpos[1] -= dist[1]
                else:
                    sequence += '>' * abs(dist[1])
                    dist[1] = 0
                    continue
            elif dist[1] < 0:
                curpos[1] += dist[1]
                if keypad[curpos[0]][curpos[1]] == 'X':
                    curpos[1] -= dist[1]
                else:
                    sequence += '<' * abs(dist[1])
                    dist[1] = 0
                    continue
                
            if dist[0] > 0:
                curpos[0] += dist[0]
                sequence += 'v' * abs(dist[0])
                dist[0] = 0
            elif dist[0] < 0:
                curpos[0] += dist[0]
                sequence += '^' * abs(dist[0])
                dist[0] = 0

                
        sequence += 'A'        
        curpos = tgt_pos
    return sequence


keycodes = []
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        keycodes.append(line.strip('\n'))
        

total = 0
start = time.time()
for keycode in keycodes:
    code = find_sequence(keycode,keypad, [3,2])
    for i in range(2):
        code = find_sequence(code,dpad,[0,2])

    s = "".join([char for char in keycode if char.isdigit()])
    print(s, len(code))
    print(code)
    total += int(s) * len(code)
    
print(total)
end = time.time()
print(end - start)

#156576 - 158428 too high