from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
            
        depth = 0

        queue = deque([root])
        out = [[root.val]]
        
        while queue:
            level_size = len(queue)
            curr_depth_vals = []
            for i in range(level_size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    curr_depth_vals.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    curr_depth_vals.append(curr.right.val)
            if len(curr_depth_vals) > 0:
                out.append(curr_depth_vals)
        
        return out
                
            