# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
import unittest 

class test(unittest.TestCase):
    def test1(self):
        self.assertCountEqual(
            subsetsWithDup([1,2,2]),
            [[2],[1],[1,2,2],[2,2],[1,2],[]]
        )


def subsetsWithDup(nums):
    return recur(nums, 0, [], [])

def recur(nums, i, cur, output):
    if i >= len(nums):
        if cur != None:
             cur = sorted(cur)
        if cur not in output:
            output.append(cur[:])
        return
    
    recur(nums, i+1, cur, output)
    
    cur.append(nums[i])
    recur(nums, i+1, cur, output)
    cur.pop()
    
    return output

if __name__ == "__main__":
    unittest.main()
        