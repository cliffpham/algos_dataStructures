import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
        solve([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]),
        35
    )

def find_max_cols(grid, heights):
    for i in range(len(grid)):
        result = []
        for j in range(len(grid[i])):
            result.append(grid[j][i])
        heights[i] = max(result)

def create_table(grid):
    heights = dict()
    find_max_cols(grid, heights)
    return heights


def solve(grid):
    heights = create_table(grid)
    total_change = 0

    for i in range(len(grid[0])):
        cur_max = max(grid[i])
        for j in range(len(grid)):
            cur = grid[i][j]
            cur_min = min(heights[j], cur_max)
            if cur < cur_min:
                total_change += cur_min - cur
    return total_change

if __name__ == "__main__":
    unittest.main()
