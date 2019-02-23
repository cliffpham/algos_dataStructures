# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        pivot, max_val = max(enumerate(nums), key=lambda x : x[1])
        
        node = TreeNode(max_val)
        
        node.left = self.constructMaximumBinaryTree(nums[:pivot])
        node.right = self.constructMaximumBinaryTree(nums[pivot + 1:])
        
        
        return node