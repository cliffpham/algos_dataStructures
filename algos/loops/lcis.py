import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            lcis([1,3,5,4,7]),
            3
        ),
    def test2(self):
        self.assertEqual(
            lcis([]),
            0
        )

def lcis(arr):
    l = 0
    cur_count = 0
    max_count = 0
    
    while l < len(arr) - 1:
        if arr[l] < arr[l+1]:
            cur_count += 1
            max_count = max(cur_count, max_count) 
            l += 1
        else:
            cur_count = 0
            l += 1
    
    if len(arr) >= 1:
        return max_count +1
    else:
        return max_count

if __name__ == "__main__":
    unittest.main()