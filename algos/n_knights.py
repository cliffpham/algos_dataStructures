#create board

#create a list of potential spots

#if place piece is true, run solve, 

#mark function

def n_knights(n):
    b = create_board(n)
    result = solve(b, n*2, [])

    return result

def solve(b, remaining_knights, positions):
    if remaining_knights == 0:
        print(positions)
        return True
    
    open_spaces = search(b)

    for candidate in open_spaces:
        if piece_placed(b, candidate, positions):
            if solve(b, remaining_knights-1, positions):
                return True
            unplace_piece(b, candidate, positions)

def create_board(n):
    b = []
    for i in range(n):
        b.append([0 for j in range(n)])
    return b

def search(b):
    q = []
    for row in range(len(b)):
        for spot in range(len(b)): 
            # if b[row][spot] == 0:
                q.append((row,spot))
    return q

def piece_placed(b, candidate, positions):
    x = candidate[0]
    y = candidate[1]

    if b[x][y] != 0:
        return False

    mark_sight(b,x,y,val = 1)
    positions.append(candidate)
    return True

def mark_sight(b, x, y, val):
    b[x][y] += val

    x1, x2, x3, x4 = x+1, x-1, x+2, x-2
    y1, y2, y3, y4 = y+1, y-1, y+2, y-2

    if x1 < len(b) and y3 < len(b):
        b[x1][y3] += val
    
    if x1 < len(b) and y4 >= 0:
        b[x1][y4] += val
    
    if x2 >= 0 and y1 < len(b):
        b[x2][y1] += val

    if x2 >= 0 and y4 >= 0:
        b[x2][y4] += val
    
    if x3 < len(b) and y2 >= 0:
        b[x3][y2] += val
    
    if x3 < len(b) and y1 < len(b):
        b[x3][y1] += val

    if x4 >= 0 and y2 >= 0:
        b[x4][y2] += val
    
    if x4 >= 0 and y1 < len(b):
        b[x4][y1] += val

    return 

def unplace_piece(b, candidate, positions):
    x = candidate[0]
    y = candidate[1]

    mark_sight(b,x,y,val = -1)
    positions.pop()
    return 

print(n_knights(5))