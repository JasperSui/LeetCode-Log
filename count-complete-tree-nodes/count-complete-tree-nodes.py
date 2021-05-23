# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        def get_depth(node):
            if not node: return 0
            return 1 + get_depth(node.left)

        if not root: return 0
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        
        if left_depth == right_depth:
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            return pow(2, right_depth) + self.countNodes(root.left)
        