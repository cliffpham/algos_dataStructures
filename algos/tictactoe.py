#create board of n x n

#fill board with random 'X' 'O'

#take the diagonal (start at [0,0]) of the board and run a check on each square vertically and horizontally to determine if there is a winner 
#if at center of the board also run an inverse diagonal check

#if false move on the next point
    #if all false return no winner

#Either O(1) / O(n) because I'm only looping through numbers (0 to n) and checking each individual square and not the entire board?

def solve(b):
    if check_diagonal_left(b) or check_diagonal_right(b):
        return True

    for i in range(len(b)):
        if check_vertical(b, i) or check_horizontal(b, i):
            return True
    
    return False

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
        
    
board = [[1,2,2],
         [1,2,1],
         [2,1,2]]

board2 = [[2,2,2,2],
          [1,2,1,2],
          [2,1,2,1],
          [1,2,1,2]]

board3 = [[2,2,2,2],
          [1,2,1,2],
          [2,1,2,1],
          [1,1,1,1]]


print(solve(board))
print(solve(board2))
print(solve(board3))