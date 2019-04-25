import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            get_products([1,2,3,4]),
            [24, 12, 8, 6]
        )

def get_products(nums):
    prefix = []
    suffix = []
    result = []

    for num in nums:
        if prefix:
            prefix.append(prefix[-1] * num)
        else:
            prefix.append(num)

    for num in reversed(nums):
        if suffix:
            suffix.append(suffix[-1] * num)
        else:
            suffix.append(num)
    suffix = list(reversed(suffix))

    for i in range(len(nums)):
        if i == 0:
            result.append(suffix[i+1])
        elif i == len(nums) - 1:
            result.append(prefix[i-1])
        else:
            result.append(prefix[i-1] * suffix[i+1])
    return result

if __name__ == "__main__":
    unittest.main()


