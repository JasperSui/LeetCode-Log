# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Time: O(N)
        # Space: O(height)
        
        # # Iterative
        # sp = [p]
        # sq = [q]
        # while sp or sq:
        #     n1 = sp.pop()
        #     n2 = sq.pop()
        #     if n1 or n2:
        #         if not n1 or not n2: return False
        #         if n1.val != n2.val: return False
        #         sp.append(n1.left)
        #         sp.append(n1.right)
        #         sq.append(n2.left)
        #         sq.append(n2.right)
        # return True
        
        # Recursive
        if not p or not q: return p == q
        if p.val != q.val: return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)