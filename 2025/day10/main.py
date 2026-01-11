import math

def read_file(filename):
    machines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            goal_state = None
            goal_jolts = None
            buttons = []
            for segment in line.strip().split(" "):

                if segment[0] == '[':
                    goal_state = list(map(lambda x: False if x =='.' else True, list(segment)[1:-1]))
                if segment[0] == '(':
                    buttons.append(list(map(lambda x: int(x), segment[1:-1].split(','))))
                if segment[0] == '{':
                    goal_jolts = list(map(lambda x: int(x), segment[1:-1].split(',')))
                
            
            machines.append([goal_state, buttons, goal_jolts])
    
    return machines

def all_combinations(lst, n):
    result = []

    def backtrack(start, path):
        if len(path) == n:
            result.append(path.copy())
            return
        for i in range(start, len(lst)):
            path.append(lst[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

def get_min_presses_for_goal_state(goal_state, buttons):
    for n in range(1, len(buttons)+1):
        combs = all_combinations(buttons, n)
        for comb in combs:
            curr_state = [False] * len(goal_state)
            for btn in comb:
                for idx in btn:
                    curr_state[idx] = not curr_state[idx]
            if curr_state == goal_state:
                return n 
    return -1

def solve_p1(machines):
    presses = 0
    for goal_state, buttons, _ in machines:
        presses += get_min_presses_for_goal_state(goal_state,buttons)
    return presses


print(solve_p1(read_file("input.txt")))
