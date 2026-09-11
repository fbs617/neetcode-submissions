# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.diameter
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)
        self.diameter = max(self.diameter, left_depth + right_depth)
        return 1 + max(right_depth, left_depth) 