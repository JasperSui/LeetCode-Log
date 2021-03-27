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
        
        # # Recursion
        # if not root: return None
        # root.left = self.pruneTree(root.left)
        # root.right = self.pruneTree(root.right)
        # if not root.left and not root.right and not root.val: return None
        # return root
        
        # Iterative
        if not root: return root
        fr = TreeNode(1) # Fake root
        fr.left = root
        stack = [(0, root, fr)] # (seen, node, parent)
        while stack:
            seen, node, parent = stack.pop()
            if not node: continue
            if not seen:
                stack += [(1, node, parent)]
                stack += [(0, node.left, node)]
                stack += [(0, node.right, node)]
            else:
                if node.val == 0 and not node.left and not node.right:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
        return fr.left