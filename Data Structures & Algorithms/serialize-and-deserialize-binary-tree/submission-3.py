# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def __init__(self):
        self.preorder = []
        self.inorder = []
        self.inorder_indices = {}
        self.preorder_index = 0
        self.curr_node_id = 0
        self.node_ids = {}
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.getPreOrder(root)
        self.getInOrder(root)
        preord = ",".join(self.preorder)
        inord = ",".join(self.inorder)
        joint = preord + "+" + inord
        return joint
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preord, inord = data.split("+")
        if len(preord) == 0:
            return None
        preord = preord.split(",")
        inord = inord.split(",")
        for i, n in enumerate(inord):
            self.inorder_indices[n] = i
        def helper(preorder, left, right):
            if left > right:
                return None
            token = preorder[self.preorder_index]
            val = preorder[self.preorder_index].split("#")[0]
            val = int(val)
            root = TreeNode(val, None, None)
            self.preorder_index += 1
            root_i = self.inorder_indices[token]
            left1 = left
            right1 = root_i - 1
            left2 = root_i + 1
            right2 = right
            root.left = helper(preorder, left1, right1)
            root.right = helper(preorder, left2, right2)
            return root
        return helper(preord, 0, len(preord) - 1)

    def getInOrder(self, node):
        if node == None:
            return
        node_id = self.node_ids[node]
        self.getInOrder(node.left)
        self.inorder.append(str(node.val) + "#" + str(node_id))
        self.getInOrder(node.right)
    
    def getPreOrder(self, node):
        if node == None:
            return
        node_id = self.curr_node_id
        self.curr_node_id += 1
        self.node_ids[node] = node_id
        self.preorder.append(str(node.val) + "#" + str(node_id))
        self.getPreOrder(node.left)
        self.getPreOrder(node.right)

# def helper(pre_left, pre_right, in_left, in_right):
        #     if pre_left > pre_right:
        #         return None
        #     val = preord[pre_left]
        #     node = TreeNode(int(val), None, None)
        #     pre_left = pre_left + 1
        #     mid = self.inorder_indices[val]
        #     pre_j = pre_right
        #     node.left = helper(pre_left, mid, in_left, mid - 1)
        #     node.right = helper(mid + 1, pre_right, mid + 1, in_right)
        #     return node