import unittest
from collections import Counter

class Test(unittest.TestCase):
    def test1(self):
        self.assertEquals(
            solve("adobecodebanc", "abc"),
            "banc"
        ),
    def test2(self):
        self.assertEquals(
            solve("aaaaaaa", "b"),
            ''
       ),
    def test3(self):
        self.assertEquals(
            solve("this is a test string", "tist"),
            "t stri"
        ),
    def test4(self):
        self.assertEquals(
            solve("a","a"),
            "a"
        ),
    def test5(self):
        self.assertEquals(
            solve("ab", "b"),
            "b"
        )

def solve(s,t):
    hashmap = Counter(t)
    counter = len(t)
    start = 0
    end = 0
    result = ''
    
    if len(t) > len(s):
        return result
    
    for end in range(len(s)):
        if hashmap[s[end]] > 0:
            counter -= 1
        hashmap[s[end]] -= 1
        
        while counter == 0:
            cur_window = s[start: end + 1]
            if not result or len(result) > len(cur_window):
                result = s[start:end + 1]
            hashmap[s[start]] += 1
            
            if hashmap[s[start]] > 0:
                counter += 1
            start += 1
            
    return result

#Initial solution TLE

#def check_window(s_count, t_count, cur_window, i, j, cur_min):
#    if cur_min != -1 and len(cur_window) >= cur_min:
#        return True
#    
#    window = s_count.copy()
#    check = t_count.copy()
#    
#    check = check - window
#    
#    return len(check) == 0
#
#def adjust_window(s, t, i, j, s_count):
#    fp = s[i]
#    s_count[fp] -= 1
#    if s_count[fp] == 0:
#        del s_count[fp]
#    i += 1
#    for k in range(j, i + len(t) - 1, -1):
#        cur = s[k]
#        s_count[cur] -= 1
#        if s_count[cur] == 0:
#            del s_count[cur]
#    return i
#    
#def solve(s, t):
#    i = 0
#    j = len(t)
#    s_count = Counter(s[i:j])
#    t_count = Counter(t)
#    cur_min = -1
#    result = ''
#
#    if len(t) > len(s):
#        return result
#    
#    while j <= len(s):
#        cur_window = s[i:j]
#        if check_window(s_count, t_count, cur_window, i, j, cur_min):
#            if cur_min == -1 or len(cur_window) < cur_min:
#                cur_min = len(cur_window)
#                result = cur_window
#                i = adjust_window(s, t, i, j - 1, s_count)
#                j = i + len(t)
#            else:
#                i = adjust_window(s, t, i, j-1, s_count)
#                j = i + len(t)
#        else:
#            j += 1
#            cur_window = s[i:j]
#            sp = cur_window[len(cur_window) - 1]
#            s_count[sp] += 1
#            
#    return result
#
if __name__ == "__main__":
    unittest.main()
