# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Time: O(N)
        # Space: O(height)
        
        # # Recursive
        # def dfs(n, l):
        #     if n.left: dfs(n.left, l)
        #     if n.right: dfs(n.right, l)
        #     if not n.left and not n.right:
        #         l.append(n.val)
        #     return l # Should return l at every single last situation
        # return dfs(root1, []) == dfs(root2, [])
        
        # Iterative
        s1, s2, l1, l2 = [root1], [root2], [], []
        while s1:
            curr = s1.pop()
            if curr:
                if not curr.left and not curr.right: 
                    l1.append(curr.val)
                    continue
                s1.append(curr.left)
                s1.append(curr.right)
                
        while s2:
            curr = s2.pop()
            if curr:
                if not curr.left and not curr.right: 
                    l2.append(curr.val)
                    continue
                s2.append(curr.left)
                s2.append(curr.right)
        return l1 == l2