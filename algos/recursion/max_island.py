import unittest

class test(unittest.TestCase):
	def test1(self):
		self.assertEqual(
		max_area_of_island([[1,1,0,0,0],[1,1,1,0,0],[0,0,0,1,1],[0,0,0,1,1]]),
		5
		),
	def test2(self):
		self.assertEqual(
		max_area_of_island([[0,0,0], [0,1,0],[0,0,1]]),
		1
		)

def check_adj(grid, x, y, possible_moves, visited):
	if y-1 >= 0:
		if grid[x][y-1] == 1:
			possible_moves.append((x, y-1))
	if x-1 >= 0:
		if grid[x-1][y] == 1:
			possible_moves.append((x-1, y))
	if y+1 < len(grid[0]):
		if grid[x][y+1] == 1:
			possible_moves.append((x, y+1))
	if x+1 < len(grid):
		if grid[x+1][y] == 1:
			possible_moves.append((x+1, y))

def find_max(grid, row, col, visited):
	count = 0;
	possible_moves = [(row, col)];
	while possible_moves:
		cur = possible_moves.pop()
		if cur not in visited:
			visited.add(cur)
			count += 1
			check_adj(grid, cur[0], cur[1], possible_moves, visited)
	return count
	
def solve(grid, i, j):
	cur_max = 0
	max_island = 0
	visited = set()

	for row in range(i):
		for col in range(j):
			if grid[row][col]== 1:
	    			cur_max = find_max(grid, row, col, visited)
			if cur_max > max_island:
				max_island = cur_max
	return max_island				

def max_area_of_island(grid):
	i = len(grid)
	j = len(grid[0])
	return solve(grid, i, j)
if __name__ == "__main__":
	unittest.main()
