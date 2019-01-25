import unittest

class triplet_sumTests(unittest.TestCase):
    def test_triplet_sum(self):
        self.assertTrue(
            triplet_sum([1,9,6,5,17,4,2],23),
            # True
        )
    def test_triplet_sum_false(self):
        self.assertFalse(
            triplet_sum([1,8,4,17,3,2,5],35),
        )

def triplet_sum(arr, target):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                result.append((arr[i],arr[j], arr[k]))
                if arr[i] + arr[j] + arr[k] == target:
                    # print("%s,%s,%s" % (arr[i],arr[j],arr[k]))
                    return True
    return False

if __name__ == "__main__":
    unittest.main()