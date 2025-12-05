def parse_input(input):
    isUncurropted = False
    do = True
    total = 0;
    nums = ["", ""]
    current_num = 0
    for i in range(3,len(input)):
        if do:
            if isUncurropted:
                if input[i].isdigit():
                    nums[current_num] += input[i]
                elif nums[0] != "" and input[i] == ",":
                    current_num = 1
                elif nums[1] != "" and input[i] ==")":
                    total+= int(nums[0]) * int(nums[1])
                    isUncurropted = False
                    nums = ["", ""]
                    current_num = 0
                else:
                    isUncurropted = False
                    nums = ["", ""]
                    current_num = 0

            if input[i-3:i+1] == "mul(" and not isUncurropted:
                isUncurropted = True
        
        if input[i:i+7] == "don't()":
            do = False
            current_num = 0
        if input[i:i+4] == "do()":
            do = True

          
    return total

filename = "Day3/input.txt"
with open(filename, 'r') as file:
    inputstr = ""
    for line in file:
        inputstr += line;
    #print(inputstr) 
    print(parse_input(inputstr))
