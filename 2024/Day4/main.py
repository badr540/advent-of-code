DebugList = []
def is_X_MAS(x,y,input_list):
    
    for i in [-1,1]:
        for j in [-1,1]:
            if  not  ( (input_list[x + i][y + j] == 'M' and input_list[x - i][y - j] == 'S') or (input_list[x + i][y + j] == 'S' and input_list[x - i][y - j] == 'M')):
                return False
    return True

for i in range(1,len(input_list)-1):
    for j in range(1,len(input_list[i])-1):
        if input_list[i][j] == "A":
            if is_X_MAS(i,j,input_list):
                total+=1
                
filename = "Day3/input.txt"
input_list = []
with open(filename, 'r') as file:
    for line in file:
        input_list.append(line);

total = 0


print(total)