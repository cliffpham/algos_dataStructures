import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            unique_paths([[0,0,0],[0,1,0],[0,0,0]]),
            2
        )

def recur(obstacle_grid, row, col, cache):
    ck = "%s:%s" % (row, col)

    if ck in cache:
        return cache[ck]
    
    if obstacle_grid[row][col] == 1:
        return 0

    if row == 0 and col == 0:
        return 1

    if row < 0 or col < 0:
        return 0
    
    l = recur(obstacle_grid, row-1, col, cache) 
    r = recur(obstacle_grid, row, col-1 , cache) 
    cache[ck] = l + r

    return l + r

def unique_paths(obstacle_grid):
    row = len(obstacle_grid[0])
    col = len(obstacle_grid)

    return recur(obstacle_grid, row-1, col-1, {})

if __name__ == "__main__":
    unittest.main()