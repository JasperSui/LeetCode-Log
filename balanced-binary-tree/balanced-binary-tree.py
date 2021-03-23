# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        # Solution 1
        # Time: O(nlogn)
        # Space: O(height)
        if not root: return True
        def get_height(node):
            if not node: return 0
            return max(get_height(node.left), get_height(node.right)) +1
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        return (abs(left_height - right_height) <= 1) and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)