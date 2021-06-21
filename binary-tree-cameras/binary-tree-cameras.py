# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        leaf = 0
        camera = 1
        covered = 2
        self.ans = 0
        if not root: return 0
        def dfs(node):
            if not node: return covered
            l, r = dfs(node.left), dfs(node.right)
            if l == leaf or r == leaf:
                self.ans += 1
                return camera
            return covered if l == camera or r == camera else 0
        return (dfs(root) == 0) + self.ans
        
        
        # Time: O(n)
        # Space: O(height)
        
        # Recursive
        # Append the camera only on the leaves' parent
        # if not root: return 0
        # leaf = 0
        # camera = 1 # parent of leaf
        # covered = 2
        # self.ans = 0
        # def dfs(node):
        #     if not node: return covered
        #     l, r = dfs(node.left), dfs(node.right)
        #     if l == leaf or r == leaf:
        #         self.ans += 1
        #         return camera
        #     return covered if l == camera or r == camera else 0
        # return (dfs(root) == 0) + self.ans