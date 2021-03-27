# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, s, d):
        if not node: return
        s += node.val
        old = s - self.t
        
        self.ans += d.get(old, 0)
        d[s] = d.get(s, 0) + 1
        
        self.dfs(node.left, s, d)
        self.dfs(node.right, s, d)
        d[s] -= 1
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Time: O(n)
        # Space: O(h)
        
        # dfs
        self.ans = 0
        self.t = sum
        d = {0: 1}
        
        self.dfs(root, 0, d)
        return self.ans