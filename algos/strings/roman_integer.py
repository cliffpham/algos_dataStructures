import unittest

# For this solution
# necessary components: dictionary, function to handle outliers i.e. values consisting 4 or 9
# caveats for loop method: keep check of array boundary
# loop through the array totaling the value at each index 
# if the cur value is either I X or C go through the function that handles special cases
# if any of the two conditions match return that specific value and add to the total
# if the copy_total is greater than the total means the special case was handled and so we
# need to increment the iterator by 2 instead of 1

class Test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
        solve("DCXXI"),
        621
        ),
    def test_two(self):
        self.assertEqual(
        solve("LVIII"),
        58
        )

def four_nine(s, i):
    if i+1 >= len(s):
        return 0
    elif s[i] == 'I' and s[i+1] == 'V':
        return 4
    elif s[i] == 'I' and s[i+1] == 'X':
        return 9
    elif s[i] == 'X' and s[i+1] == 'L':
        return 40
    elif s[i] == 'X' and s[i+1] == 'C':
        return 90
    elif s[i] == 'C' and s[i+1] == 'D':
        return 400
    elif s[i] == 'C' and s[i+1] == 'M':
        return 900
    return 0

def solve(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    total = 0

    while i < len(s):
        cur = s[i]
        if s[i] == 'I' or s[i] == 'X' or s[i] == 'C':
            total_copy = total
            total_copy += four_nine(s,i)
            if total_copy > total:
                total = total_copy
                i += 2
            else:
                total += roman[cur]
                i += 1
        else:
            total += roman[cur]
            i += 1
    return total

if __name__ == "__main__":
    unittest.main()
