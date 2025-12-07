def read_file(filename):
    worksheet = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            nums = list(filter(lambda s: s!= ' ' and s != '', line.strip().split(' ')))
            worksheet.append(nums)
    return worksheet

# part 1
def solve(worksheet):
    answer = [0 if x == '+' else 1 for x in worksheet[-1]]

    for i in range(len(worksheet)-1):
        for j in range(len(worksheet[i])):
            if not worksheet[i][j].isdigit(): continue

            if worksheet[-1][j] == '*':
                answer[j] *= int(worksheet[i][j])
            else:
                answer[j] += int(worksheet[i][j])
    print(len(answer))
    return sum(answer)

# part 2

def read_file2(filename):
    worksheet = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            worksheet.append(line)

    maxlen = max(len(x) for x in worksheet)
    worksheet = list(map(lambda x: x.ljust(maxlen, ' '), worksheet))
    worksheet_c = []

    sign = ''
    for i in range(len(worksheet[0])):
        num = ''
        for j in range(len(worksheet)):
            if worksheet[j][i] in ['*', '+']:
                if sign != '':
                    worksheet_c[-1].append(sign)
                sign = worksheet[j][i]
                worksheet_c.append([])

            elif worksheet[j][i].isdigit():
                num += worksheet[j][i]
        if num.isdigit():
            worksheet_c[-1].append(num)
    worksheet_c[-1].append(sign)

    return worksheet_c

def solve2(worksheet):
    ans = 0
    for col in worksheet:
        sign = col[-1]
        curr = 0 if sign == '+' else 1
        for n in col:
            if not n.isdigit():continue

            if sign == '+':
                curr += int(n)
            else:
                curr *= int(n)

        ans += curr
    return ans



print("part 1: ",solve(read_file("input.txt")))

print("part 2: ",solve2(read_file2("input.txt")))

#3217461261