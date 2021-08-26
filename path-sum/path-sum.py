# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        def dfs(node, target=targetSum):
            if not node: return
            if not node.left and not node.right and target == node.val: self.res = True
            dfs(node.left, target-node.val)
            dfs(node.right, target-node.val)
        dfs(root)
        return self.res