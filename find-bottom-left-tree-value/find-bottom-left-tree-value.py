# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.d = defaultdict(list)
        self.level = 0
        if not root: return 0
        def dfs(node, level=1):
            if not node: return
            dfs(node.left, level+1)
            self.level = max(self.level, level)
            self.d[level].append(node.val)
            dfs(node.right, level+1)
        dfs(root)
        return self.d[self.level][0]