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

    return sum(answer)

# part 2
def cephalopodify(worksheet):
    worksheet_c = []

    for col_idx in range(len(worksheet[0])):
        column = [row[col_idx] for row in worksheet]
        column = list(map(lambda x: x.rjust(3,'-'), column)) if col_idx % 2 == 0 else list(map(lambda x: x.ljust(3,'-'), column))

        new_col = []
        for i in range(3):
            num = ''
            for j in range(len(column)-1):
                if column[j][i] != '-':
                    num += column[j][i]
            new_col.append(num)

        new_col.append(column[-1].strip('-'))
        worksheet_c.append(new_col)
    worksheet_c = list(zip(*worksheet_c[::-1]))

    return worksheet_c


print("part 1: ",solve(read_file("input.txt")))

print("part 2: ",solve(cephalopodify(read_file("input.txt"))))
