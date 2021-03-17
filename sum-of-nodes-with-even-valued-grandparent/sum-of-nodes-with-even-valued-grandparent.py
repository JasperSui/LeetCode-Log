# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, p=None, gp=None):
            nonlocal ans
            if not node: return
            if p and gp and gp.val % 2 == 0:
                ans += node.val
            dfs(node.left, node, p)
            dfs(node.right, node, p)
        dfs(root, None, None)
        return ans