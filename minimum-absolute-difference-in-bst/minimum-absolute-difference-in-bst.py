# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
        dfs(root)
        return min(self.res[i+1] - self.res[i] for i in range(len(self.res)-1))