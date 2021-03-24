# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(height)
        
        # Solution 1 (Recursive)
        if not root: return 0
        d = list(map(self.minDepth, (root.left, root.right)))
        return 1 + (min(d) or max(d))
        
        
        # # Solution 3 (Stupid)
        # self.min_depth = 50000000
        # if not root: return 0
        # def dfs(node, depth):
        #     if node:
        #         temp_depth = depth + 1
        #         if not node.left and not node.right:
        #             self.min_depth = min(self.min_depth, temp_depth)
        #         dfs(node.left, temp_depth)
        #         dfs(node.right, temp_depth)
        # dfs(root, 0)
        # return self.min_depth
        