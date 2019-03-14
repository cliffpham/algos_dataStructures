import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([4,3,2,7,8,2,3,1]),
            [5,6]
        )

def solve(nums):
    result = []
    check = set(nums)

    for i in range(1, len(nums)+1):
        if i not in check:
            result.append(i)
    
    return result

if __name__ == "__main__":
    unittest.main()

# def solve(nums):
#     # compare = [False for _ in range(len(nums))]
#     result = []

#     for i in range(1, len(nums)+1):
#         if i in nums:                     <----- The cost of searching for an item in a list is O(N)
#             # compare[i-1] = True
#             continue
#         else:
#             result.append(i)

#     # for i in range(len(compare)):
#     #     if compare[i] == False:
#     #         result.append(i+1)

#     return result


