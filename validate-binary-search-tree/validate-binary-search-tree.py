# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Time: O(n)
        # Space: O(height)
        
        # Recursive
        # self.res = True
        # def traverse(node, low, high):
        #     if not node: return
        #     traverse(node.left, low, node.val)
        #     traverse(node.right, node.val, high)
        #     if not low < node.val < high: self.res = False
        #     return node.val
        # traverse(root, float('-inf'), float('inf'))
        # return self.res
        
        # Iterative
        stack, prev, node = [], float('-inf'), root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev >= node.val: return False
            prev = node.val
            node = node.right
        return True