# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        self.d = defaultdict(lambda: float('-inf'))
        self.max_depth = float('-inf')
        def dfs(node, depth=1):
            if not node: return
            self.d[depth] = max(self.d[depth], node.val)
            self.max_depth = max(self.max_depth, depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root)
        return [self.d[depth] for depth in range(1, self.max_depth+1)]