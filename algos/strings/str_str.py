# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

import unittest

class test_strStr(unittest.TestCase):
    def test1_str_str(self):
        self.assertEqual(
            str_str('hello', 'll'),
            2
        )
    def test2_str_str(self):
        self.assertEqual(
            str_str('aaaa', 'bba'),
            -1
        )

def str_str(haystack,needle):
    return haystack.find(needle)

if __name__ == "__main__":
    unittest.main()
