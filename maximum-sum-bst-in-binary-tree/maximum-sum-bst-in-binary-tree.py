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
        # Time: O(n)
        # Space: O(h)
        self.traverse(root)
        return self.ans
    
    def traverse(self, node):
        """
        res[0]: is bst
        res[1]: max value of node
        res[2]: min value of node
        res[3]: sum of node
        """
        if not node: return [1, float('inf'), float('-inf'), 0]
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        res = [0] * 4
        
        # is bst
        if left[0] == 1 and right[0] == 1 and node.val > left[2] and node.val < right[1]:
            res[0] = 1
            res[1] = min(left[1], node.val)
            res[2] = max(right[2], node.val)
            res[3] = left[3] + right[3] + node.val
            self.ans = max(self.ans, res[3])
        return res