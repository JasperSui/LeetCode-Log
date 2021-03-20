# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Time: O(N)
        # Space: O(height)
        # Iterable
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr: return None
            if curr.val == val: return curr
            elif curr.val > val:
                stack.append(curr.left)
            else:
                stack.append(curr.right)