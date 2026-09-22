# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum(root)
        return self.max_sum
        
    def maxSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        right_sum = max(0, self.maxSum(root.right))
        left_sum = max(0, self.maxSum(root.left))
        joint_sum = right_sum + root.val + left_sum
        self.max_sum = max(self.max_sum, joint_sum)
        return root.val + max(left_sum, right_sum)