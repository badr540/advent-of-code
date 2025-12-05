import os
import time
from PIL import Image
import numpy as np

def find_expected_output(wires):
    xbits = []
    ybits = []
    for key in wires:
        if 'x' in key:
            xbits.append(wires[key])
        if 'y' in key:
            ybits.append(wires[key])
    xval = bits_to_decimal(xbits)
    yval = bits_to_decimal(ybits)
    return xval + yval


def evaluate_wire_connections(wires,connections):
    evaluated_cons = 0
    idx = 0
    while(evaluated_cons != len(connections)):    
        w1, gate, w2, _, output_wire = connections[idx].split(' ')
        if w1 in wires.keys() and w2 in wires.keys() and output_wire not in wires.keys():
            if gate == 'OR':
                wires[output_wire] = wires[w1] | wires[w2]
            elif gate == 'AND':
                wires[output_wire] = wires[w1] & wires[w2]
            elif gate == "XOR":
                wires[output_wire] = wires[w1] ^ wires[w2]
            
            evaluated_cons += 1 
            
            
        idx += 1
        idx = idx%len(connections)
        
    return wires
    

def wire_outputs_to_decimal(output_wires, connections):
    sorted_keys = []
    for con in connections:
        if 'z' in con.split(' ')[-1]: 
            sorted_keys.append(con.split(' ')[-1])
    
    sorted_keys.sort()
    bits = []
    for key in sorted_keys:
        bits.append(output_wires[key])

    
    return bits_to_decimal(bits)

def bits_to_decimal(bits):
    number = 0
    for bit in reversed(bits):
        number = (number << 1) | bit
    
    return number


def swap_gate_outputs(wires, connections, swaps, expected_output):
    output = None
    swapped_gates = []
    while (output != expected_output):
        con_copy = [i for i in connections]
        
        output = wire_outputs_to_decimal(evaluate_wire_connections(wires,con_copy) , con_copy)
        
        
wires = {}
connections = []

filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        if ':' in line:
            wirename, wireval = line.split(':')
            wireval = int(wireval.strip(' ').strip('\n'))
            wires[wirename] = wireval
        elif line != '\n':
            connections.append(line.strip('\n'))

total = 0
start = time.time()

expected_output = find_expected_output(wires)
print(expected_output)
swap_gate_outputs(wires,connections,2,expected_output)
print()

end = time.time()
