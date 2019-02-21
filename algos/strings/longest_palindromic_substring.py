import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertAlmostEquals(
            palindrome("babad"),
            "bab"
        )

def palindrome(s):
    pivot = 1
    new_str = convert_str(s)
    count = 0
    flag = True
    seen = dict()
    result = []

    if s == "":
        return ""
    
    while pivot < len(new_str)-1:
        if new_str[pivot-1] != new_str[pivot+1]:
            result.append(count)
            pivot += 1
            
        else:
            l = pivot - 1
            r = pivot + 1
            sub_string = '' + new_str[pivot]
            while flag:
                if new_str[l] == new_str[r]:
                    sub_string = new_str[l] + sub_string + new_str[r] 
                    count += 1
                    l -= 1
                    r += 1
                else:
                    result.append(count)
                    if sub_string not in seen:
                        seen[sub_string] = count
                    count = 0
                    flag = False
            pivot += 1
            flag = True
 
    return find_all_substrings(seen)

def find_all_substrings(seen):
    longest_num = 0
    longest = None

    for i in seen:
        if seen[i] > longest_num:
            longest_num = seen[i]
            longest = i

    return longest.replace('#', '')

def convert_str(s):
    s = '#'.join(s)
    s = '#' + s + '#'
    s = '^' + s + '$'
    
    return s
    
if __name__ == "__main__":
    unittest.main()

