
import math

def wrap_around(val, mod):
    return ((val % mod) + mod) % mod

#part  1
def calculate_clicks(dial_moves):
    clicks = 0
    dial_pos = 50
    for move in dial_moves:
        d = move[0]
        val = move[1]
        sign = -1 if (d == 'L') else 1
        newVal = dial_pos + val * sign
        dial_pos = wrap_around(newVal, 100)

        if(dial_pos == 0):
            clicks += 1

    return clicks

#part 2
def calculate_clicks2(dial_moves):
    step = 100
    clicks = 0
    dial_pos = 50
    for move in dial_moves:
        d = move[0]
        val = move[1]

        sign = -1 if (d == 'L') else 1
        for i in range(val):
            newVal = dial_pos + 1 * sign
            dial_pos = wrap_around(newVal, 100)
            if dial_pos == 0:
                clicks += 1


        
    return clicks

def read_file(filename):
    moves = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            l = line.strip()
            moves.append([l[0], int(l[1:])])

    return moves

print("part 1:", calculate_clicks(read_file("input.txt")))

print("part 2:", calculate_clicks2(read_file("input.txt")))
