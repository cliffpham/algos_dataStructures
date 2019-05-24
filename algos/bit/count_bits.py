import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
        solve(5),
        [0,1,1,2,1,2]
        )

def count_bits(n):
    count = 0
    while n:
        if n % 2 == 1:
            count += 1
        n = n / 2
    return count

def solve(n):
    result = []
    for cur_num in range(n + 1):
        result.append(count_bits(cur_num))
    return result

if __name__ == "__main__":
    unittest.main()
    
        
