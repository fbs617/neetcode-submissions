# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = self.helper(p,q)
        if result == 0:
            return True
        return False
    
    def helper(self, p, q):
        if p == None and q == None:
            return 0
        elif p == None or q == None:
            return 1
        if p.val != q.val:
            return 1
        return 0 + self.helper(p.left, q.left) + self.helper(p.right, q.right)