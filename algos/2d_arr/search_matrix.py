import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
                solve([[1,3,4,5],[6,8,10,11],[16,17,20,23],[25,28,30,34],[36,39,44,50]], 12),
                False
                ),
    def test2(self):
        self.assertEqual(
                solve([[1,3,4,5],[6,8,10,11],[16,17,20,23],[25,28,30,34],[36,39,44,50]], 50),
                True
                )

def search_row(matrix, target, row):
    size = len(matrix[0])

    for i in range(size):
        if matrix[row][i] == target:
            return True
    return False

def move_down(matrix, target, row):
    if row == -1:
        return False

    start = matrix[row][0]
    end = matrix[row][len(matrix[0])-1]
    if target < start:
        return move_down(matrix, target, row-1)
    elif target >= start and target <= end:
        if search_row(matrix,target, row):
            return True
        else:
            return False

def move_up(matrix, target, row):
    if row > len(matrix) - 1:
        return False

    start = matrix[row][0]
    end = matrix[row][len(matrix[0])-1]
    if target > end:
        return move_up(matrix, target, row+1)
    elif target >= start and target <= end:
        if search_row(matrix, target, row):
            return True
        else:
            return False

def solve(matrix, target):
    if not matrix:
        return False
    if not matrix[0]:
        return False
    
    row = len(matrix) // 2
    start = matrix[row][0]
    end = matrix[row][len(matrix[0])-1]

    if target >= start and target <= end:
        if search_row(matrix, target, row):
            return True
    elif target < start:
        if move_down(matrix, target, row - 1):
            return True
    elif target > end:
        if move_up(matrix, target, row + 1):
            return True
    return False

if __name__ == "__main__":
    unittest.main()
