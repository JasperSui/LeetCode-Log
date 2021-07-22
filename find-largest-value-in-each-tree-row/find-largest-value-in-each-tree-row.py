# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            new_stack = []
            curr_max = float('-inf')
            for node in stack:
                if node:
                    curr_max = max(curr_max, node.val)
                    new_stack.append(node.left)
                    new_stack.append(node.right)
            if curr_max != float('-inf'):
                res.append(curr_max)
            stack = new_stack
        return res