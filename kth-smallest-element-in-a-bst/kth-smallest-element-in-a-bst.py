# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = 0
        rank = 0
        def traverse(node):
            nonlocal ans, rank
            if not node: return
            traverse(node.left)
            rank += 1
            if k == rank: ans = node.val
            traverse(node.right)
        traverse(root)
        return ans