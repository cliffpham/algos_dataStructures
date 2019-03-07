import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            unique_paths(3,2),
            3
        ),
    def test2(self):
        self.assertEqual(
            unique_paths(7,3),
            28
        )

def recur(m, n, cache):
    ck = "%s:%s" % (m, n)

    if ck in cache:
        return cache[ck]

    if m == 0 and n == 0:
        return 1
    
    if m < 0 or n < 0:
        return 0
    
    l = recur(m-1, n, cache) 
    r = recur(m, n-1 , cache) 
    cache[ck] = l + r

    return l + r

def unique_paths(m, n):
    return recur(m - 1, n - 1, {})

if __name__ == "__main__":
    unittest.main()