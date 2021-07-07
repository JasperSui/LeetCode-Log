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
        def dfs(node):
            if not node: return
            dfs(node.left)
            if self.prev.val >= node.val:
                if not self.first_node:
                    self.first_node = self.prev
                if self.first_node:
                    self.second_node = node
            else:
                self.prev = node
            dfs(node.right)
        dfs(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val