import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEquals(
            lps("bbbab"),
            4
        ),
    def test2(self):
        self.assertEquals(
            lps("cbbd"),
            2
        )

def lps(s):
    return recur(s, 0, len(s) - 1, cache={})


def recur(s, i, j, cache):
    ck = "%s:%s" % (i,j)

    if ck in cache:
        return cache[ck]

    if i > j:
        return 0

    if i == j:
        return 1
    
    if s[i] == s[j]:
        return recur(s, i+1, j-1, cache) + 2

    l = recur(s, i, j-1, cache)
    r = recur(s, i+1, j, cache)
    cache[ck] = max(l,r)
    
    return max(l,r)

# def palindrome(s):
#     pivot = 1
#     new_str = convert_str(s)
#     count = 0
#     flag = True
#     result = []

#     if s == "":
#         return ""
    
#     while pivot < len(new_str)-1:
#         if new_str[pivot-1] != new_str[pivot+1]:
#             result.append(count)
#             pivot += 1
            
#         else:
#             l = pivot - 1
#             r = pivot + 1
#             while flag:
#                 if new_str[l] == new_str[r]:
#                     count += 1
#                     l -= 1
#                     r += 1
#                 else:
#                     result.append(count)
#                     count = 0
#                     flag = False
#             pivot += 1
#             flag = True
#     print(result)
#     return max(result)

# def convert_str(s):
#     s = '#'.join(s)
#     s = '#' + s + '#'
#     s = '^' + s + '$'
    
#     return s
    
if __name__ == "__main__":
    unittest.main()
