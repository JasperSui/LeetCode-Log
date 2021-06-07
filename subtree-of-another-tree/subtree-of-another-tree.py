# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def check(n1, n2):
            if not n1 and not n2: return True
            if not n1 or not n2: return False
            if n1.val != n2.val: return False
            return check(n1.left, n2.left) and check(n1.right, n2.right)
        
        def dfs(n1, n2):
            if not n1: return False
            if n1.val == n2.val and check(n1, n2): return True
            return dfs(n1.left, t) or dfs(n1.right, t)
        return dfs(s, t)
                
                
                
        
        
#         # Time: O(S*T)
#         # Space: O(height)
        
#         # Solution 1 (Recursive)
#         if not t: return True
#         def check(n1, n2):
#             if not n1 and not n2: return True
#             if not n1 or not n2: return False
#             if n1.val != n2.val: return False
#             return check(n1.left, n2.left) and check(n1.right, n2.right)
        
#         def dfs(n1, n2):
#             if not n1: return False
#             if n1.val == n2.val and check(n1, n2): return True
#             return dfs(n1.left, t) or dfs(n1.right, t)
        
#         return dfs(s, t)
        