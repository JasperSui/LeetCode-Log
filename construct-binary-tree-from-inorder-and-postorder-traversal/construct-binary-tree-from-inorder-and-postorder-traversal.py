# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        d = {v: i for i, v in enumerate(inorder)}
        def build(low, high):
            if low > high: return
            root = TreeNode(postorder.pop())
            index = d[root.val]
            root.right = build(index+1, high)
            root.left = build(low, index-1)
            return root
        return build(0, len(inorder)-1)