# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(height)
        
        # Recursive
        if root is None: return 0
        self.ans = 0
        
        def dfs(node):
            part_path = 0
            total_path = 0
            if node:
                if node.left:
                    l = dfs(node.left)
                    if node.val == node.left.val:
                        total_path = part_path = 1 + l
                
                if node.right:
                    r = dfs(node.right)
                    if node.val == node.right.val:
                        part_path = max(part_path, 1 + r)
                        total_path += 1 + r
                
                self.ans = max(self.ans, total_path)
            return part_path
        dfs(root)
        return self.ans
                