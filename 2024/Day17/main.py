import os
import time
from PIL import Image
import numpy as np

program_counter = 0

registers = [0,0,0]
output = ""
#uses combo operands
def adv(operand):
    global program_counter, registers,output
    combo = operand if operand <= 3 else registers[(operand-4)]
    registers[0] =  int(registers[0]/pow(2,combo))

#uses literal operands
def bxl(operand):
    global program_counter, registers,output
    registers[1] = registers[1] ^ operand
#combo
def bst(operand):
    global program_counter, registers,output
    combo = operand if operand <= 3 else registers[(operand-4)]
    registers[1] = combo%8

#literal
def jnz(operand):
    global program_counter, registers,output
    if registers[0] != 0:
        program_counter = operand

def bxc(operand):
    global program_counter, registers,output
    registers[1] = registers[1] ^ registers[2]

def out(operand):
    global program_counter, registers,output
    combo = operand if operand <= 3 else registers[(operand-4)]
    output += str(combo%8)+','

def bdv(operand):
    global program_counter, registers,output
    combo = operand if operand <= 3 else registers[(operand-4)]
    registers[1] =  int(registers[0]/pow(2,combo))

def cdv(operand):
    global program_counter, registers,output
    combo = operand if operand <= 3 else registers[(operand-4)]
    registers[2] =  int(registers[0]/pow(2,combo)) 


def run_program(program):
    global program_counter, registers,output
    while(program_counter < len(program)):
        opcode = int(program[program_counter])
        operand = int(program[program_counter+1])
        program_counter+=2
        
        match opcode:
            case 0:
                adv(operand)
            case 1:
                bxl(operand)
            case 2:
                bst(operand)
            case 3:
                jnz(operand)
            case 4: 
                bxc(operand)
            case 5:
                out(operand)
            case 6:
                bdv(operand)
            case 7:
                cdv(operand)
               
                
program = []
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        if "Register A" in line:
            registers[0] = int(line.split(':')[1].strip(' ').strip('\n'))
        if "Register B" in line:
            registers[1] = int(line.split(':')[1].strip(' ').strip('\n'))
        if "Register C" in line:
            registers[2] = int(line.split(':')[1].strip(' ').strip('\n'))

        if "Program" in line:
            program = line.split(':')[1].strip(' ').split(',')
            programstr = line.split(':')[1].strip(' ')


start = time.time()

run_program(program)
print(registers)
print(output[0:-1])
print("")
print("output len:" + str(len(output[0:-1])))
print("program len:" + str(len(programstr)))
end = time.time()
print(end - start)



#0,3, A = A/2^3
#5,4, print A%8
#3,0 jump to 0