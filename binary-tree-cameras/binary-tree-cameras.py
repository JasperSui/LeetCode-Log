# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(height)
        
        # Recursive
        # Append the camera only on the leaves' parent
        if not root: return 0
        self.ans = 0
        def dfs(node):
            if not node: return 2
            l, r = dfs(node.left), dfs(node.right)
            if l == 0 or r == 0:
                self.ans += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root) == 0) + self.ans