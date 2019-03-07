import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve(["flower","flow","flight"]),
            "fl"
        ),
    def test2(self):
        self.assertEqual(
            solve(["racecar","race","car"]),
            ""
        ),
    def test3(self):
        self.assertEqual(
            solve(["aa", "a"]),
            "a"
        )

def solve(strs):
    # find the shortest string in the list
    # to be compared with all other words
    result = ""
    start = min(strs, key=len)


    # compare each letter at a time with every word and if every word shares the letter in common, concate to results
    # otherwise stop the loops going through each word and each letter if a letter does not repeat consecutively
    for i, j in enumerate(start):
        count = 0
        for word in range(len(strs)):
            cur = strs[word]
            if cur[i] == j:
                count += 1
            else:
                break
        if count == len(strs):
            result += j
            count = 0
        else:
            break  

    return result

if __name__ == "__main__":
    unittest.main()