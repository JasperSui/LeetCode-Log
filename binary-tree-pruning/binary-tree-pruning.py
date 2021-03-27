# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # Time: O(n)
        # Space: O(height)
        
        # Recursion
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val: return None
        return root
        
        # Iterative
        stack = [(root, False)]
        while stack:
            curr, visited = stack.pop()
            if not visited:
                stack.append((curr, True))
                stack.append((curr.left, False))
                stack.append((curr.right, False))
            else:
                if curr.left and curr.left.val == -1:
                    curr.left = None
                if curr.right and curr.right.val == -1:
                    curr.right = None
                if not curr.left and not curr.right:
                    if curr.val == 0:
                        curr.val = -1
        return root