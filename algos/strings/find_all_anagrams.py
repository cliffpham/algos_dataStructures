from collections import Counter
import unittest

class Test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
            find_all_anagrams("cbadebacfg", "abc"),
            [0, 5]
        )

def find_all_anagrams(s, p):
    # basically get an integer value of the possible anagram
    p_count = Counter(p)
    # initially set the window to the start of the string
    s_count = Counter(s[:len(p)-1])
    result = []
    # an additional anchor point to keep track of which value to remove from window
    j = 0
    
    # start from where the current window ends till the end of the string
    for i in range(len(p) - 1, len(s)):
        # keep track of current letter
        cur = s[i]
        # keep track of oldest letter
        oldest = s[j]
        s_count[cur] += 1
        # if window and p_count match add the anchor to the result array
        if s_count == p_count:
            result.append(j)
        # adjust window by subtracting the value of the oldest character from the window
        s_count[oldest] -= 1
        # if the oldest value == 0 remove
        if s_count[oldest] == 0:
            del s_count[oldest]
        # move anchor one point forward 
        j += 1
    
    return result

if __name__ == "__main__":
    unittest.main()
