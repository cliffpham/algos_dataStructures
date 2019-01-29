import unittest

class test_rm_duplicates(unittest.TestCase):
    def test1_rm_duplicates(self):
        self.assertEqual(
            rm_duplicates([0,0,1,1,2,2,3,3,4]),
            5
        )
    def test2_rm_duplicates(self):
        self.assertEqual(
            rm_duplicates([1,1,2]),
            2
        )
    def test3_rm_duplicates(self):
        self.assertEqual(
            rm_duplicates([]),
            0
        )

def rm_duplicates(arr):
    if len(arr) <= 1:
        return len(arr)

    #two pointer method
    i = 0
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return i+1

if __name__ == "__main__":
    unittest.main()

