import unittest

class max_valTests(unittest.TestCase):
    def test_max_val(self):
        self.assertEqual(
            max_val([-1,10,4,3,12,]),
            12
        )
    def test_max_val_empty(self):
        self.assertEqual(
            max_val([]),
            float('-inf')
        )

def max_val(arr):
    
    max_val = float('-inf')
    
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]

    return max_val

if __name__ ==  "__main__":
    unittest.main()

