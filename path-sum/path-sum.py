# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.ans = False
        def dfs(node, curr_sum=0):
            if not node: return
            curr_sum += node.val
            if curr_sum == targetSum and not node.left and not node.right: self.ans = True
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            return
        dfs(root)
        return self.ans