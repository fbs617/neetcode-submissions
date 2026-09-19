# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.inorder_dict = {}
        self.preorder_index = 0
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i, n in enumerate(inorder):
            self.inorder_dict[n] = i
        left = 0
        right = len(self.inorder_dict) - 1
        return self.buildHelper(preorder, left, right)

    def buildHelper(self, preorder, left, right):
        if left > right:
            return None
        root = TreeNode(preorder[self.preorder_index], None, None)
        self.preorder_index += 1
        root_i = self.inorder_dict[root.val]
        left1 = left
        right1 = root_i - 1
        left2 = root_i + 1
        right2 = right
        root.left = self.buildHelper(preorder, left1, right1)
        root.right = self.buildHelper(preorder, left2, right2)
        return root