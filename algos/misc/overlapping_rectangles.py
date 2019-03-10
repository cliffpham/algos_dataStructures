import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([0,10,10,0], [5,5,15,0]),
            False    
        ),
    def test2(self):
        self.assertEqual(
            solve([0,0,1,1],[1,0,2,1]),
            False
        ),
    def test3(self):
        self.assertEqual(
            solve([0,0,2,2],[1,1,3,3]),
            True
        )   

def solve(rec1, rec2):
    bl = rec1[:2]
    tr = rec1[2:]
    bl2 = rec2[:2]
    tr2= rec2[2:]
  

    if tr[0] <= bl2[0] or tr2[0] <= bl[0]:
        return False

    if tr[1] <= bl2[1] or tr2[1] <= bl[1]:
        return False

    return True 

if __name__ == "__main__":
    unittest.main()


