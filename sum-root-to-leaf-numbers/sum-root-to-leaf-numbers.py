# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(height)
        
        # DFS
        res = []
        def dfs(node, l):
            if not node: return
            l = [*l, str(node.val)]
            if not node.left and not node.right: res.append(l)
            dfs(node.left, l)
            dfs(node.right, l)
        dfs(root, [])
        return sum(map(lambda x: int(''.join(x)), res))