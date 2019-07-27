import bisect
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEquals(
                diagonal_sorting([[1,8,2,3],[4,6,1,7],[8,4,5,2],[6,9,3,3]]),
                [[1,1,2,3],[3,3,2,7],[8,4,5,8],[6,9,4,6]]
                )

def sort_diag(b, to_sort_left, to_sort_right, row, col_size):
    row_size = row
    col = 0
    
    while col <= col_size:
        #print("%s:%s" % (row_size,col))
        b[row_size][col] = to_sort_left[col]
        b[col][row_size] = to_sort_right[col]
        row_size += 1
        col += 1

def diagonal_sorting(b):
    row = 0
    col_size = len(b) - 1
    
    while row < len(b):
       col = 0
       temp_row = row
       to_sort_left = []
       to_sort_right = []
       while col <= col_size:
           bisect.insort(to_sort_left, b[temp_row][col])
           bisect.insort(to_sort_right, b[col][temp_row])
           temp_row += 1
           col += 1
       #print(to_sort_left)
       #print(to_sort_right)
       sort_diag(b,to_sort_left, to_sort_right, row, col_size)
       row += 1
       col_size -= 1

    return b

#    for row in b:
#        for spot in row:
#            print(str(spot) + " ", end="")
#        print()

if __name__ == "__main__":
    unittest.main()
