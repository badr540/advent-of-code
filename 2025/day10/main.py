import math

def read_file(filename):
    machines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            state = None
            buttons = []
            for segment in line.split(" "):

                if segment[0] == '[':
                    state = list(map(lambda x: False if x =='.' else True, list(segment)[1:-1]))
                if segment[0] == '(':
                    buttons.append(list(map(lambda x: int(x), segment[1:-1].split(','))))
            
            print(state, buttons)

        
print((read_file("input.txt")))
