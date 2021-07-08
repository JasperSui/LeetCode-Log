# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.res = False
        def dfs(node, target=targetSum):
            if not node: return
            next_target = target-node.val
            if not node.left and not node.right and next_target == 0: self.res = True
            dfs(node.left, next_target)
            dfs(node.right, next_target)
        dfs(root)
        return self.res