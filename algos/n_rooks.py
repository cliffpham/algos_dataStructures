def n_rooks(n):
    board = []
    
    for i in range(n):
        board.append([0 for j in range(n)])
    
    result = main(board)

    return print_board(result)

def main(b):
    p = search(b, [])

    place_piece(b, p)

    if place_piece(b, p):
        main(b)

    return b

def search(b, queue):
    for row in range(len(b)):
        for spot in range(len(b)):
            if b[row][spot] == 1 or b[row][spot] == 'R':
                continue
            queue.append((row, spot))
    # print(queue)

    if len(queue) > 0:
        position = queue.pop()
        return position
    
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
        b[x][y] = 'R'
        return True

    return

def mark_row(b, x):
    for i in range(len(b)):
        b[x][i] = 1
    return b

def mark_column(b,y):
    for i in range(len(b)):
        b[i][y] = 1
    return b

def print_board(b):
    for row in b:
        for spot in row:
            print(spot, end = " ")
        print()

print(n_rooks(5))

# def unplace_piece(b, p):
#     x = p[0]
#     y = p[1]

#     unmark_row(b, x)
#     unmark_column(b, y)

#     return b

# def unmark_row(b, x):
#     for i in range(len(b)):
#         board[x][i] = 0
#     return b

# def unmark_column(b,y):
#     for i in range(len(b)):
#         board[i][y] = 0
#     return b

