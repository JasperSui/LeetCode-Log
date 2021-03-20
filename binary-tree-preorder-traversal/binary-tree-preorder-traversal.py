# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Time: O(N)
        # Space: O(height)
        
        # # Recursive
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
    
        # Iterative
        if not root: return []
        res, stack = [], [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
            
        return res
        