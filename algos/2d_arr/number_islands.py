import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEquals(solve([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]),
                3
        ),
    def test2(self):
        self.assertEquals(solve([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]),
                1
        )

def find_neighbors(grid, cur, to_visit, visited):
    x = cur[0]
    y = cur[1]

    if x - 1 >= 0:
        if grid[x-1][y] == "1" and (x-1, y) not in visited:
            to_visit.append((x-1,y))
    if y - 1 >= 0:
        if grid[x][y-1] == "1" and (x,y-1) not in visited:
            to_visit.append((x,y-1))
    if x + 1 <= len(grid) - 1:
        if grid[x+1][y] == "1" and (x+1,y) not in visited:
            to_visit.append((x+1,y))
    if y + 1 < len(grid[0]):
        if grid[x][y+1] == "1" and (x,y+1) not in visited:
            to_visit.append((x, y+1))

def find_size(grid, coord, visited):
    to_visit = [coord]

    while to_visit:
        cur = to_visit.pop()
        visited.add(cur)
        find_neighbors(grid, cur, to_visit, visited)

def solve(grid):
    visited = set()
    count = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            cell = grid[x][y]
            coord = (x,y)
            if cell == "1" and coord not in visited:
                count += 1
                find_size(grid, coord, visited)

    return count
            
if __name__ == "__main__":
    unittest.main()
