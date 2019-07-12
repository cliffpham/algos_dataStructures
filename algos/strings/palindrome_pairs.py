import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEquals(
            palindrome_pairs(["code", "edoc", "da", "d"]),
            [(0, 1), (1, 0), (2, 3)]
        )

def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    d = dict()
    result = []
    
    for i, word in enumerate(words):
        d[word] = i
        
    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]
            
            if is_palindrome(suffix) and reversed_prefix in d:
                if i != d[reversed_prefix]:
                    result.append((i, d[reversed_prefix]))
            
            if j > 0 and is_palindrome(prefix) and reversed_suffix in d:
                if i != d[reversed_suffix]:
                    result.append((d[reversed_suffix], i))
    
    return result

if __name__ == "__main__":
    unittest.main()
