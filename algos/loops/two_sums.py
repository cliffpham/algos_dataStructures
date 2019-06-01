import unittest

# store the the values in the arr and the index in a new arr
# sort the new arr so that you can use the two pointer method
# with the two pointer method on a sorted arr with access to its index you can solve it one loop

class test_two_sum(unittest.TestCase):
     def test1_two_sum(self):
         self.assertEqual(
             solve([2,7,11,15], 9),
             [0,1]
         )

def solve(arr, target):
    result = []
    ans = []
    i = 0
    j = len(arr)-1
    
    for n in range(len(arr)):
        result.append((arr[n], n))
    result.sort()
    
    while i < j:
        if result[i][0] + result[j][0] == target:
            ans.append(result[i][1])
            ans.append(result[j][1])
            break
        if result[i][0] + result[j][0] > target:
            j -= 1
        if result[i][0] + result[j][0] < target:
            i += 1
    return ans

if __name__ == "__main__":
     unittest.main()
