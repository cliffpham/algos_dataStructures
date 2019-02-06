import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEquals(
            climbStairs(3),
            3
        )

def climbStairs(n):
    i = 1
    steps = [1,2]
    cache = {}
    for x in range(n+1):
        cache[x] = 0
        
    return main(steps, n, i, cache)

def main(steps, n, i, cache):
    cache[0] = 1
    
    if i > n:
        return
    for s in steps:
        if i - s >= 0:
            cache[i] += cache[i-s]
    main(steps, n, i+1, cache)
    
    return cache[n]

if __name__ == "__main__":
    unittest.main()