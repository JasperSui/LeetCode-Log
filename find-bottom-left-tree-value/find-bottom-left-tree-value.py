# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.d = defaultdict(list)
        self.max_depth = float('-inf')
        def dfs(node, depth=1):
            if not node: return
            self.d[depth].append(node.val)
            self.max_depth = max(self.max_depth, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root)
        return self.d[self.max_depth][0]