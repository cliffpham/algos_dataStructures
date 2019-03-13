import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([[1,3,1],[1,5,1],[4,2,1]]),
            7
        ),
    def test2(self):
        self.assertEqual(
            solve([[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]),
            47
        )

def recur(grid, row, col, i, j, cache):
    ck = "%s:%s" % (i,j)

    if ck in cache:
        return cache[ck]

    if i == row and j == col:
        return grid[i][j]
    
    if i > row or j > col:
        return float('inf')

    l = recur(grid, row, col, i, j+1, cache) + grid[i][j]
    r = recur(grid, row, col, i+1, j, cache) + grid[i][j]

    cache[ck] = min(l,r)

    return min(l, r)

def solve(grid):
    row = len(grid)
    col = len(grid[0])

    return recur(grid, row-1, col-1, 0, 0, {})

if __name__ == "__main__":
    unittest.main()

#brute force / all paths from top left to bottom right

# def recur(grid, row, col, i, j, accum, paths):
#     if i == row and j == col:
#         accum += grid[i][j]
#         paths.append(accum)
#         return accum
    
#     if i > row or j > col:
#         return float('-inf')

#     recur(grid, row, col, i, j+1, accum + grid[i][j], paths) 
#     recur(grid, row, col, i+1, j, accum + grid[i][j], paths) 
 
#     return min(paths)

# def solve(grid):
#     row = len(grid)
#     col = len(grid[0])

#     return recur(grid, row-1, col-1, 0, 0, 0, [])