def read_file(filename):
    banks = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            banks.append(line.strip())
    return banks

# part 1

def get_max_joltage(banks):
    total = 0
    for bank in banks:
        nums = list(map(lambda x: int(x), bank))
        lhs = max(nums[:-1])
        rhs = max(nums[nums.index(lhs)+1:])
        total += int(str(lhs) + str(rhs))
    return total

# part 2

def get_max_joltage2(banks):
    total = 0
    for bank in banks:
        nums = list(map(lambda x: int(x), bank))
        bank_max = ''
        lastidx = 0
        for i in range(12):
            rrange = i - 11 if i - 11 < 0 else len(nums)
            x = max(nums[lastidx : rrange])
            lastidx = lastidx + nums[lastidx:rrange].index(x) + 1
            bank_max += str(x)
        total += int(bank_max)
    return total

print("part 1:",get_max_joltage(read_file("input.txt")))

print("part 2:",get_max_joltage2(read_file("input.txt")))