import unittest

class test_first_unique(unittest.TestCase):
    def test1_first_unique(self):
        self.assertEqual(
            first_unique('loveleetcode'),
            2
        )
    def test2_first_unique(self):
        self.assertEqual(
            first_unique('leetcode'),
            0
        )
    def test3_first_unique(self):
        self.assertEqual(
            first_unique('lllly'),
            4
        )

    def test4_first_unique(self):
        self.assertEqual(
            first_unique('cc'),
            -1
        )

def first_unique(s):
    seen = {}
    min_val = float('inf')

    for i in range(len(s)):
        if s[i] in seen:
            seen[s[i]] = -1
        else:
            seen[s[i]] = i

    for val in seen.values():
        if val != -1:
            min_val = min(val, min_val)
    
    if min_val == float('inf'):
        return -1
    
    return min_val

#brute force
# def first_unique(s):
#     count = []
#     first_char = -1

#     for n in range(len(s)):
#        n = 0
#        count.append(n)

#     #loop through all characters
#     for i in range(len(s)):
#         count[i] += 1
#         for j in range(i+1, len(s)):
#             if s[j] == s[i]:
#                 count[i] += 1
#                 count[j] += 1

#     #loop through count and find first index that equals 1
#     for i in range(len(count)):
#         if count[i] == 1:
#             first_char = i
#             break

#     return first_char

if __name__ == "__main__":
    unittest.main()
        