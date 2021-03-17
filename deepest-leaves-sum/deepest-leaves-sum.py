# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        d = defaultdict(int)
        def dfs(node, level=0):
            if not node: return
            d[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root)
        _, ans = d.popitem()
        return ans