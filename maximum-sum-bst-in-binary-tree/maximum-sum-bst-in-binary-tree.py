# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    
    def maxSumBST(self, root: TreeNode) -> int:
        self.is_valid_bst(root)
        return self.ans
    
    def is_valid_bst(self, node):
        if not node: return [True, float('inf'), float('-inf'), 0]
        l = self.is_valid_bst(node.left)
        r = self.is_valid_bst(node.right)
        res = [0] * 4
        if l[0] and r[0] and l[2] < node.val and r[1] > node.val:
            res[0] = True
            res[1] = min(l[1], node.val)
            res[2] = max(r[2], node.val)
            res[3] = l[3] + r[3] + node.val
            self.ans = max(self.ans, res[3])
        return res