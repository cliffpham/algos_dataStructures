  # for each potential item to be placed check the row, col, sub-box, to ensure that the value does not exist, else try the next item
import math

def sudoku(b):
    to_fill = search(b)
    result = solve(b, to_fill, 0)
    
    return result

def solve(b, to_fill, i):
    if i == len(to_fill):
        return b
    
    cur_space = to_fill[i]
    options = get_options(b, cur_space)
   
    for option in options:
        if can_place(b, cur_space, option):
            place(b, cur_space, option)
            if solve(b,to_fill,i+1):
                return b
            else:
                undo(b, cur_space)
    return False

def search(b):
    q = []
    for row in range(len(b)):
        for space in range(len(b)):
            if b[row][space] == 0:
                q.append((row,space))
    return q

def get_options(b,space):
    x = space[0]
    y = space[1]

    numbers = [1,2,3,4,5,6,7,8,9]
    options = []

    for num in numbers:
        if check_row(b,x,num) and check_col(b,y,num) and check_sub(b, x, y, num):
            options.append(num)

    return options

#check if current num can be placed in spot, if not return false

def can_place(b, space, option):
    x = space[0]
    y = space[1]

    if check_row(b,x,option) and check_col(b,y,option) and check_sub(b, x, y, option):
        return True

    return False

def place(b, space, option):
    x = space[0]
    y = space[1]

    b[x][y] = option

def undo(b,space):
    x = space[0]
    y = space[1]
    
    b[x][y] = 0

def check_row(b,x,n):
    for i in range(len(b)):
        if b[x][i] == n:
            return False
    return True

def check_col(b,y,n):
    for i in range(len(b)):
        if b[i][y] == n:
            return False
    return True

def check_sub(b,x,y,n):
    region_size = math.trunc(math.sqrt(len(b)))

    i = math.trunc(x/3)
    j = math.trunc(y/3)
 
    top_left_sub_row = region_size * i
    top_left_sub_col = region_size * j
 
    for k in range(3):
        for l in range(3):
            if b[top_left_sub_row + k][top_left_sub_col + l] == n:
                return False
    return True

board = [
    [2,0,0,0,1,7,6,0,0],
    [4,6,7,5,0,0,0,8,0],
    [1,5,0,2,0,0,0,0,0],
    [0,9,2,3,0,0,7,0,0],
    [3,0,0,0,0,0,0,0,8],
    [0,0,5,0,0,1,4,6,0],
    [0,0,0,0,0,6,0,3,2],
    [0,2,0,0,0,3,5,9,6],
    [0,0,6,1,5,0,0,0,7]
]

print(sudoku(board))