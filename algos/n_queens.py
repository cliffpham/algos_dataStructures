def n_queens(n):
    """
    >>> n_queens(8)
    True

    >>> n_queens(2)
    False
    """
    if n < 4:
        return False

    board = []

    for i in range(n):
        board.append([0 for j in range(n)])

    open_spaces = search(board)

    solved = solve(n, board, open_spaces, 0, [])

    return solved

def solve(n, b, open_spaces, level, positions): #board, 0, []
    if level == n:
        print(positions)
        print_board(n, positions)
        return positions

    for open_space in open_spaces:
        if valid_spot(b, open_space, positions):
            if solve(n, b, open_spaces, level+1, positions):
                return True
            undo_move(b, open_space, positions)
            
def search(b):
    queue = []
    for row in range(len(b)):
        for spot in range(len(b)):
            queue.append((row, spot))
    return queue

def valid_spot(b, p, positions):
    x = p[0]
    y = p[1]

    if b[x][y] != 0:
        return False
    
    mark_row(b, x, 1)
    mark_column(b, y, 1)
    mark_diagonals(b,x,y, 1)
    positions.append((x,y))

    return True

#print out board
def print_board(n, positions):
    board = []
    for i in range(n):
        board.append(['•' for j in range(n)])

    for x, y in positions:
        board[x][y] = 'Q'

    for row in board:
        for spot in row:
            print(spot, end = " ")
        print()

#mark rows
def mark_row(b, x, val):
    for i in range(len(b)):
        b[x][i] += val
    return b

#mark columns
def mark_column(b,y, val):
    for i in range(len(b)):
        b[i][y] += val
    return b

#mark diagonals
def mark_diagonals(b,x,y, val):
    nw_x, nw_y = x, y
    ne_x, ne_y = x, y
    sw_x, sw_y = x, y
    se_x, se_y = x, y
   
    for i in range(len(b)):
        nw_x -= 1
        nw_y -= 1
        
        ne_x -= 1
        ne_y += 1

        sw_x += 1
        sw_y -= 1

        se_x += 1
        se_y += 1

        if nw_x >= 0 and nw_y >= 0:
            b[nw_x][nw_y] += val
     
        if ne_x >= 0 and ne_y < len(b):
            b[ne_x][ne_y] += val

        if se_x < len(b) and se_y < len(b):
            b[se_x][se_y] += val

        if sw_x < len(b) and sw_y >= 0:
            b[sw_x][sw_y] += val

def undo_move(b, p, positions):
    if p == 0:
        return b
    
    x = p[0]
    y = p[1]

    mark_row(b, x, -1 )
    mark_column(b, y, -1)
    mark_diagonals(b, x, y, -1)

    positions.pop()

    return

print(n_queens(4))
print(n_queens(6))
print(n_queens(8))
