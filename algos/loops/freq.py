import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            freq([2,2,2,2,1,1,1,3,3], 2),
            [2,1]
        )
    def test2(self):
        self.assertEqual(
            freq([-1,-1], 1),
            [-1]
        )

def freq(arr, k):      
    count = {}
    result = []
        
    for i in range(len(arr)):
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1
    
    for val in sorted(count, key=count.get, reverse=True):
        result.append(val)

    return result[:k]

if __name__ == "__main__":
    unittest.main()