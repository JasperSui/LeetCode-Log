# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Time: O(N)
        # Space: O(height)
        
        # Recursive
        def dfs(n, l):
            if n.left: dfs(n.left, l)
            if n.right: dfs(n.right, l)
            if not n.left and not n.right:
                l.append(n.val)
            return l # Should return l at every single last situation

        return dfs(root1, []) == dfs(root2, [])