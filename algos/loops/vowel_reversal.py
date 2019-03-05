import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve('Hello'),
            'Holle'
        ),
    
    def test2(self):
        self.assertEqual(
            solve('!!!'),
            '!!!'
        ),
    
    def test3(self):
        self.assertEqual(
            solve(''),
            ''
        )

def solve(s):
    result = list(s)
    vowels = set(list('aeiouAEIOU'))
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] not in vowels:
            l += 1
        
        if s[r] not in vowels:
            r -= 1

        if s[l] in vowels and s[r] in vowels:
            result[l] = s[r]
            result[r] = s[l]
            l += 1
            r -= 1

    return ''.join(result)

if __name__ == "__main__":
    unittest.main()