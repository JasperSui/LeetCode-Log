# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        
        # Time: O(N)
        # Space: O(height)
        
        # # Iterative
        # stack = [root]
        # while stack:
        #     curr = stack.pop()
        #     if not curr: return None
        #     if curr.val == val: return curr
        #     elif curr.val > val:
        #         stack.append(curr.left)
        #     else:
        #         stack.append(curr.right)
        
        # # Recursive
        def dfs(node):
            if not node: return
            if node.val == val:
                return node
            elif node.val > val:
                dfs(node.left)
            else: 
                dfs(node.right)
        return dfs(root)