import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            next_greater_element([3,1,5,7,9,2,6], [1,2,3,5,6,7,9,11]),
            [5, 2, 6, 9, 11, 3, 7]
        ),
    def test2(self):
        self.assertEqual(
            next_greater_element([4,1,2], [1,3,4,2]),
            [-1,3,-1]
        )

def que_ify(arr):
    result = []
    while arr:
        i = arr.pop()
        result.append(i)
    return result

def next_greater_element(nums1, nums2):
    nums1 = que_ify(nums1)
    result = []

    while nums1:
        i = nums1.pop()

        if i in nums2:
            for k in range(len(nums2)):
                if i == nums2[k]:
                    j = k
                    if j < len(nums2)-1:
                        while j < len(nums2):
                            if i < nums2[j]:
                                result.append(nums2[j])
                                break
                            j += 1
                            if j == len(nums2):
                                result.append(-1)
                    else:
                        result.append(-1)
        else:
            result.append(-1)
                    
    return result

if __name__ == "__main__":
    unittest.main()
