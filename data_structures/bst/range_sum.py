# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R, accum=0, keep =[], used={}):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
       
        q = [root]
        used = {}
        accum = 0
        
        while q:
            cur = q.pop()
            if cur.val >= L and cur.val <= R:
                if cur.val not in used:
                    accum += cur.val
                    used[cur.val] = True
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        
        return accum