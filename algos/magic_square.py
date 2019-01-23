def magic_square(b):

    nb = [row[:] for row in b]
    
    immutables = scan_diagonals(b)
    scan_rows(b, immutables)
    scan_cols(b, immutables)
    spots = find_mutable_spots(b, immutables)

    result = solve(b, spots, nb, immutables, 0)
    c = compare_boards(b, result, spots)
    
    return c

def solve(b, spots, nb, immutables, i):
    if i == len(spots):
        # print(nb)
        return nb

    spot = spots[i]

    if place_num(nb, spot):
        if solve(b, spots, nb, immutables, i+1):
            return nb
        undo_move(nb, spot)


def find_mutable_spots(b, immutables):
    q = []
    
    for row in range(len(b)):
        for col in range(len(b)):
            if (row, col) in immutables: continue
            q.append((row,col))
    
    return q

def place_num(nb, spot):
    x = spot[0]
    y = spot[1]

    if check_row(nb, x, y, nb[x][y]) or check_col(nb, x, y, nb[x][y]):
        return True

    options = [1,2,3,4,5,6,7,8,9]

    for option in options:
        if check_row(nb, x, y, option) or check_col(nb,x, y, option):
            nb[x][y] = option
            return True

    return False

def undo_move(nb, spot):
    x = spot[0]
    y = spot[1]

    nb[x][y] = 0

def check_row(nb, x, y, option):
    temp = nb[x][y]
    val = 0
    nb[x][y] = option

    for i in range(len(nb)):
        val = val + nb[x][i]
    
    if val == 15:
        nb[x][y] = temp
        return True
   
    nb[x][y] = temp
    return False

def check_col(nb, x, y, option):
    temp = nb[x][y]
    val = 0
    nb[x][y] = option

    for i in range(len(nb)):
        val = val + nb[i][y]
    
    if val == 15:
        nb[x][y] = temp
        return True
   
    nb[x][y] = temp
    return False
    

def scan_diagonals(b):
    immutables = set()
    if b[0][0] + b[1][1] + b[2][2] == 15:
        for i in range(len(b)):
            immutables.add((i,i))

    if b[0][2] + b[1][1] + b[2][0] == 15:
        r = len(b) - 1
        for i in range(len(b)):
            immutables.add((i, r-i))
    
    return immutables

def scan_rows(b, immutables):
    if b[0][0] + b[0][1] + b[0][2] == 15:
        for i in range(len(b)):
            if (0, i) in immutables: continue
            immutables.add((0,i))
    
    if b[1][0] + b[1][1] + b[1][2] == 15:
        for i in range(len(b)):
            if (1, i) in immutables: continue
            immutables.add((1,i))   
    
    if b[2][0] + b[2][1] + b[2][2] == 15:
        for i in range(len(b)):
            if (2, i) in immutables: continue
            immutables.add((2,i)) 
    return

def scan_cols(b, immutables):
    if b[0][0] + b[1][0] + b[2][0] == 15:
        for i in range(len(b)):
            if (i, 0) in immutables: continue
            immutables.add((i,0))
    
    if b[0][1] + b[1][1] + b[2][1] == 15:
        for i in range(len(b)):
            if (i, 1) in immutables: continue
            immutables.add((i,1))   
    
    if b[0][2] + b[1][2] + b[2][2] == 15:
        for i in range(len(b)):
            if (i, 2) in immutables: continue
            immutables.add((i,2)) 
    return

def compare_boards(b, nb, spots):
    c = []
    for x,y in spots:
         c.append(abs(b[x][y] - nb[x][y]))
    return sum(c)
        

b = [
    [4,9,2],
    [3,5,7],
    [8,1,5]
]

b1 = [
    [5,3,4],
    [1,5,8],
    [6,4,2]
]

b2 = [
    [4,8,2],
    [4,5,7],
    [6,1,6]
]

print(magic_square(b))
print(magic_square(b1))
print(magic_square(b2))

