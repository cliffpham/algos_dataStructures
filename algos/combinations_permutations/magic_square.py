import unittest

class test_magic_square(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            magic_square([[4,9,2],[3,5,7],[8,1,5]]),
            1
        )
    def test2(self):
        self.assertEqual(
            magic_square([[4,5,8],[2,4,1],[1,9,7]]),
            14
        )

def magic_square(arr):
    n = []

    all_n = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],[4,9,2,3,5,7,8,1,6],[2,9,4,7,5,3,6,1,8],[8,3,4,1,5,9,6,7,2],[4,3,8,9,5,1,2,7,6],[6,7,2,1,5,9,8,3,4],[2,7,6,9,5,1,4,3,8]]

    for row in arr:
        for item in row:
            n.append(item)

    allsum = []
    for l in all_n:
        # print(([abs(n[i]-l[i]) for i in range(9)]))
        allsum.append(sum([abs(n[i]-l[i]) for i in range(9)]))

    return min(allsum)


if __name__ == "__main__":
    unittest.main()

# def magic_square(b):

#     nb = [row[:] for row in b]
#     output = []
    
#     #find diagonals, rows, and or cols that already = the magic constant
#     immutables = scan_diagonals(b)
#     scan_rows(b, immutables)
#     scan_cols(b, immutables)

#     #find candidates on the board that may be mutated
#     spots = find_mutable_spots(b, immutables)
    
#     #return new board that is a magic square
#     result = solve(b, spots, nb, immutables, 0, output)

#     #compare the first board with the magic square and return the difference
#     c = compare_boards(b, result, spots)
    
#     return c

# def solve(b, spots, nb, immutables, i, output):
#     if i == len(spots):
#         print(nb)
#         return nb

#     spot = spots[i]

#     if place_num(nb, spot):
#         if solve(b, spots, nb, immutables, i+1, output):
#             return nb
#         undo_move(nb, spot)
    

# def find_mutable_spots(b, immutables):
#     q = []
    
#     for row in range(len(b)):
#         for col in range(len(b)):
#             if (row, col) in immutables: continue
#             q.append((row,col))
    
#     return q

# def place_num(nb, spot):
#     x = spot[0]
#     y = spot[1]

#     #if the either the row or col that the spot already exists on equals the magic constant continue to next spot
#     if check_row(nb, x, y, nb[x][y]) or check_col(nb, x, y, nb[x][y]):
#         return True

#     # else find a number that will = magic constant
#     options = [1,2,3,4,5,6,7,8,9]

#     for option in options:
#         if check_row(nb, x, y, option) or check_col(nb,x, y, option):
#             nb[x][y] = option
#             return True

#     return False

# #undo previous move if no move works
# def undo_move(nb, spot):
#     x = spot[0]
#     y = spot[1]

#     nb[x][y] = 0

# def compare_boards(b, nb, spots):
#     c = []
#     for x,y in spots:
#          c.append(abs(b[x][y] - nb[x][y]))
#     return sum(c)
        
# def check_row(nb, x, y, option):
#     temp = nb[x][y]
#     val = 0
#     nb[x][y] = option

#     for i in range(len(nb)):
#         val = val + nb[x][i]
    
#     if val == 15:
#         nb[x][y] = temp
#         return True
   
#     nb[x][y] = temp
#     return False

# def check_col(nb, x, y, option):
#     temp = nb[x][y]
#     val = 0
#     nb[x][y] = option

#     for i in range(len(nb)):
#         val = val + nb[i][y]
    
#     if val == 15:
#         nb[x][y] = temp
#         return True
   
#     nb[x][y] = temp
#     return False
    
# def scan_diagonals(b):
#     immutables = set()
#     if b[0][0] + b[1][1] + b[2][2] == 15:
#         for i in range(len(b)):
#             immutables.add((i,i))

#     if b[0][2] + b[1][1] + b[2][0] == 15:
#         r = len(b) - 1
#         for i in range(len(b)):
#             immutables.add((i, r-i))
    
#     return immutables

# def scan_rows(b, immutables):
#     if b[0][0] + b[0][1] + b[0][2] == 15:
#         for i in range(len(b)):
#             if (0, i) in immutables: continue
#             immutables.add((0,i))
    
#     if b[1][0] + b[1][1] + b[1][2] == 15:
#         for i in range(len(b)):
#             if (1, i) in immutables: continue
#             immutables.add((1,i))   
    
#     if b[2][0] + b[2][1] + b[2][2] == 15:
#         for i in range(len(b)):
#             if (2, i) in immutables: continue
#             immutables.add((2,i)) 
#     return

# def scan_cols(b, immutables):
#     if b[0][0] + b[1][0] + b[2][0] == 15:
#         for i in range(len(b)):
#             if (i, 0) in immutables: continue
#             immutables.add((i,0))
    
#     if b[0][1] + b[1][1] + b[2][1] == 15:
#         for i in range(len(b)):
#             if (i, 1) in immutables: continue
#             immutables.add((i,1))   
    
#     if b[0][2] + b[1][2] + b[2][2] == 15:
#         for i in range(len(b)):
#             if (i, 2) in immutables: continue
#             immutables.add((i,2)) 
#     return




