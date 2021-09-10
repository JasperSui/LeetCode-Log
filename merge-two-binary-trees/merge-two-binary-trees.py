# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(n1, n2):
            if not n1 and not n2: return
            if not n1 or not n2: return n1 or n2
            n3 = TreeNode(n1.val + n2.val)
            n3.left = dfs(n1.left, n2.left)
            n3.right = dfs(n1.right, n2.right)
            return n3
        return dfs(root1, root2)