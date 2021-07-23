# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        self.res = False
        def check(n1, n2):
            if not n1 and not n2: return True
            if not n1 or not n2: return False
            if n1.val != n2.val: return False
            return check(n1.left, n2.left) and check(n1.right, n2.right)

        def dfs(node):
            if not node: return
            if node.val == subRoot.val:
                if check(node, subRoot): self.res = True
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res
            