# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDepth(root)
        return self.balanced
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)
        if abs(right_depth - left_depth) > 1:
            self.balanced = False
        return 1 + max(right_depth, left_depth) 