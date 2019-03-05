import unittest

class Test (unittest.TestCase):
    def test1(self):
        self.assertEqual(
            floodfill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        )
    def test2(self):
        self.assertEqual(
            floodfill([[0,0,0],[0,0,0]], 0, 0, 2),
            [[2, 2, 2], [2, 2, 2]]
        )

def check_adj(image, coord, new_color, stack, orig):
    x = coord[0]
    y = coord[1]

    image[x][y] = new_color
   
    if x-1 >= 0:
        if image[x-1][y] == orig:
            image[x-1][y] = new_color
            stack.append((x-1, y))
    
    if x+1 < len(image):
        if image[x+1][y] == orig:
            image[x+1][y] = new_color
            stack.append((x+1, y))
    
    if y-1 >= 0:
        if image[x][y-1] == orig:
            image[x][y-1] = new_color
            stack.append((x, y-1))
    
    if y+1 <= len(image[0]) - 1:
        if image[x][y+1] == orig:
            image[x][y+1] = new_color
            stack.append((x, y+1))


def floodfill(image, x, y, new_color):
    stack = [(x,y)]
    orig = image[x][y]
    visited = set()

    while stack:
        coord = stack.pop()
        if coord not in visited:
            check_adj(image, coord, new_color, stack, orig)
            visited.add(coord)
    
    return image

if __name__ == "__main__":
    unittest.main()