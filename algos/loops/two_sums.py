# import unittest

# class test_two_sum(unittest.TestCase):
#     def test1_two_sum(self):
#         self.assertEquals(
#             two_sum([2,7,11,15], 9)
#             [0,1]
#         )

def two_sum(arr, target):
    i = 0
    j = len(arr) - 1
    ans = []

    while i < j:
        if arr[i] + arr[j] == target:
            ans.append(i)
            ans.append(j)
            break

        if arr[i] + arr[j] > target:
            j -= 1

        if arr[i] + arr[j] < target:
            i += 1

    return ans

# print(two_sum([2,7,11,15], 9))

# if __name__ == "__main__":
#     unittest.main()