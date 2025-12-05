def organize_memory(memory, free_space):
    for i in range(len(memory) - free_space):
        if memory[i] == '.':
            for j in reversed(range(i, len(memory))):
                if memory[j] != '.':
                    memory[i] = memory[j]
                    memory[j] = '.'
                    break

    return memory

def organize_memory_nofrag(memory, sizes):
    
    i = len(memory) 
    while i > 0:
        i -= 1
        if memory[i] != '.':
            if memory[i] == 8:
                print('')
                
            for j in range(i):
                if memory[j] == '.' and sizes[j] >= sizes[i]:
                    file = memory[i]
                    filesize = sizes[i]
                    memory[i] = '.'
                    memory.insert(j,file)
                    sizes.insert(j,filesize)
                    i+=1
                    sizes[j+1] -= sizes[j]
                    
                    if sizes[j+1] == 0:
                        sizes.pop(j+1)
                        memory.pop(j+1)
                        i -= 1
                    elif memory[j+2] == '.':
                        sizes[j+2] += sizes[j+1]
                        sizes.pop(j+1)
                        memory.pop(j+1)
                        i -= 1
                    break 
                        
    reformatted_memory = []
    for i in range(len(memory)):
        for j in range(sizes[i]):
            reformatted_memory.append(str(memory[i]))
    
    return reformatted_memory
            
    
def calculate_memory_checksum(memory):
    checksum = 0
    
    for i in range(len(memory)):
        if memory[i] != '.':
            checksum += (i * int(memory[i]))
            
    return checksum

memory = []
file_id = 0          
free_space = 0

#part 2 
memory = [] #val = id
sizes = [] #val = size

filename = "Day9/input.txt"
with open(filename, 'r') as file:
    for line in file:
        f = True
        for l in line:

            if f:
                memory.append(file_id)
                sizes.append(int(l))
                file_id += 1
                f = False
            else:
                memory.append('.')
                sizes.append(int(l))
                f = True
                
#part 1
#memory = organize_memory(memory, free_space)
#print(calculate_memory_checksum(memory, free_space))

#part 2
memory = organize_memory_nofrag(memory, sizes)
print("".join(memory))
print(calculate_memory_checksum(memory))