import os
import time
from PIL import Image
import numpy as np

def mix(n1,n2):
    return n1^n2

def prune(n):
    return n % 16777216

def generate_next_secret_numbers(secret_num,n):
    num_sequence = []
    for i in range(n):
        secret_num = mix(secret_num,secret_num*64)
        secret_num = prune(secret_num)
        secret_num = mix(secret_num, int(secret_num/32))
        secret_num = prune(secret_num)
        secret_num = mix(secret_num,secret_num*2048)
        secret_num = prune(secret_num)        
        num_sequence.append(secret_num%10)
    
    return num_sequence

def find_best_sequence(sequences):
    sequence_totals = {
        
    }
    for seq in sequences:
        cur_sequence_totals = {
        
        }
        cur_seq = []
        prev_n = seq.pop(0)
        for n in seq:
            cur_seq.append(n - prev_n) 
               
            if len(cur_seq) == 4:
                tcur_seq = tuple(cur_seq)
                if tcur_seq not in cur_sequence_totals.keys():
                    cur_sequence_totals[tcur_seq] = n
                    
                cur_seq.pop(0)
                
            prev_n = n 
        
        for key in cur_sequence_totals.keys():
            if key not in sequence_totals.keys():
                sequence_totals[key] = cur_sequence_totals[key]
            else:
                sequence_totals[key] += cur_sequence_totals[key]
                
    return sequence_totals
                    

secret_nums = []
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
with open(filename, 'r') as file:
    for line in file:
        secret_nums.append(int(line.strip('\n')))
        

total = 0
num_sequences = []
start = time.time()
for secret_num in secret_nums:
    num_sequences.append(generate_next_secret_numbers(secret_num,2000))

seq_vals = find_best_sequence(num_sequences)

max_value = max(seq_vals.values())
max_key = None
for k in seq_vals.keys():
    if seq_vals[k] == max_value:
        max_key = k
        break
        


print(max_value)
print(max_key)  
end = time.time()
print(end - start)

#1726 too high