import unittest

class quad_sumTests(unittest.TestCase):
    def test_quad_sum(self):
        self.assertTrue(
            quad_sum([1,4,2,6,8,11,12,9,15],15),
        )
    def test_quad_sum_false(self):
        self.assertFalse(
            quad_sum([1,4,2,6,8,11,12,9,15],55),
        )

def quad_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                for l in range(k+1, len(arr)):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        # print("%s,%s,%s,%s" % )
                        return True
    return False

# print(quad_sum([1,4,2,6,8,11,12,9,15],15))

if __name__ == "__main__":
    unittest.main()