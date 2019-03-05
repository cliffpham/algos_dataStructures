import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve("abcd def abcd xyz", "ijk def ijk"),
            "xyz"
        )

def solve(s1, s2):
    seen = {}
    split1 = s1.split()
    split2 = s2.split()
    result = []

    for i in split2:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    
    for i in split1:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1

    for k, v in seen.items():
        if v == 1:
            result.append(k)

    return result

if __name__ == "__main__":
    unittest.main()