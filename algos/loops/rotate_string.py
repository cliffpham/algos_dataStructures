import unittest

class test_rotate_string(unittest.TestCase):
    def test1(self):
        self.assertTrue(
            rotate_string('abc', 'cab')
        )
    def test2(self):
        self.assertFalse(
            rotate_string('aa', 'a')
        )

def rotate_string(A, B):
    
    if A == B:
        return True

    if len(A) != len(B):
        return False

    new_s = ''
    for i in range(len(A)):
        i = A
        new_s += i
   
    for i in range(len(new_s)):
        if new_s[i:i+len(B)] == B:
            return True

    return False

if __name__ == "__main__":
    unittest.main()