import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            strWithout3a3b(4,1),
            'aabaa'
        )

def strWithout3a3b(A, B):
    if A == 0:
      return 'b' * B
    
    elif B == 0:
        return 'a' * A

    elif A == B:
        return 'ab' + strWithout3a3b(A-1, B-1)
    elif A > B:
        return 'aab' + strWithout3a3b(A-2, B-1)
    elif B > A:
        return 'bba' + strWithout3a3b(A-1, B-2)

if __name__ == "__main__":
    unittest.main()