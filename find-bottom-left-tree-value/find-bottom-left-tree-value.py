# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.bottom_left_value = float('inf')
        self.max_level = 0
        def dfs(node, level=1):
            if not node: return
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            if level > self.max_level:
                self.max_level = level
                self.bottom_left_value = node.val
        dfs(root)
        return self.bottom_left_value if self.bottom_left_value != float('inf') else root.val