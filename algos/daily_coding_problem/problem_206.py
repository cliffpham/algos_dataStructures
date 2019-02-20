# This problem was asked by Twitter.

# A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

# Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            apply_perm(['a', 'b', 'c'], [2,1,0]),
            ['c', 'b', 'a']
        )

def apply_perm(arr, perm):
    seen = dict()
    result = []

    for i, j in enumerate(arr):
        if j not in seen:
            seen[i] = j
 
    for i in perm:
        if i in seen:
            result.append(seen[i])

    return result

if __name__ == "__main__":
    unittest.main()
