def read_file(filename):
    board = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            board.append(list(line.strip()))
    return board

def count_adjacent_rolls(board, x, y):
    
    max_x = len(board[0]) - 1
    max_y = len(board) - 1
    x_start = max(0, x-1)
    y_start = max(0, y-1)
    x_end = min(max_x, x+1) + 1
    y_end = min(max_y, y+1) + 1

    count = 0
    for i in range(y_start,y_end):
        for j in range(x_start,x_end):
            if x == j and y == i: continue
            if board[i][j] == '@':
                count+= 1
    
    return count


def count_accessable_rolls(board):
    count = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == '@' and count_adjacent_rolls(board, x, y) < 4:
                count+= 1
    
    return count


def count_all_removable_rolls(board):
    count = 0
    while True:
        rolls_to_remove = []
        current_count = 0
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == '@' and count_adjacent_rolls(board, x, y) < 4:
                    rolls_to_remove.append([x,y])
                    current_count+= 1
        count += current_count
        if current_count == 0:
            break
        for [x, y] in rolls_to_remove:
            board[y][x] = 'X'
    
    return count


print("part 1:",count_accessable_rolls(read_file("input.txt")))

print("part 2:",count_all_removable_rolls(read_file("input.txt")))

