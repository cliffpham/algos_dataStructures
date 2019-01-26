import unittest

class test_rm_duplicates(unittest.TestCase):
    def test_rm_duplicates(self):
        self.assertEqual(
            rm_duplicates([1,2,2,1,3,1,4]),
            [4,1,3,2]
        )

def rm_duplicates(arr):
    dups = set()
    result = []

    while arr:
        cur = arr.pop()
        if cur in dups: continue
        result.append(cur)
        dups.add(cur)

    return result

if __name__ == "__main__":
    unittest.main()