# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.d = {}
        for i, v in enumerate(inorder): self.d[v] = i
        def build(low, high):
            if low > high: return
            root = TreeNode(preorder.pop(0))
            mid = self.d[root.val]
            root.left = build(low, mid-1)
            root.right = build(mid+1, high)
            return root
        return build(0, len(inorder)-1)
        
        # if inorder:
        #     index = inorder.index(preorder.pop(0))
        #     root = TreeNode(inorder[index])
        #     root.left = self.buildTree(preorder, inorder[:index])
        #     root.right = self.buildTree(preorder, inorder[index+1:])
        #     return root