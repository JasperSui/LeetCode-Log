# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder)-1,
                          inorder, 0, len(inorder)-1)
        
    def build(self, preorder, pre_s, pre_e,
              inorder, in_s, in_e):
        if pre_s > pre_e: return
        root_val = preorder[pre_s]
        index = 0
        for i, v in enumerate(inorder):
            if v == root_val:
                index = i
                break
        left_size = index - in_s
        root = TreeNode(root_val)
        root.left = self.build(preorder, pre_s+1, pre_s+left_size,
                               inorder, in_s, index-1)
        root.right = self.build(preorder, pre_s+left_size+1, pre_e,
                               inorder, index+1, in_e)
        return root