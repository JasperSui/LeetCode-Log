# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Time: O(N)
        # Space: O(height)
        
        # # Recursive
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
        
        # # Iterative (Cool Version)
        # # Using flag to record if the node is visited
        # res, stack = [], [(root, False)]
        # while stack:
        #     node, visited = stack.pop()
        #     if node:
        #         if visited:
        #             res.append(node.val)
        #         else:
        #             stack.append((node, True))
        #             stack.append((node.right, False))
        #             stack.append((node.left, False))
        # return res
        
        # Iterative 2
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]