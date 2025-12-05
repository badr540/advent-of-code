import os
import time

def find_cheapest_button_presses(A,B,tgt_pos):
    B_presses = total = min(round(tgt_pos[0]/B[0]), round(tgt_pos[1]/B[1]))
    A_presses = 0
    curr_pos = [B[0] * B_presses + A[0] * A_presses, B[1] *B_presses + A[1] * A_presses]
    while(curr_pos != tgt_pos and B_presses > 0):
        if curr_pos[0] > tgt_pos[0] or curr_pos[1] > tgt_pos[1]:
            B_presses -= 1
        elif  curr_pos[0] < tgt_pos[0] or curr_pos[1] < tgt_pos[1]:
            A_presses += 1
        total = A_presses*3 + B_presses
        curr_pos = [B[0] * B_presses + A[0] * A_presses, B[1] *B_presses + A[1] * A_presses]

    if B_presses <= 0:
        return 0
    
    return total

def find_cheapest_button_presses_p2(A,B,tgt_pos):
    #part 2
    for i in range(len(tgt_pos)):
        tgt_pos[i] += 10000000000000
    
    A_presses = (tgt_pos[0] * B[1] - tgt_pos[1] * B[0]) / (A[0] * B[1] - A[1] * B[0])
    B_presses = (tgt_pos[0] - A[0] * A_presses)/ B[0]
    if A_presses%1 != 0 or B_presses%1 != 0:
        return 0
    return (B_presses + A_presses*3)

button_A = []
button_B = []
prize_pos = []
filename = "{}/input.txt".format(os.path.abspath(__file__)[0:-8])
total = 0
start = time.time()
with open(filename, 'r') as file:
    for line in file:
        if "Button A:" in line:
            button_A = line.split(':')[1].split(',')
            for i in range(len(button_A)):
                button_A[i].strip(' ').strip('\n')
                button_A[i] = list(button_A[i])
                for j in reversed(range(len(button_A[i]))):
                    if not button_A[i][j].isdigit():
                        button_A[i].pop(j)
                button_A[i] = int("".join(button_A[i]))
        if "Button B:" in line:
            button_B = line.split(':')[1].split(',')
            for i in range(len(button_B)):
                button_B[i].strip(' ').strip('\n')
                button_B[i] = list(button_B[i])
                for j in reversed(range(len(button_B[i]))):
                    if not button_B[i][j].isdigit():
                        button_B[i].pop(j)
                button_B[i] = int("".join(button_B[i]))
        if "Prize:" in line:
            prize_pos = line.split(':')[1].split(',')
            for i in range(len(prize_pos)):
                prize_pos[i].strip(' ').strip('\n')
                prize_pos[i] = list(prize_pos[i])
                for j in reversed(range(len(prize_pos[i]))):
                    if not prize_pos[i][j].isdigit():
                        prize_pos[i].pop(j)
                prize_pos[i] = int("".join(prize_pos[i]))
            
            total += find_cheapest_button_presses_p2(button_A,button_B,prize_pos)


print(total)
#print(calculate_fencing_prices(map))
end = time.time()
print(end - start)
