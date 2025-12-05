rules = dict()

def parse_rules(x,y,rules):
    if x not in rules:
        rules[x] = [y]
    else:
        rules[x].append(y)


def is_manual_correct(manual, rules):
    for i in reversed(range(len(manual))):
        if manual[i] in rules:
            for j in reversed(range(0,i)):
                if manual[j] in rules[manual[i]]:
                    return False
    
    return True

def fix_manual(manual, rules):
    for i in reversed(range(len(manual))):
        if manual[i] in rules:
            for j in reversed(range(0,i)):
                if manual[j] in rules[manual[i]]:
                    manual[j], manual[i] = manual[i],manual[j]
                    
    return manual
    


filename = "Day5/input.txt"
total = 0
with open(filename, 'r') as file:
    for line in file:
        if "|" in line:
            x = line.split("|")[0].strip()
            y = line.split("|")[1].strip()
            parse_rules(x,y,rules)
        
        if "," in line:
            manual = line.replace("\n", "").split(',')
            if not is_manual_correct(manual,rules):
                manual = fix_manual(manual, rules)
                total += int(manual[int((len(manual)-1)/2)])

print(total)
