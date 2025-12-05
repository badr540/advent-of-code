import itertools

def is_equation_true(nums,result):
    for combo in itertools.product(range(3), repeat=len(nums)-1):
        nums2 = nums.copy()
        total = int(nums2.pop(0))
        for i in combo:
            if i == 0:
                total += int(nums2.pop(0))
            elif i == 1:
                total *= int(nums2.pop(0))
            else:
                total = int(str(total) + nums2.pop(0))
        if total == result:
            return True
        
    return False

filename = "Day7/input.txt"
total = 0
with open(filename, 'r') as file:
    for line in file:
        res = int(line.split(':')[0])
        nums = line.split(':')[1].strip().rstrip("\n").split(' ')
        
        if is_equation_true(nums,res):
            total += res


print(total)