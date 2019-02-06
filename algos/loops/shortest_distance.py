import unittest

class test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            shortest_dist('loveleetcode', 'e'),
            [3,2,1,0,1,0,0,1,2,2,1,0]
        )

def shortest_dist(s, c):
    p_dist = []
    result = []
    
    for i in range(len(s)):
        if s[i] == c:
            p_dist.append(i)
    
    for i in range(len(s)):
        result.append(min([abs(t - i) for t in p_dist]))

    return result

if __name__ == '__main__':
    unittest.main()