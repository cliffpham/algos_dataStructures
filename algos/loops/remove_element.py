import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([3,3], 3),
            0
        ),
    def test2(self):
        self.assertEqual(
            solve([0,1,2,2,3,0,4,2], 2),
            5
        )

def solve(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    return len(nums[:j])

if __name__ == "__main__":
    unittest.main()

# first attempt
# def solve(nums, val):
    # count = 0
    # left = 0
    # right = len(nums) - 1
    # for n in nums:
    #     if n == val:
    #         count += 1

    # while left < right:
    #     if nums[right] == val:
    #         while right != left:
    #             if nums[right] == val:
    #                 right -= 1
    #             else:
    #                 break
    #     if nums[left] == val:
    #         nums[left] = nums[right]
    #         nums[right] = val
    #         left += 1
    #     else:
    #         left += 1
    # return len(nums) - count



