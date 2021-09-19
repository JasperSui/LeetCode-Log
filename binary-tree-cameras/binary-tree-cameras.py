# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        LEAF, CAMERA, COVERED = 0, 1, 2
        self.ans = 0
        if not root: return 0
        def dfs(node):
            if not node: return COVERED
            l = dfs(node.left)
            r = dfs(node.right)
            if l == LEAF or r == LEAF:
                self.ans += 1
                return CAMERA
            return COVERED if l == CAMERA or r == CAMERA else LEAF
        
        return (dfs(root) == LEAF) + self.ans
        