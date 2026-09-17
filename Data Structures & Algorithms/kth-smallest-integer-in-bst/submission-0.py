# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            # go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            # visit node
            curr = stack.pop()
            k = k-1
            if k == 0:
                return curr.val
            curr = curr.right
            




        #     lefts.append(curr)
        #     curr = curr.left
        # curr, parent = lefts.pop(), lefts.pop()
        # in_order.append(curr)
        # in_order.append(parent)
        # curr = parent.right
        # while curr:
        #     curr = curr.left
            
        