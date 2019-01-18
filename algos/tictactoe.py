from random import randint
import math
#create board of n x n

#fill board with random '1' '0'

#take the diagonal (start at [0,0]) of the board and run a check on each square vertically and horizontally to determine if there is a winner 
#if at center of the board also run an inverse diagonal check

#if false move on the next point
    #if all false return false else true

def tictactoe(n):
    b = create_board(n)
    fill_board(b)
    print_board(b)

    return  solve(b)

def solve(b):
    if check_diagonal_left(b) or check_diagonal_right(b):
        return True

    for i in range(len(b)):
        if check_vertical(b, i) or check_horizontal(b, i):
            return True
    
    return False

def create_board(n):
    board = []
    for i in range(n):
        board.append([0 for j in range(n)])

    return board

def fill_board(b):
    limit = math.ceil(len(b) * len(b) / 2)
    counter = 0
    i = 0

    while counter < limit:
        r1 = randint(0, len(b)-1)
        r2 = randint(0, len(b)-1)
        x = r1
        y= r2

        if i % 2 == 0 and b[x][y] == 0:
            b[x][y] = 1
            counter += 1
            i += 2

    return b

def print_board(b):
    for row in b:
        for spot in row:
            print(spot,end = " ")
        print()

def check_vertical(b,y):
    cur = b[y][y]
    count = 0
    
    for i in range(len(b)):
        if cur == b[i][y]:
            count += 1
        else:
            count -= 1
    
    if count == len(b):
        return True
    
    return False

def check_horizontal(b,x):
    cur = b[x][x]
    count = 0
    
    for i in range(len(b)):
        if cur == b[x][i]:
            count += 1
        else:
            count -= 1
    
    if count == len(b):
        return True
    
    return False
        
def check_diagonal_left(b):
    cur = b[0][0]
    count = 0
    
    for i in range(len(b)):
        if cur == b[i][i]:
            count += 1
    
    if count == len(b):
        return True
    
    return False

def check_diagonal_right(b):
    r = (len(b) - 1) #rightmostcorner
    cur = b[0][r] 
    count = 0
    
    for i in range(len(b)):
        if cur == b[i][r-i]:
            count += 1
    
    if count == len(b):
        return True
    
    return False
        
    
# print(tictactoe(3))
# print(tictactoe(5))
