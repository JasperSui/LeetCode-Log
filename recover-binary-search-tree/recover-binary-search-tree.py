# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first_node, self.second_node = None, None
        self.prev = TreeNode(float('-inf'))
        def inorder(node):
            if not node: return
            inorder(node.left)
            if self.prev.val >= node.val:
                if self.first_node is None:
                    self.first_node = self.prev
                if self.first_node:
                    self.second_node = node
            self.prev = node
            inorder(node.right)
        inorder(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val