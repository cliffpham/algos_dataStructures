import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            find_diff('abcd', 'abcde'),
            'e'
        )

def find_diff(s, t):
    t = list(t)
    seen = set(s)

    for i in s:
        if i in seen:
            t.remove(i)

    return t[0]

if __name__ == "__main__":
    unittest.main()
    
