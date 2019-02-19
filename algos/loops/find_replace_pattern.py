import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            find_and_replace(["abc","deq","mee","aqq","dkd","ccc"], "abb"),
            ["mee", "aqq"]
        )

def find_and_replace(words, pattern):
    searching_for = find(pattern)
    result = []

    for i in words:
        p = find(i)
        if p == searching_for:
            result.append(i)

    return result

def find(pattern):
    seen = {}
    s = ''
    for i in range(len(pattern)):
        if pattern[i] in seen:
            s += str(seen[pattern[i]])
        else:
           seen[pattern[i]] = i
           s += str(seen[pattern[i]])
    return s

if __name__ == "__main__":
    unittest.main()