# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(node):
            if not node: return
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if not node.left and not node.right and node.val == target:
                return None
            return node
        return dfs(root)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Time: O(N)
        # Space: O(height)
        
        # # DFS
        # if not root: return
        # root.left = self.removeLeafNodes(root.left, target)
        # root.right = self.removeLeafNodes(root.right, target)
        # if not root.left and not root.right and root.val == target: return
        # return root
        
        # Iterative
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                stack.append(curr.left)
                stack.append(curr.right)
                if not curr.left and not curr.right and curr.val == target:
                    curr = None
        return root