# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -1001
        def dfs(node):
            if not node: return 0
            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)
            s = node.val + l + r
            self.ans = max(self.ans, s)
            return node.val + max(l, r)
        dfs(root)
        return self.ans
        
        
        # Time: O(n)
        # Space: O(height)
        
        # # Recursive
        # if not root: return 0
        # ans = -1001
        # def dfs(node):
        #     if not node: return 0
        #     nonlocal ans
        #     l = max(dfs(node.left), 0)
        #     r = max(dfs(node.right), 0)
        #     s = node.val + l + r
        #     ans = max(ans, s)
        #     return node.val + max(l, r)
        # dfs(root)
        # return ans
        
        
        if not root: return 0
        ans = -1001
        def dfs(node):
            nonlocal ans
            if not node: return 0
            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)
            s = node.val + l + r
            ans = max(ans, s)
            return node.val + max(l, r)
        dfs(root)
        return ans
        