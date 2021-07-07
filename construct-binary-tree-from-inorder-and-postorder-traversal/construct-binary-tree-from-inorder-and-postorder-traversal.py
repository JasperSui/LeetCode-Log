# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.d = {}
        for i, v in enumerate(inorder): self.d[v] = i
        def build(low, high):
            if low > high: return
            root = TreeNode(postorder.pop())
            mid = self.d[root.val]
            root.right = build(mid+1, high)
            root.left = build(low, mid-1)
            return root
        return build(0, len(inorder)-1)