# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        def dfs(node):
            if not node: return
            if node.val > R:
                dfs(node.left)
            elif node.val < L:
                dfs(node.right)
            else:
                dfs(node.left)
                dfs(node.right)
                
            if L <= node.val <= R: self.ans += node.val
        dfs(root)
        return self.ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.ans = 0
        # def calc(root, L, R):
        #     if not root:
        #         return None
        #     if root.val and L <= root.val <= R:
        #         self.ans += root.val
        #     calc(root.left, L, R)
        #     calc(root.right, L, R)
        # calc(root, L, R)
        # return self.ans
        if not root:
            return 0
        return self.rangeSumBST(root.left, L, R) + \
               self.rangeSumBST(root.right, L, R) + \
               (root.val if L <= root.val <= R else 0)