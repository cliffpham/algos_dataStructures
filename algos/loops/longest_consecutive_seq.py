import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            lcs([1,9,3,10,4,20,2]),
            4
        )

def lcs(arr):
    longest = 0
    cur = 0
    nums = set()

    for i in arr:
        nums.add(i)

    for i in range(len(arr)):
        if arr[i-1] in nums:
            j = arr[i-1]
            while j in nums:
                cur += 1
                j -= 1
                longest = max(cur, longest)
        
        cur = 0
        longest = max(cur, longest)
    
    return longest

if __name__ == "__main__":
    unittest.main()