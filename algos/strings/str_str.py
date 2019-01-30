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
    # return haystack.find(needle)

# other solution
    if len(haystack)==0 and len(needle)==0:
        return 0

    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    else:
        return -1

if __name__ == "__main__":
    unittest.main()


