  # for each potential item to be placed check the row, col, sub-box, to ensure that the value does not exist, else try the next item
import math

def solve(b):
    spaces_to_fill = search(b)
    print(spaces_to_fill)

    for space in spaces_to_fill:
        if place_pieced(b, space):
            continue
    return b 

def search(b):
    q = []
    for row in range(len(b)):
        for space in range(len(b)):
            if b[row][space] == 0:
                q.append((row,space))
    return q

def place_pieced(b, candidate):
    x = candidate[0]
    y = candidate[1]
    print(candidate)

    options = [1,2,3,4,5,6,7,8,9]

    for choice in options:
        # print(choice)
        if check_row(b,x,choice) and check_col(b,y,choice) and check_sub(b, x, y, choice):
            print('selected value: ', end='')
            print(choice)
            b[x][y] = choice
            return True

def check_row(b,x,n):
    for i in range(len(b)):
        if b[x][i] == n:
            print(b[x][i])
            return False
    return True

def check_col(b,y,n):
    for i in range(len(b)):
        if b[i][y] == n:
            return False
    return True

def check_sub(b,x,y,n):
    # region_size = round(math.sqrt(len(b)))
    # print(region_size)

    # i = round((x / region_size))
    # j = round((y / region_size))

    # top_left_sub_row = region_size * i
    # top_left_sub_col = region_size * j

    for k in range(len(b)):
        for l in range(len(b)):
            if b[k][l] == n:
                return False
    return True

board = [
 [0,2,0],
 [1,0,9],
 [4,5,0]]

print(solve(board))