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
        self.first_element = None
        self.second_element = None
        self.prev = TreeNode(float('-inf'))
        
        def inorder(node):
            if not node: return
            inorder(node.left)
            if self.prev.val >= node.val:
                if not self.first_element:
                    self.first_element = self.prev
                if self.first_element:
                    self.second_element = node
            self.prev = node
            inorder(node.right)
        inorder(root)
        self.first_element.val, self.second_element.val = self.second_element.val, self.first_element.val