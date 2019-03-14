# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def recur(root, k, result):
    
        if not root:
            return
        
        result.append(root.val)
        
        recur(root.left, k, result)
        recur(root.right, k, result)
        
        return result

class Solution(object):
    def kthSmallest(self, root, k, result=[]):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        result = recur(root, k, [])
        result.sort()
        
        return result[k-1]