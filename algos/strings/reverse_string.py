import unittest

class test_reverse_string(unittest.TestCase):
    def test1_reverse_string(self):
        self.assertEqual(
            reverse_string(['H', 'e', 'l', 'l', 'o']),
            ['o', 'l', 'l', 'e', 'H']
        )

def reverse_string(s):        
    left_index = 0
    right_index = len(s) - 1
        
    while left_index < right_index:
        temp = s[left_index]
        s[left_index] = s[right_index]
        s[right_index] = temp
        left_index += 1
        right_index -= 1
    
    return s

if __name__ == "__main__":
    unittest.main()