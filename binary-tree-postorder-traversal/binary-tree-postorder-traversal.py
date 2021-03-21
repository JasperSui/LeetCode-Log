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
        
        # Recursive
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []