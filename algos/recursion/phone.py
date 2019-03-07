import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve('234'),
            ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
        )

def recur(phone, remaining_word, cur, combinations):
    if len(remaining_word) < 1:
        if cur not in combinations:
            combinations.append(cur)
        return
    
    first = remaining_word[0]
    rest = remaining_word[1:]

    letters = phone[first]

    for letter in letters:
        recur(phone, rest, cur + letter, combinations)

    return combinations

def solve(n):
    phone = {'2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']}

    combinations = []

    if len(n) < 1:
        return combinations

    return recur(phone, n, '', combinations)

if __name__ == "__main__":
    unittest.main()