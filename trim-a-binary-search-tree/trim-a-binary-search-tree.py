# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        while root and not (L <= root.val <= R):
            if root.val < L:
                root = root.right
            elif root.val > R:
                root = root.left
        stack = [root]
        while stack:
            curr = stack[-1]
            if curr is None:
                stack.pop()
                continue
            updated = 0
            if curr.left and curr.left.val < L:
                curr.left = curr.left.right
                updated += 1
            if curr.right and curr.right.val > R:
                curr.right = curr.right.left
                updated += 1
            if not updated:
                stack.pop()
                stack.append(curr.left)
                stack.append(curr.right)
        return root
        
        # def trim(node):
        #     if not node: return
        #     if node.val > R: return trim(node.left)
        #     if node.val < L: return trim(node.right)
        #     node.left = trim(node.left)
        #     node.right = trim(node.right)
        #     return node
        # trim(root)
        # return root
        
        
        
        
        # Time: O(n)
        # Space: O(height)
        
        # # DFS
        # if not root: return None
        # if root.val > R: return self.trimBST(root.left, L, R)
        # if root.val < L: return self.trimBST(root.right, L, R)

        # root.left = self.trimBST(root.left, L, R)
        # root.right = self.trimBST(root.right, L, R)
        
        # return root
        
        # Iterative
        while root and not (L <= root.val <= R):
            if root.val < L: root = root.right
            elif root.val >R: root = root.left
        stack = [root]
        while stack:
            curr = stack[-1]
            if curr is None: stack.pop(); continue
            updated = 0
            if curr.left and curr.left.val < L:
                curr.left = curr.left.right
                updated += 1
            if curr.right and curr.right.val > R:
                curr.right = curr.right.left
                updated += 1
            if not updated:
                stack.pop()
                stack.append(curr.left)
                stack.append(curr.right)
        return root