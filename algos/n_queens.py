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
        if place_piece(b, open_space, positions):
            if solve(n, b, open_spaces, level+1, positions):
                return True
            unplace_piece(b, open_space, positions)
            
def search(b):
    queue = []
    for row in range(len(b)):
        for spot in range(len(b)):
            queue.append((row, spot))
    return queue

def place_piece(b, p, positions):
    x = p[0]
    y = p[1]

    if b[x][y] != 0:
        return False
    
    mark_row(b, x)
    mark_column(b, y)
    mark_diagonals(b,x,y)
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
def mark_row(b, x):
    for i in range(len(b)):
        b[x][i] += 1
    return b

#mark columns
def mark_column(b,y):
    for i in range(len(b)):
        b[i][y] += 1
    return b

#mark diagonals
def mark_diagonals(b,x,y):
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
            b[nw_x][nw_y] += 1
     
        if ne_x >= 0 and ne_y < len(b):
            b[ne_x][ne_y] += 1

        if se_x < len(b) and se_y < len(b):
            b[se_x][se_y] += 1

        if sw_x < len(b) and sw_y >= 0:
            b[sw_x][sw_y] += 1

def unplace_piece(b, p, positions):
    if p == 0:
        return b
    
    x = p[0]
    y = p[1]

    unmark_row(b, x)
    unmark_column(b, y)
    unmark_diagonals(b, x, y)

    positions.pop()

    return

def unmark_row(b, x):
    for i in range(len(b)):
        b[x][i] -= 1
    return b

def unmark_column(b,y):
    for i in range(len(b)):
        b[i][y] -= 1
    return b

def unmark_diagonals(b,x,y):
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
            b[nw_x][nw_y] -= 1
     
        if ne_x >= 0 and ne_y < len(b):
            b[ne_x][ne_y] -= 1

        if se_x < len(b) and se_y < len(b):
            b[se_x][se_y] -= 1

        if sw_x < len(b) and sw_y >= 0:
            b[sw_x][sw_y] -= 1


print(n_queens(4))
print(n_queens(8))


###############initial attempt###################

# def n_queens(n):
#     #create board
#     board = []
#     for i in range(n):
#         board.append([0 for j in range(n)])

#     result = main(board, [], 0, 0, None)
#     count = 0
   
#     return print_board(result)

# def main(b, queue, i, j, last_space):

#     if i >= len(b):
#         return b

#     search_board = search(b, queue)
#     open_space = 0
   
#     if search_board:
#         open_space = search_board[j]
        
#     if place_piece(b, open_space):
#         main(b, queue, i, j, open_space)
  

#     if last_space != None:
#         unplace_piece(b, last_space)
#         search_board = search(b, queue)
#         print(search_board)
#         place_piece(b, search_board[j])

#     return b

# def search(b, queue):
#     print('hello from search')
#     print_board(b)
#     queue = []
#     for row in range(len(b)):
#         for spot in range(len(b)):
#             if b[row][spot] == 1 or b[row][spot] == 'Q' or check_adjacency(b, row, spot):
#                 continue
#             queue.append((row, spot))

#     if len(queue) > 0:
#         # position = queue[i]
#         return queue
    
#     # if there are no possible spots
#     return False

# def place_piece(b, p):
#     if p == False:
#         return False

#     x = p[0]
#     y = p[1]

#     cur = b[x][y]

#     if cur != 1:
#         mark_row(b, x)
#         mark_column(b, y)
#         mark_diagonals(b,x,y)
#         b[x][y] = 'Q'
#         print('Hello from place_piece')
#         print_board(b)
#         return True

# #count all queens on current board
# def count_queens(b):
#     count = 0
#     for row in b:
#         for spot in row:
#             if spot == 'Q':
#                 count += 1
#     return count

# #print out board
# def print_board(b):
#     for row in b:
#         for spot in row:
#             print(spot, end = " ")
#         print()

# def check_adjacency(b, x, y):
#     adj_list = []

#     up = x-1
#     down = x+1
#     left = y-1
#     right = y+1

#     if up >= 0 and left >= 0:
#         if b[x-1][y-1] == 'Q' or b[x-1][y] == 'Q'or b[x][y-1] == 'Q':
#             adj_list.append(True)
   
#     if down < len(b) and right < len(b):
#         if b[x][y+1] == 'Q' or b[x+1][y+1] == 'Q'  or b[x+1][y] == 'Q':
#             adj_list.append(True)

#     if up >= 0 and right < len(b):
#         if b[x-1][y+1] == 'Q':
#             adj_list.append(True)
    
#     if down < len(b) and left >= 0:
#         if b[x+1][y-1] == 'Q':
#             adj_list.append(True) 
   
#     return True in adj_list

# #mark rows
# def mark_row(b, x):
#     for i in range(len(b)):
#         b[x][i] += 1
#     return b

# #mark columns
# def mark_column(b,y):
#     for i in range(len(b)):
#         b[i][y] += 1
#     return b

# #mark diagonals
# def mark_diagonals(b,x,y):
#     nw_x, nw_y = x, y
#     ne_x, ne_y = x, y
#     sw_x, sw_y = x, y
#     se_x, se_y = x, y
   
#     for i in range(len(b)):
#         nw_x -= 1
#         nw_y -= 1
        
#         ne_x -= 1
#         ne_y += 1

#         sw_x += 1
#         sw_y -= 1

#         se_x += 1
#         se_y += 1

#         if nw_x >= 0 and nw_y >= 0:
#             b[nw_x][nw_y] += 1
     
#         if ne_x >= 0 and ne_y < len(b):
#             b[ne_x][ne_y] += 1

#         if se_x < len(b) and se_y < len(b):
#             b[se_x][se_y] += 1

#         if sw_x < len(b) and sw_y >= 0:
#             b[sw_x][sw_y] += 1

# def unplace_piece(b, p):
#     if p == 0:
#         return b
    
#     x = p[0]
#     y = p[1]

#     unmark_row(b, x)
#     unmark_column(b, y)
#     unmark_diagonals(b, x, y)

#     print('hello from unplace_piece')
#     print(p)
#     print_board(b)

#     return b

# def unmark_row(b, x):
#     for i in range(len(b)):
#         b[x][i] -= 1
#     return b

# def unmark_column(b,y):
#     for i in range(len(b)):
#         b[i][y] -= 1
#     return b

# def unmark_diagonals(b,x,y):
#     nw_x, nw_y = x, y
#     ne_x, ne_y = x, y
#     sw_x, sw_y = x, y
#     se_x, se_y = x, y
   
#     for i in range(len(b)):
#         nw_x -= 1
#         nw_y -= 1
        
#         ne_x -= 1
#         ne_y += 1

#         sw_x += 1
#         sw_y -= 1

#         se_x += 1
#         se_y += 1

#         if nw_x >= 0 and nw_y >= 0:
#             b[nw_x][nw_y] -= 1
     
#         if ne_x >= 0 and ne_y < len(b):
#             b[ne_x][ne_y] -= 1

#         if se_x < len(b) and se_y < len(b):
#             b[se_x][se_y] -= 1

#         if sw_x < len(b) and sw_y >= 0:
#             b[sw_x][sw_y] -= 1
  
  
# print(n_queens(4))