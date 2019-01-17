def n_queens(n):
    #create board
    board = []
    for i in range(n):
        board.append([0 for j in range(n)])

    result = main(board, [], 0, 0, None)
    count = 0
    count = max(count, count_queens(result))
    # print(count)

    return print_board(result)

def main(b, queue, i, j, last_space):
    print('this is the last selected spot: ', end='')
    print(last_space)

    if i >= len(b):
        return b

    search_board = search(b, queue)
    open_space = 0
   
    if search_board:
        open_space = search_board[j]
        
    if place_piece(b, open_space):
        main(b, queue, i+1, j, open_space)
    
    print(last_space)
    if last_space != None:
        unplace_piece(b, last_space)
    #unplace_
    # print(last_space)
    # unplace_piece(b, last_space)
    # open_space = search_board[j+1]
    # place_piece(b, open_space)

    return b

def search(b, queue):
    queue = []
    for row in range(len(b)):
        for spot in range(len(b)):
            if b[row][spot] == 1 or b[row][spot] == 'Q':
                continue
            queue.append((row, spot))

    if len(queue) > 0:
        # position = queue[i]
        return queue
    
    # if there are no possible spots
    return False

def place_piece(b, p):
    if p == False:
        return False

    x = p[0]
    y = p[1]

    cur = b[x][y]

    if cur != 1:
        mark_row(b, x)
        mark_column(b, y)
        mark_diagonals(b,x,y)
        b[x][y] = 'Q'
        return True

#count all queens on current board
def count_queens(b):
    count = 0

    for row in b:
        for spot in row:
            if spot == 'Q':
                count += 1
    return count

#print out board
def print_board(b):
    for row in b:
        for spot in row:
            print(spot, end = " ")
        print()

#mark rows
def mark_row(b, x):
    for i in range(len(b)):
        b[x][i] = 1
    return b

#mark columns
def mark_column(b,y):
    for i in range(len(b)):
        b[i][y] = 1
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
            b[nw_x][nw_y] = 1
     
        if ne_x >= 0 and ne_y < len(b):
            b[ne_x][ne_y] = 1

        if se_x < len(b) and se_y < len(b):
            b[se_x][se_y] = 1

        if sw_x < len(b) and sw_y >= 0:
            b[sw_x][sw_y] = 1

def unplace_piece(b, p):
    x = p[0]
    y = p[1]

    unmark_row(b, x)
    unmark_column(b, y)
    # unmark_diagonals(b,x,y)
    print_board(b)

    return b

def unmark_row(b, x):
    for i in range(len(b)):
        b[x][i] = 0
    return b

def unmark_column(b,y):
    for i in range(len(b)):
        b[i][y] = 0
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
            b[nw_x][nw_y] = 0
     
        if ne_x >= 0 and ne_y < len(b):
            b[ne_x][ne_y] = 0

        if se_x < len(b) and se_y < len(b):
            b[se_x][se_y] = 0

        if sw_x < len(b) and sw_y >= 0:
            b[sw_x][sw_y] = 0
  
  
print(n_queens(4))