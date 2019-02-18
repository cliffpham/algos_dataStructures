import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertTrue(
            word_search([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"),
            True
        ),

    def test2(self):
        self.assertTrue(
            word_search([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS" ),
            True
        )

def word_search(board, word):
    word = list(word)
    i = 0
    sheet = []

    for row, _ in enumerate(board):
        for tile, _ in enumerate(board[row]):
            len_col = len(board)
            len_row  = len(board[row])

            if board[row][tile] == word[i]:
                seen = set()
                origin = (row,tile)
                solve = recur(board, origin, word, len_col, len_row, i+1, seen)
                sheet.append(solve)
                i = 0

            else:
                sheet.append(False)

   
    if True in sheet:
        return True

    return False

def recur(board, origin, word, len_col, len_row, i, seen):
    #base case
    if i == len(word):
        return True

    seen.add(origin)
    possible_moves = check_adj(board, origin, word, len_col, len_row, i, seen)

    while possible_moves:
        candidate = possible_moves.pop()
        if recur(board, candidate, word, len_col, len_row, i+1, seen):
            return True
        else:
            seen.remove(candidate)
        
    return False

def check_adj(board, coordinates, word, len_col, len_row, i, seen):
    x = coordinates[0]
    y = coordinates[1]
    possible_moves = []
    cur_char = word[i]

    if y-1 >= 0:
        if board[x][y-1] == cur_char:
            new_y = y-1
            coordinates = (x, new_y)

            if coordinates in seen:
                pass
            else:
                possible_moves.append(coordinates)
    
    if x-1 >= 0:
        if board[x-1][y] == cur_char:
            new_x = x-1
            coordinates = (new_x,y)

            if coordinates in seen:
                pass
            else:
                possible_moves.append(coordinates)

    if y+1 < len_row:
        if board[x][y+1] == cur_char:
            new_y = y+1
            coordinates = (x, new_y)

            if coordinates in seen:
                pass
            else:
                possible_moves.append(coordinates)

    if x+1 < len_col:
        if board[x+1][y] == cur_char:
            new_x = x+1
            coordinates = (new_x, y)

            if coordinates in seen:
                pass
            else:
                possible_moves.append(coordinates)

    if len(possible_moves) >= 1:
        return possible_moves
    
    return False

if __name__ == "__main__":
    unittest.main()


# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# b2 = [
#     ["b","b"],
#     ["a","b"],
#     ["b","a"]]

# b3 = [["C","A","A"],
#       ["A","A","A"],
#       ["B","C","D"]]

# b4 = [["A","B","C","E"],
#       ["S","F","E","S"],
#       ["A","D","E","E"]]


# word = "ABCCED"
# word2 = "SEE"

# print(word_search(board,word))
# print(word_search(board,word2))
# print(word_search(board,'ABCB'))
# print(word_search(b3,"AAB"))
# print(word_search(b4,"ABCESEEEFS"))
