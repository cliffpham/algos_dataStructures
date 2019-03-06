import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            ascii_deletion_distance('sea', 'eat'),
            231
        )

def score(s):
    return sum([ord(i) for i in s])

def recur(s1, s2, i, j, cache):
    ck = "%s:%s" % (i,j)

    if ck in cache:
        return cache[ck]

    if i >= len(s1):
        return score(s2[j:])
    if j >= len(s2):
        return score(s1[i:])
    
    a = recur(s1,s2,i+1,j, cache) + ord(s1[i])
    b = recur(s1, s2, i, j+1, cache) + ord(s2[j])
    
    k = ord(s1[i]) + ord(s2[j]) if s1[i] != s2[j] else 0
    c = recur(s1,s2,i+1,j+1, cache) + k
    
    cache[ck] = min(a,b,c)
    return min(a,b,c)

def ascii_deletion_distance(str1, str2):
    result = recur(str1, str2, 0, 0, {})

    return result

if __name__ == "__main__":
    unittest.main()
    
