# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.good_nodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.good_nodes

    def dfs(self, root, path_max):
        if root == None:
            return
        if root.val >= path_max:
            self.good_nodes += 1
            path_max = root.val
        self.dfs(root.left, path_max)
        self.dfs(root.right, path_max)
        