class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)
        return 1 + max(right_depth, left_depth)