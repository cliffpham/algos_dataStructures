  # for each potential item to be placed check the row, col, sub-box, to ensure that the value does not exist, else try the next item
import math

def solve(b):
    spaces_to_fill = search(b)

    for space in spaces_to_fill:
        if place_number(b, space):
            continue
    return b 

def search(b):
    q = []
    for row in range(len(b)):
        for space in range(len(b)):
            if b[row][space] == 0:
                q.append((row,space))
    return q

def place_number(b, candidate):
    x = candidate[0]
    y = candidate[1]

    options = [1,2,3,4,5,6,7,8,9]

    for choice in options:
        if check_row(b,x,choice) and check_col(b,y,choice) and check_sub(b, x, y, choice):
            b[x][y] = choice
            return True
        else:
            print('hit, choice was: ', end='')
            print(choice)
            undo(b,x,y)

def undo(b,x,y):
    b[x][y] == 0
    return

def check_row(b,x,n):
    for i in range(len(b)):
        if b[x][i] == n:
            # print(b[x][i])
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
 [0,2,0],
 [1,0,9],
 [4,5,0]]

board2= [
  [4,0,0,0,0,0,8,0,5],
  [0,3,0,0,0,0,0,0,0],
  [0,0,0,7,0,0,0,0,0],
  [0,2,0,0,0,0,0,6,0],
  [0,0,0,0,8,0,4,0,0],
  [0,0,0,0,1,0,0,0,0],
  [0,0,0,6,0,3,0,7,0],
  [5,0,0,2,0,0,0,0,0],
  [1,0,4,0,0,0,0,0,0]
 ]

board_result = [
    [4, 1, 2, 3, 6, 9, 8, 0, 5], 
    [6, 3, 5, 1, 2, 4, 7, 9, 0], 
    [8, 9, 0, 7, 5, 0, 1, 2, 3], 
    [3, 2, 1, 4, 7, 5, 9, 6, 8], 
    [7, 5, 6, 9, 8, 2, 4, 1, 0], 
    [9, 4, 8, 0, 1, 6, 2, 3, 7], 
    [2, 8, 9, 6, 4, 3, 5, 7, 1], 
    [5, 6, 3, 2, 9, 1, 0, 4, 0], 
    [1, 7, 4, 5, 0, 8, 3, 0, 2]]


# print(solve(board))
print(solve(board2))
