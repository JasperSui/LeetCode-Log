# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        s = 0
        def convert(node):
            nonlocal s
            if not node: return
            convert(node.right)
            
            s += node.val
            node.val = s
            
            convert(node.left)
        convert(root)
        return root
            