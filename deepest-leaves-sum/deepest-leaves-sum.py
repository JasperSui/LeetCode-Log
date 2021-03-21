# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # Time: O(N)
        # Space: O(height)
        
        # Iterative
        d = defaultdict(int)
        l = 0
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                if not node.left and not node.right:
                    d[level] += node.val
                    l = max(l, level)
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
            
        return d[l]