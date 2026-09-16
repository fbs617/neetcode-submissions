from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            curr, lo, hi = queue.popleft()
            if curr.val <= lo or curr.val >= hi:
                return False
            if curr.left:
                queue.append((curr.left, lo, curr.val))
            if curr.right:
                queue.append((curr.right, curr.val, hi))
        return True
            