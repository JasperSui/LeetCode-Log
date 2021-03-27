# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Time: O(n)
        # Space: O(height)
        
        # DFS
        ans = False
        def dfs(node, current_sum):
            nonlocal ans
            if not node: return
            current_sum += node.val
            if current_sum == targetSum and not node.left and not node.right:
                ans = True
            if node.left: dfs(node.left, current_sum)
            if node.right: dfs(node.right, current_sum)
        dfs(root, 0)
        return ans
        
            