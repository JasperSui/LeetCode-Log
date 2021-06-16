# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node: return
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if not node.val and not node.left and not node.right: return
            return node
        return dfs(root)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Time: O(n)
        # Space: O(height)
        
        # # Recursion
        # if not root: return None
        # root.left = self.pruneTree(root.left)
        # root.right = self.pruneTree(root.right)
        # if not root.left and not root.right and not root.val: return None
        # return root
        
        # Iterative
        stack = [(0, root)]
        while stack:
            seen, node = stack.pop()
            if node is None:
                continue
            if not seen:
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                if node.left and not (node.left.val or node.left.left or node.left.right):
                    node.left = None
                if node.right and not (node.right.val or node.right.left or node.right.right):
                    node.right = None
        return root
