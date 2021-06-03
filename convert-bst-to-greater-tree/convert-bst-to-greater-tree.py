# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.val = 0
        def visit(node):
            if not node: return
            visit(node.right)
            node.val += self.val
            self.val = node.val
            visit(node.left)
        visit(root)
        return root