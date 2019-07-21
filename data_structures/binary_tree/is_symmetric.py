# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def solve(root1, root2):
    if not root1 and not root2:
        return True
    
    if root1 and root2:
        if root1.val == root2.val:
            return solve(root1.left, root2.right) and solve(root1.right, root2.left)
    
    return False

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return solve(root, root)
