# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, is_left=False):
            if not node: return
            if not node.left and not node.right and is_left:
                self.ans += node.val
            dfs(node.left, True)
            dfs(node.right, False)
        dfs(root)
        return self.ans